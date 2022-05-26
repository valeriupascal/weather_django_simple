from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

def index(request):

	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5d50dc94bbfe77b23b192a3986fb00b0'

	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()
	form = CityForm()


	cities = City.objects.all()
	weather_data = []

	for city in cities:
		r = requests.get(url.format(city)).json()

		city_weather = {
			'id': city.id,
			'city': city.name,
			'temperature': r['main']['temp'],
			'description': r['weather'][0]['description'],
			'icon': r['weather'][0]['icon'],
		}
		weather_data.append(city_weather)

	print(weather_data)


	context = {'weather_data': weather_data, 'form': form}

	return render(request, 'weather/weather.html', context)


class CityDelete(DeleteView):
	model = City
	success_url = '/'
	context_object_name = 'city'
