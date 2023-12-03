# PROPUESTAS DE VISUALIZACIÓN ATÓMICA

1) ### Gráfico sobre la Ejecución Presupuestaria anual del Instituto Nacional de Deportes 

<image src="./Gráfico de Ejecución presupuestaria IND.png" alt="Ejecución Presupuestaria del IND desde 2015 hasta septiembre de 2023">

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


2) ### Gráfico sobre la Ejecución Presupuestaria anual del Instituto Nacional de Deportes desglosada por sector de gasto

<image src="./Gráfico 2.png" alt="Ejecución Presupuestaria del IND desde 2015 hasta septiembre de 2023">

**Explicación:**

**Código:**

**Bases de datos utilizadas:**


3) ### Gráfico de inversión anual en deportismo de alto rendimiento de primeros 8 lugares de Santiago 2023

<image src="./Grafico Edward .png" alt="Inversión anual en deportismo de alto rendimiento de primeros 8 lugares de Santiago 2023">

**Explicación:**	

**Código:**

**Bases de datos utilizadas:**


4) ### Gráfico del total de preseas obtenidas por los primeros 8 lugares en Santiago 2023 y comparando su rendimiento con el de Lima 2019

<image src="./Gráfico Jorge.png" alt="Total de preseas obtenidas por los primeros 8 lugares en Santiago 2023 comparado su rendimiento con Lima 2019">

**Explicación:**

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

**Bases de datos utilizadas:**
