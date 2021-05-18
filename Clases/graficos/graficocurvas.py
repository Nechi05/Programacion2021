import pandas as pd
import matplotlib.pyplot as plt
ecgDatas = pd.read_csv('ecg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print (ecgDatas.keys ())
muestras = list(ecgDatas['muestra'].values())
print (muestras)
voltaje = list(ecgDatas['valor'].values())
print (voltaje [-10])
plt.plot(muestras, voltaje)
plt.show()
open('/users/MirnaNaranjo/Desktop/map/data.csv')