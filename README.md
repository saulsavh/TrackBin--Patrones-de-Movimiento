# TrackBin Patrones de movimiento :oncoming_automobile:
## Reporte final 

Se dio inicio al proyecto con la lectura del Paper de “ [TrajGAIL: Generating urban vehicle trajectories using generative adversarial imitation learning](https://www.sciencedirect.com/science/article/abs/pii/S0968090X21001121?via%3Dihub "Paper del repositorio")" ya que se usaría su proyecto como base para comenzar a analizar las rutas de vehículos [TrajGAIL](https://github.com/benchoi93/TrajGAIL "Repositorio").(https://github.com/benchoi93/TrajGAIL)

Como primer trabajo se solicitó el descargar el repositorio de GitHub e intentar ejecutarlo en la pc para evaluar cómo funcionaba, pero para ello salieron errores donde al final el Dr. Ramón Aranda se comunicó directamente al propietario del repositorio comentándole del error.

Durante el proceso de corrección en el repositorio se buscó la manera de crear nuestra propia data base recopilando datos con ayuda de una aplicación móvil. Para esta actividad se decidió el uso de “Outdooractive” por las facilidades y que los datos obtenidos nos los otorga en formato “gpx”. (la información correspondiente a la cuenta y a la presentación PowerPoint con el instructivo se puede encontrar en la carpeta “Outdooractive” dentro de la carpeta “Datos Servicio”)

Una vez el dueño del repositorio de TrajGAIL arreglo el error nos dimos cuenta que el programa estaba estructurado para funcionar específicamente en la zona del test por lo que se decidió iniciar el propio tomando como ejemplo alguna base de datos como ejemplo. Asi fue que se encontró una base de datos en la pagina de “https://www.kaggle.com”, de un proyecto llamado “ [PVS - Passive Vehicular Sensors Datasets](https://www.kaggle.com/jefmenegazzo/pvs-passive-vehicular-sensors-datasets "Database") ”. 

En esta base de datos es posible observar nueve diferentes grupos de muestras donde equivalen a tres **escenarios** diferentes con 3 **choferes**

|DataSet		|Vehicle		|Driver		|Scenario	|Distance|
|---------        |--------         |--------         |-------    |--------|
|PVS 1	|Volkswagen Saveiro	|Driver 1	      |Scenario 1	|13.81 km|
|PVS 2	|Volkswagen Saveiro	|Driver 1	      |Scenario 2	|11.62 km|
|PVS 3	|Volkswagen Saveiro	|Driver 1	      |Scenario 3	|10.72 km|
|PVS 4	|Fiat Bravo	            |Driver 2	      |Scenario 1	|13.81 km|
|PVS 5	|Fiat Bravo	      	|Driver 2	      |Scenario 2	|11.63 km|
|PVS 6	|Fiat Bravo	      	|Driver 2	      |Scenario 3	|10.73 km|
|PVS 7	|Fiat Palio	      	|Driver 3	      |Scenario 1	|13.78 km|
|PVS 8	|Fiat Palio	      	|Driver 3	      |Scenario 2	|11.63 km|
|PVS 9	|Fiat Palio	      	|Driver 3	      |Scenario 3	|10.74 km|

Para cada una de las muestra tenemos diferentes datasets, pero se destacan tres los cuales son: **dataset_gps, dataset_gps_mpu_left y dataset_labels**, del primero extrajimos la información de posición y velocidad, de “**dataset_gps_mpu_left**” y “**dataset_labels**” podemos notar que coinciden en la cantidad de datos y de **dataset_labels** podemos extraer información de la condición del camino.

Para ello se inició la programación en Python de un recurso que nos ayudaría en la filtración de los datasets quedándonos con la información importante, siendo que de **dataset_gps** extraeremos tanto la información de posición como la de velocidad y de los siguientes dos dataset se combinaron para poder manejar los valores de **dataset_labels** con las marcas de **timestamp** de **dataset_gps_mpu_left** para crear un nuevo dataset.

Una vez teniendo los dos datasets se procede a hacer la comparación con respecto a las marcas de **timestamp** para poder combinar ambos archivos teniendo en cuenta la gran diferencia de datos entre un dataset y otro, así generando un archivo nuevo con los valores necesarios llamado “**LabelGPS**”.

Teniendo los datos completos ahora fue necesario identificar por medio de los datos, donde es que existe un tope, con ello en mente se utilizo el valor de velocidad teniendo en mente la lógica donde un vehículo va a desacelerar antes de llegar al tope, con ello utilizamos la definición de la derivada para detectar un **cruce por 0** y así marcar un posible tope. Se programo una forma de dividir cada sección que detecte un supuesto tope, para ello se utilizo un filtro de savgol para estilizar un poco los datos para evitar cortes falsos gracias a algún pico instantáneo, después dentro de un ciclo for, se aplicó la definición de la derivada para detectar el cruce por cero y así en conjunto de un contador, ir realizando cortes al dataset de “**LabelGPS**”, generando y guardando con ella, una serie de datasets con la información de cada uno de los supuestos topes.

Se tiene en cuenta que los datos generados serán procesados por una red neuronal, asi que los dataset generados aun se necesitan redimensionar para poder utilizarlos, para ello en un nuevo programa se realizo una interpolación lineal con cada uno de los dataset generados definiéndolos todos a un numero exacto de valores y a su vez generando nuevos dataset ya redimensionados. Otro de los procesos que realiza el programa es generar una lista con los valores reales donde nos indica si es que existe un tope o no, en cada dataset.

Por ultimo se planteó el diseño de una **red neuronal binaria** en Python para el procesado de los datos que se generaron anteriormente.

## Instrucciones de uso
Para utilizar la serie de programas es necesario ingresar la información correspondiente al escenario y el conductor a la carpeta “Datos”, donde únicamente deben ir “dataset_gps_mpu_left.csv”, ”dataset_gps.csv” y “dataset_labels.csv”.
Esta información puede encontrarse en el link de la base de datos [PSV-Database](https://www.kaggle.com/jefmenegazzo/pvs-passive-vehicular-sensors-datasets)  o también puede encontrarse ordenado por escenario y conductor en la ruta “DatosServicio\Rutas\Data-TrackBin” del repositorio.

### Orden de programas

- Filtrado de datos
- Cortes de Grafica
- InterpoLinealint1
- Red Neuronal Binaria




### Librerias necesarias

- numpy
- pandas
- matplotlib
- scipy
- tensorflow

-Preferible usar python 3.8.8



## Rutas de archivos


Para el filtrado de archivos se requiere de tres archivos principales "**dataset_gps_mpu_left.csv**, **dataset_labels.csv**, **dataset_gps.csv**, de los cuales "***dataset_gps_mpu_left.csv***" solo es necesario para proporcionar las etiquetas "*Timestamp*" para el dataset **dataset_labels.csv** y así generar el nuevo dataset **LabelTimestamp.csv**, en caso de que se tenga un dataset con los datos necesarios("timestamp","no_speed_bump", "speed_bump_asphalt", "speed_bump_cobblestone"), use la línea #15 del código y comente la línea 6 a la 12.

Para el segundo caso, **el archivo se carga en la línea #15 con el nombre "LabelTimestamp.csv"**

````
15 dl = pd.read_csv("Datos\LabelTimestamp.csv")
````

En caso de que se tengan los 2 archivos por separado y sea necesario realizar el primero proceso, en la línea #6 y #7 se encuentran las rutas para abrir "**dataset_gps_mpu_left.csv**" y "**dataset_labels.csv**" respectivamente


````
6 dataset = pd.read_csv("Datos\dataset_gps_mpu_left.csv")
7 label = pd.read_csv("Datos\dataset_labels.csv")
````
Como resultado guardara un solo archivo con toda la información con la misma cantidad de datos que “**dataset_gps.csv**” llamado “**LabelGPS.csv**”


