import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#Cargar Datos


#Modelo de la red
model = tf.keras.models.Sequential([
      tf.keras.layers.Input((None,2,)),
      tf.keras.layers.Dense(30, activation='relu'),
      tf.keras.layers.Dense(60, activation='relu'),
      tf.keras.layers.Dense(1, activation='sigmoid')
])
#configuracion entrenamiento
model.compile(optimizer='adam',
      loss='binary_crossentropy',
      metrics=['accuracy'])

#entrenamiento
model.fit(x,y, verbose = 2, epochs=5)
model.evaluate(x-test,y_test)
