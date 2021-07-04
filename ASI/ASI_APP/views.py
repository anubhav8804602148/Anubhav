# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import HttpResponse
from django.shortcuts import render
import urllib2
from django.views.decorators.csrf import csrf_exempt
from models import Insurance
# Create your views here.


def default(request):
  return render(request, "info.html")


id = 0
@csrf_exempt
def home(request):
  global id
  #urllib2.urlopen(request.path, {"name":"Anubhav"})
  if request.method == 'GET':
    return render(request, 'home.html', {
      'data':getFullData(getData(id))
    })
  if request.method == 'POST':
    id = int(request.body.replace('\"',""))
    return render(request, 'home.html')

def getFullData(datax):
  if datax is None:
    res = {}
    res['id'] = "\n"
    res['name'] = "\n"
    res['address'] = "\n"
    res['amount'] = "\n"
    return res

  print "name : " + datax.name 
  res = {}
  res['id'] = str(datax.id)+"\n"
  res['name'] = datax.name+"\n"
  res['address'] = datax.address+"\n"
  res['amount'] = str(datax.amount)+"\n"
  return res

def getData(ais_id):
  res = Insurance.objects.filter(id=ais_id)
  try:
    return res.get()
  except :
    return None
  '''
  for lines in open(r'myData.csv').read():
    if ais_id in lines:
      return lines
      '''
