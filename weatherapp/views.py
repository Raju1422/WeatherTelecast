from django.shortcuts import render
from django.conf import settings
import requests
def get_weather_data(city):
    try:
        url=f"http://api.weatherapi.com/v1/current.json?key={settings.KEY}&q={city}"
        response =requests.get(url)
        data= response.json()
        return data
    except Exception as e:
        return e
def home(request):
    if request.method == "POST":
        city = request.POST.get("city")
        weather_data = get_weather_data(city)
        if 'error' in weather_data:
            error_message = weather_data['error']['message']
            return render(request, 'home.html', {'error_message': error_message})
        else:
            return render(request, 'home.html', {'weather_data': weather_data})
    
    return render(request,'home.html')
    