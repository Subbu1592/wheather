from django.shortcuts import render
import json
import requests
import datetime
# Create your views here.
def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'bangalore'

    appid = '9bc6825457e67fae2be85069044feff8'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':'bangalore', 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()
    return render(request, 'home.html', {'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city})