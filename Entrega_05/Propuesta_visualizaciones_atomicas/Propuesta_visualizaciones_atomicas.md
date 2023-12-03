# PROPUESTAS DE VISUALIZACIÓN ATÓMICA

1) ### Gráfico sobre la Ejecución Presupuestaria anual del Instituto Nacional de Deportes (Agustín)

<image src="./Gráfico 1.png" alt="Ejecución Presupuestaria del IND desde 2015 hasta septiembre de 2023">

**Explicación:**
Este gráfico nos servirá para introducir la historia, ya que instaura una problemática: desde 2015 hasta 2019, el IND gastó menos de un tercio de los fondos disponibles ¿Dónde están el resto de los fondos ahora? ¿Se ejecutaron? Se preguntará el lector. Aunque, desde 2020 hasta 2023 esto cambió, porque el gráfico indica que la ejecución de fondos se comenzó a acercar al total disponible anualmente. Sin embargo, esto también plantea la pregunta de si, con el aumento del presupuesto y de la cantidad de fondos usados, también aumentó el dinero destinado a los deportistas y sus federaciones, lo que introduce la temática del siguiente gráfico.

**Variables:**

- **Presupuesto IND (miles de $US):** corresponde a los fondos totales otorgados al Instituto Nacional de Deportes cada año por la Ley de Presupuestos propuesta por el Poder Ejecutivo y aprobada en el Congreso. Esto expresado en dólares para hacer comparables los datos a los de otros países. Su fluctuación en la gráfica nos indicará que la inyección de fondos al IND aumentó fuerte y progresivamente desde 2020 hasta 2023, en preparación a los Juegos Panamericanos de Santiago 2023, para gastos operacionales y de infraestructura.

- **Ejecución o gasto (en miles de $US y hasta sept. de 2023):** los gastos efectivamente extraídos de los fondos totales del presupuesto anual. Con su fluctuación en la tabla queremos indicar que el gasto era mínimo antes del comienzo de la preparación para los Panamericanos Santiago 2023, que comenzó en 2020. Esto da una pista de por qué el reclamo de falta de apoyo económico de los deportistas ha rondado por mucho tiempo. Sin embargo, esta ejecución debe ser desglosada para saber cuanta va dirigida directamente a los atletas (federaciones), lo cual se abarca en el siguiente gráfico y obliga a avanzar en la narrativa.

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

**Bases de datos utilizadas:**

- https://acrobat.adobe.com/id/urn:aaid:sc:US:72301d83-7c8f-4ecf-94b7-d0bbda600132 (diapositiva 9)
- https://www.dipres.gob.cl/597/articles-199366_doc_pdf.pdf
- https://www.dipres.gob.cl/597/articles-215418_doc_pdf.pdf
- http://www.dipres.cl/597/articles-264000_doc_pdf.pdf
- https://transparencialobby.ind.cl/activa/presupuestoejecucion/2022/ejecucion/diciembre.pdf
- https://www.dipres.gob.cl/597/articles-323170_doc_pdf.pdf


2) ### Gráfico sobre la Ejecución Presupuestaria anual del Instituto Nacional de Deportes desglosada por sector de gasto (Agustín)

<image src="./Gráfico 2.png" alt="Ejecución Presupuestaria del IND desde 2015 hasta septiembre de 2023">

**Explicación:**

Este gráfico intenta visualizar qué tanto del gasto efectivamente ejercido del presupuesto total va a las Federaciones Deportivas. Lo que se puede concluir a partir de la fluctuación de las barras de las variables es que: 1) La correspondiente a los Gastos Totales del IND aumentó exponencialmente tras el año 2021; 2) Lo mismo ocurrió con la de los Juegos Para y Panamericanos, correspondiente a los gastos operacionales e infraestructurales ejercidos por el IND en Santiago 2023; 3) La única barra que se mantuvo constante y muy baja fue la de Federaciones Deportivas, dinero que, en teoría, debería ser el que va más directamente a los deportistas profesionales chilenos (infraestructura o equipos para entrenar, apoyo técnico y psicológico, etc.)

**Código:**

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

**Bases de datos utilizadas:**
- https://www.dipres.gob.cl/597/articles-323170_doc_pdf.pdf
- https://transparencialobby.ind.cl/activa/presupuestoejecucion/2022/ejecucion/diciembre.pdf
- http://www.dipres.cl/597/articles-264000_doc_pdf.pdf
- https://www.dipres.gob.cl/597/articles-215418_doc_pdf.pdf
- https://www.dipres.gob.cl/597/articles-199366_doc_pdf.pdf


3) ### Gráfico de inversión anual en deportismo de alto rendimiento de primeros 8 lugares de Santiago 2023

<image src="./Grafico Edward .png" alt="Inversión anual en deportismo de alto rendimiento de primeros 8 lugares de Santiago 2023">

**Explicación:** Este gráfico muestra el cálculo del presupuesto anual destinado a deportistas de alto rendimiento de los ocho primeros países en el medallero de los Juegos Panamericanos Santiago 2023. Las federaciones representadas en el gráfico son las de Estados Unidos, Brasil, México, Canadá, Cuba, Colombia, Argentina y Chile. Al analizar el gráfico, surgen diversas preguntas y respuestas. Una de ellas es el hecho de que la federación chilena fue la que menos presupuesto invirtió en sus deportistas de 2019 a 2021. Se observa un aumento significativo en 2022, pero esto tiene una razón: el presupuesto incluyó los fondos invertidos en la realización de los Juegos Panamericanos Santiago 2023, lo que explica el notable aumento de un año a otro. Como consecuencia, se realizará otro gráfico desglosando los montos distribuidos en 2023 para conocer la inversión real en deportes de alto rendimiento.

