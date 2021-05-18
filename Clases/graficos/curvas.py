import matplotlib.pyplot as plt
tiempo = [0,1,2,3,4,5]
sensor = [4,5,6,7,8,9]

plt.plot (tiempo,sensor,'*','r')
#3333333333333333#
plt.title('Gráfico SENSOR contra el TIEMPO')
plt.xlabel('Tiempo(s)')
plt.ylabel('Voltaje(mV)')
plt.savefig('sensor.png')
plt.show()

