from django.shortcuts import render
from django.http import JsonResponse
import json
import requests

def getCities():    
    url = 'https://dc.tintoc.net/app/api-customer/public/provinces'
    r = requests.get(url)
    if r.status_code == 200:
        city_json = r.json()
        cities = [(item['id'], item['name']) for item in city_json]
        return cities
    return []

def getDistrictsInCity(request, city_id):
    url = 'https://dc.tintoc.net/app/api-customer/public/districts?provinceId.equals='+str(city_id)
    r = requests.get(url)
    if r.status_code == 200:
        districts = [(item['id'],item['name']) for item in r.json()]
        return JsonResponse(districts, safe=False)
    return JsonResponse({})
def getWardsInDistrict(request, district_id):
    url = 'https://dc.tintoc.net/app/api-customer/public/wards?districtId.equals='+str(district_id)
    r = requests.get(url)
    if r.status_code == 200:
        wards = [(item['id'],item['name']) for item in r.json()]
        return JsonResponse(wards, safe=False)
    return JsonResponse({})