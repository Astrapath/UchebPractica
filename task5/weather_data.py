import requests, json

def get_weather_data(city_name):
    api = 'aef454789ee3d0bad82fee47b0613904'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}&units=metric&lang=ru"
    response = requests.get(url).text
    data = json.loads(response)

    if len(data) == 2 and data["cod"] == '404':
        return 'Город введен неправильно бро'
    else:
        return (f'Название города: {data["name"]}\n '
                f'Температура: {data["main"]["temp"]}\n '
                f'описание погоды: {data["weather"][0]["description"]}')