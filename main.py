"""
PYMQTT LOGGER DEL CLIMA (ESP32)

para revisar los datos generados por los eventos del sensor:

1. vaya al sitio web  http://www.hivemq.com/demos/websocket-client/
2. Click  en "Connect" ( no es nescesario configurar un broker o un client id)
3. En caso de que el paso anterior falle, vuelva a intentar hasta establecer una conexión
4. Una vez conectado , en la Opcion  Subscriptions, haga click en   "Add New Topic Subscription"
5. en el campo de Topic , escriba "sensor-clima-leo" y haga click "Subscribe"

Ahora haga click en el sensor de temperatura/humedad DHT22 en el simulador y haga uso del los sliders
para cambiar los valores de la temperatura y humedad, tras esto us podrá ver como
se capturan los valores en el broker MTTQ y son enviados al servicio de mensajeria de MQTT

*En caso de no poderse conectar al broker MQTT contactarme por mensaje interno para encender la  del cloud cluster
"""
#Importando lop
import network
import time
from machine import Pin
import dht
import ujson
from umqtt.simple import MQTTClient #importando el cliente base de MQTT para la mensajeria de los eventos

# Parametros del servidor MQTT
MQTT_CLIENT_ID = "5f266c35683a484cbe49c51a20bedcfa.s1.eu.hivemq.cloud"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = "hivemq.webclient.1741662916727"
MQTT_PASSWORD  = ",?x&S7>N4Qn6PRH5mcrg"
MQTT_TOPIC     = "sensor-clima-leo"

sensor = dht.DHT22(Pin(15))

# Configuración de la red WiFi del ESP32

print("Conectando a WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Conexión establecida a la red!")

# Configuración de la conexión al broker MQTT

print("Conectando alservidor MTQQ... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()

print("Conexión establecida al broker MQTT!")

clima_prev = ""
while True:
  print("Capturando los datos climaticos... ", end="")
  sensor.measure() 
  message = ujson.dumps({
    "temperatura": sensor.temperature(),
    "humedad": sensor.humidity(),
  })
  if message != clima_prev:
    print("Datos actualizados!")
    print("Reportando los datos al MQTT topic {}: {}".format(MQTT_TOPIC, message))
    client.publish(MQTT_TOPIC, message)
    clima_prev = message
  else:
    print("No hay cambios")
  time.sleep(1)
