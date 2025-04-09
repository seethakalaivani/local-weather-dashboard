import requests
from django.shortcuts import render

def index(request):
    weather_data = None
    if request.method == "POST":
        city = request.POST.get("city")
        api_key = "9d98929d09759871e6dc0a4d5abe2bd5"  
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
            }
        else:
            weather_data = {"error": "City not found 😓"}

    return render(request, "index.html", {"weather": weather_data})
