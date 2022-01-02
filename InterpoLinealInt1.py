#%%
import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt


puntos = 20
n = 1
df_topes = pd.DataFrame(columns={'Topes'})
tope = False

archivos = glob.glob("Resultados\Cortes\Grafica_No_#*.csv")
grafica= [0]*(len(archivos)+1)
x= [0]*(len(archivos)+1)
y= [0]*(len(archivos)+1)
# %%
for i in archivos:
      graf = pd.read_csv(i)
      if graf['speed_bump_asphalt'].sum() != 0:
            print('En Grafica',str(n),'tiene un tope en el asfalto')
            tope = True
      if graf['speed_bump_cobblestone'].sum() != 0:
            print('En Grafica',str(n),'tiene un tope en la tierra')  
            tope = True
      
      if tope == True:
            df_topes = df_topes.append({'Topes': int(1)}, ignore_index = True)
      else: 
            df_topes = df_topes.append({'Topes': int(0)}, ignore_index = True)
            
      
      x[n-1] = graf['timestamp']
      y[n-1]= graf['speed_meters_per_second']
      n = n + 1
      tope = False
df_topes.to_csv("Resultados\Cortes\Dato_RN\Resultados_para_RN.csv")
# %%
xtotal = [0]
ytotal = [0]
for i in range(0, n-1):
      print(i+1)
      xnew = np.linspace(x[i][0],x[i][len(x[i])-1], num = puntos)
      ynew = np.interp(xnew,x[i],y[i])
      df= pd.DataFrame({"X":xnew, "Y":ynew})
      df.to_csv("Resultados\Cortes\Dato_RN\Grafica_#"+ str(i+1)+".csv", index=False)
      plt.plot(x[i], y[i], ':')
      plt.plot(xnew, ynew)
      ##plt.show()

print('Fin del programa')
# %%
