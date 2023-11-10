# Documentación general sobre la Visualización Atómica individual

La selección de datos relativos a la variación anual del preupuesto del IND y de su gasto se realizó porque estaba a la mano (muy fácilmente encontrable en la web y en documentos poseídos con anterioridad), además de que no involucraba el volumen de información y la posterior prolongada graficación de la comparación del gasto a nivel internacional en deporte de elite, algo que decidimos dejar a Edward, que tendrá más tiempo para hacerlo.

Además, creemos que esta información graficada es muy relevante para contestar a las preguntas:

* ¿Cuánto invierte la institución encargada de fomentar el deporte profesional en los deportistas que nos representan en el extranjero?

* ¿Hace el IND un uso eficiente y justo de sus recursos? Esperamos ahondar en esta pregunta en el futuro, cuando obtengamos mayor información sobre bloqueos económicos que sufren distintas federaciones desde hace años, según denuncia el presidente de la Federación de Biathlón, Manuel Reyes. La pregunta ya fue enviada por Transparencia.

* ¿Tienen sustento empírico las declaraciones de nuestros deportistas, tan [viejas](https://www.latercera.com/el-deportivo/noticia/el-dificil-presente-del-alto-rendimiento-deportistas-nacionales-recurren-a-las-rifas-para-poder-representar-a-chile/T6AGQNNVVREZTFHKG7CZ3HSKCU/) como [actuales](https://radio.uchile.cl/2023/11/06/los-proximos-desafios-del-patinaje-artistico-ha-crecido-de-nivel-pero-falta-apoyo-economico-porque-tambien-somos-deportistas/), de que no reciben suficiente apoyo financiero?

La información se obtuvo de sitios web como el Portal de Transparencia, la Dirección de Presupuestos y la Biblioteca Nacional del Congreso, además del estudio y paper "Analysis of the public financial investment in elite sport in chile", hecho por académicos tanto de universidades chilenas como extranjeras, y publicado recientemente (en septiembre de 2023), por lo que lo encontramos adecuado. Agradecemos al profesor Aquiles Yáñez, 
Director del Centro de Investigación en Fisiología del Ejercicio de la Universidad Mayor, por proveernos de este documento recopilatorio que agilizó nuestro trabajo.

Ya obtenidos los datos y sabiendo como importar el dataset en Google Colab, faltaba obtener un código que pudiera graficarlos didácticamente. El escogido fue "matplotlib.pyplot", por su fácil uso y capacidad de presentar dos lineas en un gráfico, algo que fue dificil de hacer con otras funciones pero que era necesario para contar la historia de este trabajo (fondos vs gasto real del IND).