De manera similar, se concluye que Estados Unidos es, con diferencia considerable, el país que más presupuesto invierte en deportistas de alto rendimiento. Relacionándolo con otros gráficos que poseemos, donde se muestra que Estados Unidos históricamente es el principal ganador de medallas en los Juegos Panamericanos y también en los Juegos Olímpicos, llegamos a la conclusión de que su inversión monetaria se traduce en éxito deportivo.

Otra variable que revela el gráfico es que en 2020 todos los presupuestos de los países disminuyeron. Este hecho genera la siguiente pregunta: ¿La pandemia del COVID-19 fue la causa de la disminución de los presupuestos de las federaciones? Trataremos de responder a esta pregunta en las siguientes entregas de este trabajo.

**Código:** import matplotlib.pyplot as plt

valoresAY = [1047960, 574980, 1033160, 1195090]
valoresBY = [52545, 45010, 67209, 72708]
valoresCY = [150385, 142607, 145974, 113471]
valoresDY = [214732, 228010, 223248, 272484]
valoresEY = [93067, 110607, 273298, 497105]
valoresFY = [13967, 16610, 18843, 22047]
valoresGY = [22952, 12934, 24458, 24001]
valoresHY = [13499, 14564, 16441, 312674]
valoresX = [2019, 2020, 2021, 2022]

fig, ax = plt.subplots()

# Líneas mejoradas con etiquetas y colores
plt.plot(valoresX, valoresAY, "o-", label="EE.UU.", color="green")
plt.plot(valoresX, valoresBY, "o-", label="Brasil", color="blue")
plt.plot(valoresX, valoresCY, "o-", label="México", color="red")
plt.plot(valoresX, valoresDY, "o-", label="Canadá", color="yellow")
plt.plot(valoresX, valoresEY, "o-", label="Cuba", color="cyan")
plt.plot(valoresX, valoresFY, "o-", label="Colombia", color="magenta")
plt.plot(valoresX, valoresGY, "o-", label="Argentina", color="orange")
plt.plot(valoresX, valoresHY, "o-", label="Chile", color="purple")

# Etiquetas de los ejes y título
plt.xlabel("Año")
plt.ylabel("Dinero")
plt.title("Comparación de valores por país a lo largo de los años")

# Leyenda con colores correspondientes
plt.legend()

# Formato de los números en los ejes x e y y eliminación de duplicados en x
ax.set_xticks(list(set(valoresX)))
ax.yaxis.set_major_formatter('${x:,.0f}')

# Mostrar el gráfico
plt.show()

**Bases de datos utilizadas:** file:///Users/edwardandresjimenezriascos/Documents/GitHub/Entrega1_JimenezFuentesMonsalve/Edward_Monsalve_Fuentes/Entrega_04/Jimenez_Integrante_02_Edward_vis_02/Otros%20Documentos/2019-vol3-ds6-eng.pdf 
file:///Users/edwardandresjimenezriascos/Documents/GitHub/Entrega1_JimenezFuentesMonsalve/Edward_Monsalve_Fuentes/Entrega_04/Jimenez_Integrante_02_Edward_vis_02/Otros%20Documentos/2020-vol3-ds6-eng.pdf 
file:///Users/edwardandresjimenezriascos/Documents/GitHub/Entrega1_JimenezFuentesMonsalve/Edward_Monsalve_Fuentes/Entrega_04/Jimenez_Integrante_02_Edward_vis_02/Otros%20Documentos/2022-vol3-ds6-eng.pdf
file:///Users/edwardandresjimenezriascos/Documents/GitHub/Entrega1_JimenezFuentesMonsalve/Edward_Monsalve_Fuentes/Entrega_04/Jimenez_Integrante_02_Edward_vis_02/Otros%20Documentos/2023-24-q1-quarterly-financial-report-eng.pdf 
file:///Users/edwardandresjimenezriascos/Documents/GitHub/Entrega1_JimenezFuentesMonsalve/Edward_Monsalve_Fuentes/Entrega_04/Jimenez_Integrante_02_Edward_vis_02/Otros%20Documentos/Comite%CC%81%20olimpico%20USA%202019.pdf 
file:///Users/edwardandresjimenezriascos/Documents/GitHub/Entrega1_JimenezFuentesMonsalve/Edward_Monsalve_Fuentes/Entrega_04/Jimenez_Integrante_02_Edward_vis_02/Otros%20Documentos/P51-1-2021-3-s6-eng.pdf 







4) ### Gráfico del total de preseas obtenidas por los primeros 8 lugares en Santiago 2023 y comparando su rendimiento con el de Lima 2019

<image src="./Gráfico Jorge.png" alt="Total de preseas obtenidas por los primeros 8 lugares en Santiago 2023 comparado su rendimiento con Lima 2019">

**Explicación:**

Este gráfico compara las medallas obtenidas por los ocho primeros lugares de Santiago 2023 en los Juegos Panamericanos de este año con las obtenidas en Lima 2019. Sirve para comparar qué tanto han avanzado estos ocho países durante los últimos cuatro años, para así evidenciar que Chile se ha quedado estancado en el octavo lugar, a pesar de mejorar en sus medallas. Es la forma más objetiva de mostrar el rendimiento deportivo de cada país.

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
