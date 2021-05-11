import pandas as pd
import matplotlib.pyplot as plt

datosPpg = pd.read_csv ('ppgExamen.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print (datosPpg.keys())

muestras = list(datosPpg['muestra'].values())
print (muestras)
voltaje = list(datosPpg['valor'].values())
print (voltaje)

plt.plot(muestras, voltaje)
plt.title('Fotopletismografía Paciente Urgencias')
plt.xlabel('Tiempo (seg)')
plt.show()