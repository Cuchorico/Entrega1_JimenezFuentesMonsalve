SCRIPTS

1) Gráfico sobre la Ejecución Presupuestaria anual del Instituto Nacional de Deportes 


import matplotlib.pyplot as plt
valoresAY = [156471,141443,149352,132558,136003,148310,152650,261005,528688]
valoresBY = [27248,28766,38861,28053,20926,116603,142177,258068,488494]
valoresX = [2015,2016,2017,2018,2019,2020,2021,2022,2023]
fig, ax = plt.subplots()
plt.plot(valoresX, valoresAY, "o-y" )
plt.plot(valoresX, valoresBY, "o-r" )
plt.legend(["Presupuesto IND (en miles de $US)","Ejecución o gasto (en miles de $US y hasta sept. 2023)"])
plt.show()


2) Gráfico sobre la Ejecución Presupuestaria anual del Instituto Nacional de Deportes desglosada por sector de gasto


import numpy as np
import matplotlib.pyplot as plt

N = 5
ind = np.arange(N)
width = 0.12

xvals = [116122,103135,127324,235571,422532]
bar1 = plt.bar(ind, xvals, width, color = '#BA2A20')

yvals = [5021,6148,10339,49978,209213]
bar2 = plt.bar(ind+width, yvals, width, color="#ABB900")

zvals = [18167,16594,20328,22721,17699]
bar3 = plt.bar(ind+width*2, zvals, width, color = '#004BAB')

plt.xlabel('Año')
plt.ylabel('En millones de pesos (CLP)')
plt.title('Desglose de Ejecución Presupuestaria del IND')

plt.xticks(ind+width,["2019","2020","2021","2022","2023 (hasta sept.)"])
plt.legend( (bar1, bar2, bar3), ("Gasto Total","En Para y Panamericanos","En Federaciones Deportivas"))
plt.show()


3) Gráfico de inversión anual en deportismo de alto rendimiento de primeros 8 lugares de Santiago 2023


valoresAY = [1047960, 574980, 1033160, 1195090] valoresBY = [52545, 45010, 67209, 72708] valoresCY = [150385, 142607, 145974, 113471] valoresDY = [214732, 228010, 223248, 272484] valoresEY = [93067, 110607, 273298, 497105] valoresFY = [13967, 16610, 18843, 22047] valoresGY = [22952, 12934, 24458, 24001] valoresHY = [13499, 14564, 16441, 312674] valoresX = [2019, 2020, 2021, 2022]

fig, ax = plt.subplots()

plt.plot(valoresX, valoresAY, "o-", label="EE.UU.", color="green") plt.plot(valoresX, valoresBY, "o-", label="Brasil", color="blue") plt.plot(valoresX, valoresCY, "o-", label="México", color="red") plt.plot(valoresX, valoresDY, "o-", label="Canadá", color="yellow") plt.plot(valoresX, valoresEY, "o-", label="Cuba", color="cyan") plt.plot(valoresX, valoresFY, "o-", label="Colombia", color="magenta") plt.plot(valoresX, valoresGY, "o-", label="Argentina", color="orange") plt.plot(valoresX, valoresHY, "o-", label="Chile", color="purple")

plt.xlabel("Año") plt.ylabel("Dinero") plt.title("Comparación de valores por país a lo largo de los años")

plt.legend()

ax.set_xticks(list(set(valoresX))) ax.yaxis.set_major_formatter('${x:,.0f}')

plt.show()


4) Gráfico del total de preseas obtenidas por los primeros 8 lugares en Santiago 2023 y comparando su rendimiento con el de Lima 2019


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


5) Gráfico del total acumulado de preseas obtenidas por los primeros 8 lugares en Santiago 2023 pero en los Juegos Olímpicos 
