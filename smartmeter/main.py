import smartmeter
import requests
import time
import paho.mqtt.client as mqtt
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# VARIABLE START
smartMeterDataUrl = 'http://192.168.222.40/meter'
mqttTopicRoot = 'smartmeter'
mqttHost = '127.0.0.1'
mqttPort = 1883
mqttUsername = 'smartmeter'
mqttPassword = 'smartMeter#Passw0rd1234'
influxdbToken = 'mySecureToken'
influxdbOrg = 'home'
influxdbUrl = 'http://127.0.0.1:8086'
influxdbBucket = 'smartmeter'
# VARIABLES END

# Init MQTT Client
mqttClient = mqtt.Client()
mqttClient.connect(mqttHost, mqttPort, 60)
mqttClient.username_pw_set(mqttUsername, mqttPassword)
mqttClient.loop_start()

# Init InfluxDB Client
influxdbWriteClient = influxdb_client.InfluxDBClient(url=influxdbUrl, token=influxdbToken, org=influxdbOrg)
influxdbWriteApi = influxdbWriteClient.write_api(write_options=SYNCHRONOUS)

while True:
    # Get meter result
    meterResult = requests.get(smartMeterDataUrl, timeout=5)
    # Parse meter result
    resultDict = smartmeter.parseDSMRMessage(meterResult)
    # Send results to influxdb
    for key,value in resultDict.items():
        point = (
            Point(key)
            .tag('unit', value['unit'])
            .field(key, value['value'])
        )
        influxdbWriteApi.write(bucket=influxdbBucket, org=influxdbOrg, record=point)
    # Publish data to mqtt server
    for key,value in resultDict.items():
        topic = "{}/{}".format(mqttTopicRoot, key)
        mqttClient.publish(topic, value['value'])
    time.sleep(10)
