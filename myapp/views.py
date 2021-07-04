from django.shortcuts import render
import json
import urllib.request
# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
            place api_key in place of appid ="your_api_key_here "  '''

        # source contain JSON data from API

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&appid=92a76ac085af5052951bc3c3e73705df').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "city":city,
            'description' : str(list_of_data['weather'][0]['description']),
            'weather_icon' : str(list_of_data['weather'][0]['icon']),
            "country_code": str(list_of_data['sys']['country']),
            "sunrise": str(list_of_data['sys']['sunrise']),
            "sunset": str(list_of_data['sys']['sunset']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
            + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "visibility":str(list_of_data['visibility']),
        }
        print(data)
    else:
        data = {}
    return render(request, "index.html", data)
