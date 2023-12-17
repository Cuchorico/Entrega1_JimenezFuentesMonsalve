# CÓDIGOS:

# Gráfico 1: Fue escogido porque, pese a su generalidad (es todo el presupuesto anual del IND vs lo ejecutado de este) ofrece información relevante, como que solo 1/3 de los fondos se invirtió de 2015 hasta 2019. Esto introduce la pregunta de por qué motivos ocurrió esto y cuál es el destino de estos fondos inutilizados.

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <title>Gráfico Plotly en HTML</title>
    <style>
        body {
            background-color: #070608; /* Color de fondo de la página */
            color: #ffffff; /* Color del texto en la página */
        }
    </style>
</head>
<body>

<div id="grafico"></div>

<script>
    // Datos del gráfico
    var valoresAY = [156471,141443,149352,132558,136003,119637,152650,261005,528688];
    var valoresBY = [27248,28766,38861,28053,20926,116603,142177,258068,488494];
    var valoresX = [2015,2016,2017,2018,2019,2020,2021,2022,2023];

    // Crear trazas
    var trace1 = {
        x: valoresX,
        y: valoresAY,
        mode: 'lines+markers',
        name: 'Presupuesto IND (en miles de $US)',
        marker: {color: 'yellow'}
    };

    var trace2 = {
        x: valoresX,
        y: valoresBY,
        mode: 'lines+markers',
        name: 'Ejecución o gasto (en miles de $US y hasta sept. 2023)',
        marker: {color: 'blue'}
    };

    // Configurar diseño del gráfico sin especificar el color de fondo
    var layout = {
        title: 'Presupuesto IND vs Ejecución o gasto',
        xaxis: {title: 'Años'},
        yaxis: {title: 'Miles de $US'},
        paper_bgcolor: '#070608', // Color de fondo del área del gráfico
        plot_bgcolor: '#070608',  // Color de fondo del gráfico
        font: {color: '#ffffff'}  //Color del texto del gráfico
    };

    // Crear figura
    var data = [trace1, trace2];
    Plotly.newPlot('grafico', data, layout);
</script>

</body>
</html>



# Gráfico 2: este gráfico fue escogido porque explicita que el alza gigantesca en el presupuesto del IND desde el año 2020 no significó lo mismo para las partidas que van directo en beneficio de los deportistas (Fomento Deporte Convencional, ADO, COPACHI, etc.), por lo que existe una especie de constancia en el tiempo en el financiamiento de los deportistas, el cual ya era menor antes de 2020.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <title>Desglose de Ejecución Presupuestaria del IND</title>
</head>
<body style="background-color: #07608; color: #ffffff;">

<!-- Contenedor para el gráfico -->
<div id="plotly-chart" style="width: 80%; margin: 0 auto;"></div>

<script>
// Código de Python convertido a JavaScript
var xvals = [116122, 103135, 127324, 235571, 422532];
var yvals = [5021, 6148, 10339, 49978, 209213];
var zvals = [20771, 19392, 23126, 25765, 20668];

var N = 5;
var ind = [...Array(N).keys()];
var width = 0.12;

var trace1 = {
    x: ind,
    y: xvals,
    name: 'Gasto Total',
    type: 'bar',
    marker: {color: '#BA2A20'}
};

var trace2 = {
    x: ind.map(i => i + width),
    y: yvals,
    name: 'En Para y Panamericanos',
    type: 'bar',
    marker: {color: '#ABB900'}
};

var trace3 = {
    x: ind.map(i => i + width * 2),
    y: zvals,
    name: 'En Federaciones Deportivas',
    type: 'bar',
    marker: {color: '#004BAB'}
};

var layout = {
    title: 'Desglose de Ejecución Presupuestaria del IND',
    xaxis: { title: 'Año', tickvals: ind.map(i => i + width), ticktext: ["2019", "2020", "2021", "2022", "2023 (hasta sept.)"], tickfont: {color: '#ffffff'} },
    yaxis: { title: 'En millones de pesos (CLP)', titlefont: {color: '#ffffff'}, tickfont: {color: '#ffffff'} },
    template: 'plotly_dark',  // Usar un fondo oscuro
    barmode: 'group',
    plot_bgcolor: 'rgba(0, 0, 0, 0)',
    paper_bgcolor: 'rgba(0, 0, 0, 0)',
    font: {color: '#ffffff'}
};

var data = [trace1, trace2, trace3];

Plotly.newPlot('plotly-chart', data, layout);
</script>

</body>
</html>


# Gráfico 3: Escogido por representar y ejemplificar detalladamente y en términos prácticos el rendimiento de los primeros ocho países en los Juegos Panamericanos a través del desglose del tipo de medallas adquiridas y su consecuente posición en el tablero. Aporta el contraste entre el orden de los países que invierten más en sus deportistas de elite vs el orden de posicionamiento en el medallero, lo cual apoya el argumento de la historia que señala que poseer más fondos no se traduce instantáneamente en mejor rendimiento deportivo.

import numpy as np
import matplotlib.pyplot as plt


medidas=('Oro','Plata','Bronce')
y = ["Chile (8°)","Argentina (7°)","Colombia (6°)","Cuba (5°)",'Canadá (4°)','México (3°)','Brasil (2°)','EE.UU. (1°)']

verde_1 = np.array([12,17,29,30,46,52,66,124])
amarillo_1 = np.array([75,73,38,55,22,38,25,31])
rojo_1 = np.array([87,66,52,63,17,34,33,36])

plt.barh(y, verde_1, height=0.5, color='#A88900')
plt.barh(y, amarillo_1, left=verde_1, height=0.5, color='#868686')
plt.barh(y, rojo_1, left=verde_1 + amarillo_1, height=0.5, color='#5c3d00')

plt.title('Medallero desglosado Santiago 2023')
plt.xlabel('Medallas')
plt.ylabel('País (Top-8)')
plt.legend(labels=medidas)


for i, (v, a, r) in enumerate(zip(verde_1, amarillo_1, rojo_1)):
    ax.text(v / 2, i, str(v), ha='center', va='center', color='black')
    ax.text(v + a / 2, i, str(a), ha='center', va='center', color='black')
    ax.text(v + a + r / 2, i, str(r), ha='center', va='center', color='black')


ax.legend()

plt.show()
