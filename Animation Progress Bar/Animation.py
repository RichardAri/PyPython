import time,os,random

message = 'Charging'
puntos = 0
character = '.'
time_sleep = 0.3
range_charge = 20

while True:
    print(message + f'{character}'*puntos)
    if (puntos == range_charge):
        puntos = 0
    puntos +=1
    time.sleep(time_sleep)
    os.system('cls')


