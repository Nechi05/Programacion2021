import pandas as pd
import matplotlib.pyplot as plt

ppgdatos = pd.read_csv('ppg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print (ppgdatos.keys ())
muestras = list(ppgdatos['muestra'].values())
print (muestras)
voltaje = list(ppgdatos['valor'].values())
print (voltaje [-10])
plt.plot(muestras, voltaje)
plt.title('Fotopletismografía')
plt.xlabel('Tiempo (seg)')
plt.show()