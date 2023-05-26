import requests
import pandas as pd

#cidade jaguarão
lat = -32.5602
lon = -53.381

#periodo de avaliação
inicio = '2023-02-20'
final = '2023-03-20'

url = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,windspeed_10m,winddirection_10m&timezone=auto&start_date={}&end_date={}'.format(lat, lon, inicio, final)

data = requests.get(url).json()

time = data['hourly']['time']
temp = data['hourly']['temperature_2m']
umidity = data['hourly']['relativehumidity_2m']
ponto = data['hourly']['dewpoint_2m']
vento_dir = data['hourly']['winddirection_10m']
vento = data['hourly']['windspeed_10m']

dados = pd.DataFrame({'time': time,'temperatura':temp, 'humidade':umidity, 'ponto de orvalho': ponto, 'direção do vento':vento_dir, 'velocidade do vento': vento})

dados.to_csv('dados.csv')
#print(data)
