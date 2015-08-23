from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Device
from oemfinal.serializers import DevicesSerializer
from .forms import DeviceForm
from django.contrib.auth.decorators import login_required
import tweepy
from mysite.settings import consumer_key, consumer_secret, access_token, access_token_secret


# Create your views here.
@login_required(login_url='accounts/login/')
def device_list(request):
    devices = Device.objects.all()
    return render(request, 'oemfinal/device_list.html', {'devices' : devices})

@login_required
def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    oem = device.oem
    codename = device.dev_CodeName
    marketname = device.dev_MarketName
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    keyword = oem
    #device.tweets = api.search(q=keyword)

    results =api.search(q=keyword)

    for result in results:
        device.tweet = result.text

    return render(request, 'oemfinal/device_detail.html', {'device' : device})

@login_required
def device_new(request):
    if request.method == "POST":
            form = DeviceForm(request.POST)
            if form.is_valid():
                device = form.save(commit=False)
                device.productManager = request.user
                device.save()
                return redirect('oemfinal.views.device_detail', pk=device.pk)
    else:
            form = DeviceForm()
    return render(request, 'oemfinal/device_edit.html', {'form': form})

@login_required
def device_edit(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == "POST":
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            device = form.save(commit=False)
            device.productManager = request.user
            device.save()
            return redirect('oemfinal.views.device_detail', pk=device.pk)
    else:
        form = DeviceForm(instance=device)
    return render(request, 'oemfinal/device_edit.html', {'form': form})

#@login_required
#def gettweets():
#    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#    auth.set_access(access_token, access_token_secret)
#    keyword = {{ device }}
#    api = tweepy.API(auth)
#    tweets = api.search(q=keyword)

#    for tweet in tweets:
#        print tweet.text



@login_required
@api_view(['GET', 'POST'])
def device_listAPI(request, format=None):
    if request.method == "GET":
        devices = Device.objects.all()
        serializer = DevicesSerializer(devices, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = DevicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET', 'POST', 'DELETE'])
def device_detailAPI(request, pk, format=None):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DevicesSerializer(device)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DevicesSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)