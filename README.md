<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Predicción de Salinidad en La Guajira</title>
</head>
<body>
  <h1>Predicción de Salinidad en La Guajira</h1>

  <h2>Descripción breve</h2>
  <p>
    Este repositorio se basa en los datos abiertos de Colombia sobre hidrogeología y salinidad en La Guajira. 
    Se espera que pueda ayudar a nuestras orgullosas comunidades guajiras a planificar sus necesidades de agua. 
    El alcance de este proyecto es predecir la salinidad del agua subterránea en la región, utilizando el mapa hidrogeológico y los datos de salinidad.
  </p>
  <p>
    La Guajira es una región desértica en el norte de Colombia. El agua en la región es escasa y la salinidad es alta, 
    lo que dificulta que las comunidades tengan acceso a agua limpia. Gran parte del agua en la región proviene de pozos subterráneos 
    perforados por las comunidades o entidades públicas. Es fundamental tener una idea de la salinidad del agua subterránea antes de perforar un pozo.
  </p>
  <p>
    Este proyecto busca cumplir ese objetivo mediante un modelo de aprendizaje automático que toma coordenadas X, Y y estima la salinidad del agua 
    en tres categorías: <strong>"BAJA SALINIDAD"</strong>, <strong>"MEDIA SALINIDAD"</strong> y <strong>"ALTA SALINIDAD"</strong>. 
    Los datos provienen del gobierno colombiano y son de acceso público.
  </p>
  <p>
    Los datos pueden encontrarse en:
    <ul>
      <li><a href="https://www.datos.gov.co/dataset/Salinidad-Guajira/fwz7-px8j/about_data">Salinidad</a></li>
      <li><a href="https://datos-sgcolombiano.opendata.arcgis.com/maps/ecda31174a204641a96d57cb4b379d0a/about">Mapa hidrogeológico de La Guajira</a></li>
  </ul>
  </p>

  <h2>Sobre los modelos analíticos</h2>
  <p>
    Usaremos el mapa hidrogeológico como fuente de características para el modelo, y los datos de salinidad como variable objetivo. 
    El modelo será entrenado con los datos de salinidad y las características extraídas del mapa hidrogeológico. 
    Se evaluará con un conjunto de prueba de datos de salinidad que no fue usado en el entrenamiento. 
    El modelo podrá predecir la salinidad del agua subterránea en la región, dadas las coordenadas X, Y.
  </p>
  <p>
    Entrenaremos los siguientes modelos:
    <ul>
      <li>Máquinas de Vectores de Soporte (SVM)</li>
      <li>Árbol de Decisión</li>
      <li>Boosting</li>
      <li>Voting</li>
      <li>Bagging</li>
      <li>KNN</li>
      <li>Regresión Logística</li>
      <li>Red Neuronal</li>
    </ul>
  </p>

  <h2>Sobre el uso de la aplicación</h2>
  <p>
    La aplicación está dividida en cuatro subpáginas:
      <li><b>Readme:</b> Contiene la descripción del proyecto y el modo de uso de la aplicación</li>
      <li><b>Model:</b> En esta pestaña se puede acceder a los diferentes modelos entrenados</li>
      <li><b>Model Metrics:</b> Contiene la información de la evaluación de los modelos analíticos entrenados</li>
      <li><b>Data:</b> Se pueden acceder a los datos de entrenamiento y al perfilamiento de los datos. Contiene también el link al repo donde se encuentra el código de procesamiento de datos.</li>
  </p>
  <p>
    Para usar el modelo en la pestaña <b>Model</b> basta con seleccionar un punto en el mapa y aparecerán las coordenadas en un popup en el punto seleccionado. La categoría de la salinidad se mostrará en la parte baja del mapa.
    Es posible seleccionar el modelo a testear mediante el uso de la lista desplegable localizada en la parte superior de la pesta.
  </p>
</body>
</html>
