

![WhatsApp Image 2025-03-24 at 17 17 59_8d7702c2](https://github.com/user-attachments/assets/d1dc4f4e-3004-4d81-a08f-7be0a287f63b)


# PYMQTT LOGGER DEL CLIMA (ESP32)



## Introducción
El **PYMQTT LOGGER DEL CLIMA (ESP32)** es un sistema basado en el protocolo MQTT para la transmisión de datos climáticos capturados por un sensor DHT22 conectado a un ESP32. Este proyecto permite la monitorización en tiempo real de temperatura y humedad a través de un broker MQTT. 

### Beneficios de usar MQTT como protocolo de comunicación
MQTT es un protocolo ligero y eficiente para la transmisión de datos en redes IoT. Algunas de sus ventajas incluyen:
- **Bajo consumo de energía y ancho de banda**, ideal para dispositivos embebidos.
- **Escalabilidad**, permitiendo conectar múltiples sensores y clientes de forma simultánea.
- **Fiabilidad**, ya que permite mecanismos de reintento y confirmación de entrega de mensajes.
- **Interoperabilidad**, facilitando la integración con diversas plataformas de análisis de datos y visualización.

 ### Uso de IoT en sensores climáticos y la importancia de una comunicación liviana

En entornos de Internet de las Cosas (IoT), sensores como el DHT22 juegan un papel fundamental en la recolección y transmisión de datos ambientales. Estos dispositivos deben operar con un mínimo consumo de energía y ancho de banda, lo que hace esencial el uso de protocolos optimizados como MQTT.

Eficiencia: Los sensores IoT suelen operar en entornos con conectividad limitada, por lo que un protocolo liviano minimiza la carga de transmisión.

Baja latencia: La comunicación en tiempo real es crucial para sistemas de monitoreo, permitiendo respuestas rápidas a cambios en las condiciones ambientales.

Integración con múltiples plataformas: MQTT permite que diferentes dispositivos y sistemas interactúen de manera eficiente sin necesidad de complejos protocolos de comunicación.

### ¿Por qué usar MicroPython?
MicroPython es una implementación eficiente del lenguaje Python diseñada para microcontroladores como el ESP32. Su uso facilita:
- **Desarrollo rápido**, ya que permite escribir y probar código sin necesidad de compilaciones largas.
- **Compatibilidad con Python**, facilitando la transición desde el desarrollo en computadoras a sistemas embebidos.
- **Acceso a librerías específicas**, como `network` para WiFi y `umqtt.simple` para la comunicación MQTT.

### Aplicaciones futuras
Aprender a diseñar sistemas con sensores interconectados como este permite desarrollar aplicaciones avanzadas, tales como:
- Sistemas de monitoreo ambiental en agricultura de precisión.
- Control de condiciones climáticas en entornos industriales.
- Automatización de viviendas inteligentes para optimización energética.

---

## Instalación y Configuración

### Requisitos previos
Para ejecutar este código correctamente, necesitarás:
- **Un ESP32** con conexión WiFi en wokwi.
- **Un sensor DHT22** conectado a un pin digital del ESP32.
- **MicroPython** instalado en el ESP32.
- **Broker MQTT disponible**, como HiveMQ.
- **Cliente MQTT** para visualizar los datos, como HiveMQ WebSocket Client.

### Configuración del ESP32
#### 1. Instalar MicroPython en ESP32
Si aún no tienes MicroPython en tu ESP32, sigue esta guía oficial: [MicroPython en ESP32](https://docs.wokwi.com/guides/micropython)

#### 2. Conectar el ESP32 a la red WiFi
El ESP32 usa la librería `network` para conectarse a una red WiFi. Consulta la documentación oficial aquí: [Conectar ESP32 a WiFi](https://docs.wokwi.com/guides/esp32-wifi#connecting-to-the-wifi)

1. **Editar credenciales WiFi** en el código para que coincidan con las de wokwi.
2. **definir el bloque de  el código** al ESP32 utilizando el editor de wokwi.
3. **Ejecutar el código** y verificar que se conecta a la red.

#### 3. Configurar el Cliente MQTT
Uso de la librería umqtt.simple

La librería umqtt.simple permite una implementación minimalista del protocolo MQTT en MicroPython. Se usa para establecer la conexión y manejar la mensajería entre el ESP32 y el broker MQTT.

Conectar al broker:

client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()

Publicar datos del sensor:

client.publish(MQTT_TOPIC, mensaje)





---

## Uso del Sistema

1. **Conectar al Broker MQTT**
   - Abre el cliente web MQTT: [HiveMQ WebSocket Client](http://www.hivemq.com/demos/websocket-client/).
   - Haz clic en "Connect" (No es necesario configurar un broker o Client ID).
   - Si la conexión falla, intenta nuevamente.

2. **Suscribirse al tópico del sensor**
   - En la sección "Subscriptions", haz clic en "Add New Topic Subscription".
   - Ingresa el siguiente tópico: `sensor-clima-prueba`.
   - Haz clic en "Subscribe".

3. **Ver los datos en tiempo real**
   - Activa el sensor de temperatura/humedad en el simulador o en un entorno físico.
   - Modifica los valores de temperatura y humedad.
   - Observa cómo los datos se capturan y envían al broker MQTT.

4. **Conexión del ESP32 al MQTT Broker**
   - El ESP32 se conecta automáticamente al broker y comienza a capturar datos.
   - Si hay cambios en la temperatura o humedad, se publicarán en el tópico MQTT.

---

## Solución de Problemas
- **No puedo conectar el ESP32 a WiFi**:
  - Asegúrate de que la red WiFi está activa y las credenciales son correctas.
  - Consulta la guía: [Conectar ESP32 a WiFi](https://docs.wokwi.com/guides/esp32-wifi#connecting-to-the-wifi).
- **No veo datos en el cliente MQTT**:
  - Verifica la conexión del ESP32 al broker MQTT.
  - Asegúrate de que el sensor DHT22 está correctamente conectado.
- **El cliente MQTT no se conecta**:
  - Si usas HiveMQ WebSocket Client, intenta reconectar varias veces al broker gratuito en https://www.hivemq.com/demos/websocket-client/.
  - Intenta alternar entre el puerto 8884 y 8883
  - Verifica que el nombre del topic sea el miso que esta en el parameter **MQTT_TOPIC**
  - Contactame para verificar el estado del servidor MQTT.


Para obtener un ejemplo en funcionamiento por favor seguir este link
https://wokwi.com/projects/425139012393254913
---

## Créditos
Este código fue desarrollado para la monitorización de condiciones climáticas en proyectos IoT usando ESP32, MicroPython y MQTT y esta basado en gran parte sobre proyectos existentes del uso de MQTT en IoT


