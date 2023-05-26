import requests

#cidade jaguarão
lat = -32.5602
lon = -53.381

url = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&timezone=auto&current_weather=true'.format(lat, lon)

data = requests.get(url).json()

temp = data['current_weather']['temperature']
vento = data['current_weather']['windspeed']
vento_dir = data['current_weather']['winddirection']
temp_code = data['current_weather']['weathercode']
hora = data['current_weather']['time'][11:]

if temp_code == 0:
    print('Hora: {}, o tempo está limpo, temperatura de {}°C, ventos de {}km/h na direção {} '.format(hora, temp, vento, vento_dir))
elif temp_code == 1:
    print('Hora: {}, o tempo está nublado, temperatura de {}°C, ventos de {}km/h na direção {} '.format(hora, temp, vento, vento_dir))
elif temp_code == 6:
    print('Hora: {}, está chovendo, temperatura de {}°C, ventos de {}km/h na direção {} '.format(hora, temp, vento, vento_dir))
