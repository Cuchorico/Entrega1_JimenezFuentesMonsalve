# PROPUESTAS DE VISUALIZACIÓN ATÓMICA

1) ### Gráfico sobre la Ejecución Presupuestaria anual del Instituto Nacional de Deportes 

<image src="./Gráfico de Ejecución presupuestaria IND.png" alt="Ejecución Presupuestaria del IND desde 2015 hasta septiembre de 2023">

**Código:**

import matplotlib.pyplot as plt

valoresAY = [156471,141443,149352,132558,136003,148310,152650,261005,528688]
valoresBY = [27248,28766,38861,28053,20926,116603,142177,258068,488494]
valoresX = [2015,2016,2017,2018,2019,2020,2021,2022,2023]
fig, ax = plt.subplots()
plt.plot(valoresX, valoresAY, "o-y" )
plt.plot(valoresX, valoresBY, "o-r" )
plt.legend(["Presupuesto IND (en miles de $US)","Ejecución o gasto (en miles de $US y hasta sept. 2023)"])
plt.show()

2) ### Gráfico sobre la Ejecución Presupuestaria anual del Instituto Nacional de Deportes desglosada por sector de gasto


**Código:**


3) ### Gráfico de inversión anual en deportismo de alto rendimiento de primeros 8 lugares de Santiago 2023

<image src="./Grafico Edward .png" alt="Inversión anual en deportismo de alto rendimiento de primeros 8 lugares de Santiago 2023">

**Código:**


4) ### Gráfico del total de preseas obtenidas por los primeros 8 lugares en Santiago 2023 y comparado su rendimiento con el de Lima 2019

<image src="./Gráfico Jorge.png" alt="Total de preseas obtenidas por los primeros 8 lugares en Santiago 2023 comparado su rendimiento con Lima 2019">

**Código:**

etiquetas = ["EEUU", "Brasil", "México", "Canadá", "Cuba", "Colombia", "Argentina", "Chile"]
valores = [293, 169, 138, 152, 100, 82, 101, 50]
valores2 = [286, 205, 142, 164, 69, 101, 75, 79]

fig, ax = plt.subplots()
ax.bar(co - an/2, valores, an, label="Lima 2019")
ax.bar(co + an/2, valores2, an, label="Santiago 2023")

co = np.arange(len(valores))
an = 0.30

ax.set_title('Medalleros Panamericanos 2019 y 2023')
ax.set_ylabel('Medallas')
ax.set_xticks(co)
ax.set_xticklabels(etiquetas)
plt.legend()
