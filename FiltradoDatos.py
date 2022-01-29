# %%
import pandas as pd
import numpy as np

# Acomodamos los datos de label para usarlo como lo necesitamos 1577218696.999 1577218796
dataset = pd.read_csv("Datos\dataset_gps_mpu_left.csv")
label = pd.read_csv("Datos\dataset_labels.csv")
# solo retiro la columna que necesito del primer dataset
dataset = dataset["timestamp"]
# ahora unire el dataset1 con el label
dl = pd.merge(dataset, label, right_index=True, left_index=True)
dl.to_csv("Resultados\LabelTimestamp.csv")

#en caso de tener dataset con el timestamp, usar esta linea de codigo
#dl = pd.read_csv("Datos\LabelTimestamp.csv")

# importo el data del gps
gps = pd.read_csv("Datos\dataset_gps.csv")
gps = gps[["timestamp", "latitude", "longitude", "speed_meters_per_second", "distance_meters", "elapsed_time_seconds"]]
#%%
resultado = pd.DataFrame(columns = ["timestamp", "latitude", "longitude", "speed_meters_per_second", "distance_meters",
                  "elapsed_time_seconds", "paved_road", "unpaved_road", "dirt_road", "cobblestone_road", "asphalt_road",
                  "no_speed_bump", "speed_bump_asphalt", "speed_bump_cobblestone", "good_road_left",
                  "regular_road_left", "bad_road_left", "good_road_right", "regular_road_right", "bad_road_right"])
counter = 0
dls = dl["timestamp"]

dls = dls.to_numpy()

for turno in gps['timestamp']:

      var = abs(dls - turno)
      # comprobar en un rango de 2seg
      
      if np.amin(var) <= 10:
            index = np.where(var == np.amin(var))
            index_gps = np.where(gps['timestamp'] == turno)
            val_index = dl.iloc[index]
            val_gps = gps.iloc[index_gps]
            #val_gps = gps.iloc[counter]
            dir_val = {"timestamp" : val_gps['timestamp'].tolist()[0], "latitude" : val_gps['latitude'].tolist()[0], "longitude" : val_gps['longitude'].tolist()[0],
                  "speed_meters_per_second" : val_gps['speed_meters_per_second'].tolist()[0], "distance_meters" : val_gps['distance_meters'].tolist()[0],
                  "elapsed_time_seconds": val_gps['elapsed_time_seconds'].tolist()[0], "paved_road" : val_index['paved_road'].tolist()[0],
                  "unpaved_road": val_index['unpaved_road'].tolist()[0], "dirt_road":val_index['dirt_road'].tolist()[0],
                  "cobblestone_road": val_index['cobblestone_road'].tolist()[0], "asphalt_road" : val_index['asphalt_road'].tolist()[0],
                  "no_speed_bump" : val_index['no_speed_bump'].tolist()[0], "speed_bump_asphalt" : val_index['speed_bump_asphalt'].tolist()[0],
                  "speed_bump_cobblestone" : val_index['speed_bump_cobblestone'].tolist()[0], "good_road_left" : val_index['good_road_left'].tolist()[0],
                  "regular_road_left" : val_index['regular_road_left'].tolist()[0], "bad_road_left" : val_index['bad_road_left'].tolist()[0],
                  "good_road_right" : val_index['good_road_right'].tolist()[0], "regular_road_right" : val_index['regular_road_right'].tolist()[0],
                  "bad_road_right" : val_index['bad_road_right'].tolist()[0]}
            
            resultado = resultado.append(dir_val, ignore_index=True)
            #counter = counter + 1
#%%     
resultado.to_csv("Resultados\LabelGPS.csv")     
print('Fin del Programa')

#print(resultado)


