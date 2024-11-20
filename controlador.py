import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


def cargar_datos(archivo):
	file_path = os.path.dirname(os.path.realpath(__file__)) + '\\datos\\'+archivo+'.csv'
	df = pd.read_csv(file_path)
	return df

def separar_datos(df, criterio):
	if criterio == 'agiles':
		df1 = df[df['¿Trabaja con un enfoque ágil de desarrollo de software?'] == 'Si']
		df2 = df[df['¿Trabaja con un enfoque ágil de desarrollo de software?'] == 'No']
	else:
		df1 = df[df['¿Su equipo realiza estimaciones del esfuerzo necesario para completar las historias de usuario (HU) ?'] == 'Sí']
		df2 = df[df['¿Su equipo realiza estimaciones del esfuerzo necesario para completar las historias de usuario (HU) ?'] == 'No']
	return df1,df2

def eliminar_columnas(df,columnas):
	df = df.drop(df.columns[columnas], axis=1)
	return df

def mostrar_columnas(datos):
	pass

def graficar(**kwargs):

	# Configurar el estilo de seaborn
	sns.set(style="whitegrid")
	i = 1
	for k,v in kwargs.items():
	# Contar las filas de cada DataFrame
		filas_df1 = len(v[0])
		filas_df2 = len(v[1])

		# Datos para el gráfico de torta
		tamaños = [filas_df1, filas_df2]
		etiquetas = [f'usan ({filas_df1})', f'no usan ({filas_df2})']
		colores = sns.color_palette("pastel")[0:2]  # Colores de pastel de seaborn

		# Crear el gráfico de torta
		plt.figure(i)
		plt.pie(tamaños, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=140)
		plt.title(k)
		plt.legend()
		i+=1
	plt.show()
