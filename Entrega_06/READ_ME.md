# INFORMACIÓN GENERAL

* **Link al sitio:** https://cuchorico.github.io/Entrega_JimenezFuentesMonsalve/

* **Resumen del proceso:**

La webstory utilizó diversos aspectos que ya teníamos planteados con antelación para ser incorporados en esta. En primer lugar, el fondo de color negro para añadir ese toque de misterio y de obscuridad que le queríamos dar a nuestro relato, más cercano a lo que es el periodismo investigativo, ya que revelamos información nueva que no es de extendido saber (bloqueos económicos a las federaciones deportivas, fondos cuya ejecución es menor y cuyo destino no es conocido, etc.). 

Para mantenernos con el enfoque de una tematica deportiva, eso sí, es que, para elementos estructurales, como barras de gráficos, el índice de navegación y hasta los mismos textos, se mantuvo la paleta de colores de los Juegos Pana y Parapanamericanos Santiago 2023, solo que en tonalidades un poco más apagadas. Tal como lo habíamos definido en nuestro Manual de Marca.

Además, durante la entrega previa se nos ocurrió la idea de que los elementos de nuestra historia (gráficos, textos, imágenes) se revelaran progresivamente con el scrolling de la página para otorgar suspenso al relato. Esto, finalmente, se implementó en la webstory, pero no a cada elemento, para así ahorrar tiempo de trabajo y tampoco generar una sensación de hastío en el lector interactivo. Pero no fue fácil, ya que el código de Javascript que originalmente teníamos para ejecutar la función no dio resultados, por lo que tuvimos que pedir ayuda. La profesora Francisca nos compartió una versión adaptada y modificada del código que se ejecutó en primera instancia, pero, a medida que adheríamos este código a más elementos, solamente mostraba la animación en el último objeto, por lo que utilizamos un nuevo código que nos proveyó la profesora Katherine (muchas gracias) y que es el que finalmente está en nuestro archivo Script funcionando perfectamente.

Por su parte está la idea del índice interactivo, la cual sufrió ciertas modificaciones a cómo se envisionó en un inicio al solicitársenos integrar los testimonios de entrevistados en el relato de nuestra historia y no aparte, por lo que el índice, al ser cliqueado en el trabajo ya finalizado, conecta con el incio, el desarrollo y la conclusión de nuestra historia.

Entre otros aspectos que cambiaron está la evolución de dos gráficos, hechos originalmente en Matplotlib, a formato Plotly, para que fueran interactivos y tuvieran un fondo que se mezclara con el del sitio web. Luego se transformaron ambos a lenguaje HTML para poder ser incrustados en nuestra página. Además, para avanzar más rápidamente con la producción de otras cuatro gráficas se optó por la herramienta Flourish, más sencilla de manipular y ejecutar.

Desde el aspecto más humano y menos técnico, se utilizaron para las entrevistas los testimonios del académico de Fisiología Aquíles Yáñez (para conocer las consecuencias de la falta de financiamiento o el mal uso de los recursos en los deportistas nacionales y la población general), el presidente de la Federación de Biathlón Manuel Reyes (para respaldar la idea de que hay federaciones con bloqueos económicos hace años por parte del IND), y el periodista y vocero de la dirección del Instituto Nacional de Deportes Carlos Marchant (para dar respuesta al destino de los fondos no utilizados y un adelanto a futuros planes del IND), ante una agenda copada e indisponibilidad del director nacional del organismo público, Israel Castro. Tampoco contamos con el testimonio de Nicole Sáez, académica USACH y ex subsecretaria del Deporte, quien además es conocedora de la problemática del financiamiento de los deportistas de elite en Chile y las políticas publicas relativas tanto actuales como aquellas necesarias para resolver la cuestión en base a la experiencia comparada internacional, la cual conoce, pero ella no contestó nuestros correos.

Finalmente, se descartó utilizar el testimonio de más deportistas sobre una posible falta de financiamiento, ya que consideramos que quedaba bastante claro el reclamo de los atletas con el collage de fotos de titulares que así lo registran, presente en la introducción del relato.

* **Tabla de autoría de Webstory:**

| Elemento | Edward Jimenez | Jorge Fuentes | Agustín Monsalve |
|:---------|:-------------|:-------------|:-------------|
| Gráficos en Flourish        |    Edward          |     Jorge         |              |
| Gráficos Plotly en HTML        |     Edward         |              |   Agustín         |
|Gráfico Matplotlib de Medallero Santiago 2023| | |Agustín |
| Índice interactivo       |              |    Jorge          |              |
| Fade in de elementos |  |  | Agustín (con ayuda de profe Katherine) |
|Crónicas del relato | | |Agustín |
|Color, tamaño, justificación y posicionamiento de textos| | |Agustín |
|Hípervínculos| | |Agustín |
|Entrevistas a Aquíles Yáñez, Manuel Reyes y Carlos Marchant| | |Agustín|