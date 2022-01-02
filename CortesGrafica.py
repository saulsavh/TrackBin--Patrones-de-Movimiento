#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from scipy.signal import savgol_filter

datos = pd.read_csv("Resultados/LabelGPS.csv")
rango_min = 250
rango_max = 1200
x = datos['timestamp'][rango_min : rango_max]
y = datos['speed_meters_per_second'][rango_min : rango_max]
#y = datos['speed_meters_per_second'][250:1200]/datos['elapsed_time_seconds']
yfilter = savgol_filter( y, 25, 1)
yfinal = savgol_filter( yfilter, 25, 1)
xfinal = x.to_numpy()
#%%
#Mapeo de cortes 
n=0
detec_pos = True
graf_num = 0
resultado = pd.DataFrame(columns = ["timestamp", "latitude", "longitude", "speed_meters_per_second", "distance_meters",
                  "elapsed_time_seconds", "paved_road", "unpaved_road", "dirt_road", "cobblestone_road", "asphalt_road",
                  "no_speed_bump", "speed_bump_asphalt", "speed_bump_cobblestone", "good_road_left",
                  "regular_road_left", "bad_road_left", "good_road_right", "regular_road_right", "bad_road_right"])
mapa = pd.DataFrame(columns=['timestamp','speed_meters_per_second']) 
for i in yfinal:

      dy = yfinal[n+1]-yfinal[n]
      if dy > 0:
            detec_pos = True
      if dy < 0 and detec_pos == True:
            print("Grafica no. ", graf_num+1)
            print('el valor y es: ', yfinal[n])
            print('el valor x es: ', xfinal[n])
            dir_punto = {"timestamp" : xfinal[n], "speed_meters_per_second" : yfinal[n]}
            mapa = mapa.append(dir_punto, ignore_index= True)
            if n!= 0:
                  resultado.to_csv("Resultados\Cortes\Grafica_No_#" + str(graf_num) + ".csv")
            resultado = resultado[0:0]
            graf_num = graf_num + 1
            detec_pos = False
            
            
      val_gps = datos.loc[rango_min + n]
      dir_val = {"timestamp" : val_gps['timestamp'].tolist(), "latitude" : val_gps['latitude'].tolist(), "longitude" : val_gps['longitude'].tolist(),
                  "speed_meters_per_second" : val_gps['speed_meters_per_second'].tolist(), "distance_meters" : val_gps['distance_meters'].tolist(),
                  "elapsed_time_seconds": val_gps['elapsed_time_seconds'].tolist(), "paved_road" : val_gps['paved_road'].tolist(),
                  "unpaved_road": val_gps['unpaved_road'].tolist(), "dirt_road": val_gps['dirt_road'].tolist(),
                  "cobblestone_road": val_gps['cobblestone_road'].tolist(), "asphalt_road" : val_gps['asphalt_road'].tolist(),
                  "no_speed_bump" : val_gps['no_speed_bump'].tolist(), "speed_bump_asphalt" : val_gps['speed_bump_asphalt'].tolist(),
                  "speed_bump_cobblestone" : val_gps['speed_bump_cobblestone'].tolist(), "good_road_left" : val_gps['good_road_left'].tolist(),
                  "regular_road_left" : val_gps['regular_road_left'].tolist(), "bad_road_left" : val_gps['bad_road_left'].tolist(),
                  "good_road_right" : val_gps['good_road_right'].tolist(), "regular_road_right" : val_gps['regular_road_right'].tolist(),
                  "bad_road_right" : val_gps['bad_road_right'].tolist()}
            
      resultado = resultado.append(dir_val, ignore_index=True)

      
      n = n + 1
      if n == len(yfinal)-1:
            break

#Graficar esos cortes   
print('Numero de graficas es ', graf_num)    
# %%
#plt.plot(x,resultado["speed_meters_per_second"])
plt.plot(xfinal,yfilter)
plt.plot(xfinal,yfinal)
plt.plot(mapa['timestamp'], mapa['speed_meters_per_second'], "o")
plt.xlabel('timestamp')
plt.ylabel('mps')
plt.title('Grafica Aceleracion')

plt.show()
# %%
#Extraer cortes de archivo original
n=1
mapa.to_csv("Resultados\Cortes\mapeo.csv")
print('Fin del programa')
