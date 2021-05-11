import matplotlib.pyplot as plt

snacks = ['PapasFritas', 'Maní','Platanitos','Almendras','FrutosRojos']
precio = [1800,2400,1900,3000,2700]

plt.bar (snacks,precio,width=0.8, color='c')
plt.title('Precio de mis snacks favoritos')
plt.xlabel ('Nombres')
plt.ylabel ('Precio')
plt.savefig('SnacksBarras.png')
plt.show()