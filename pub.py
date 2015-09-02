# coding=utf8

import paho.mqtt.client as paho
import datetime
import json

def on_connect(mqttc, obj, rc):
#    mqttc.subscribe("$SYS/#", 0)
    print("rc: "+str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_log(mqttc, obj, level, string):
    print(string)

if __name__ == '__main__':
    import sys
    p = sys.argv
    mqttc = paho.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.username_pw_set('utfj', password='utfj123')

    mqttc.connect(p[1], 1884, keepalive=60)
    d = datetime.datetime.now()
    msg = {
        "msg": "hello world",
        "@timestamp": str(d)}

    mqttc.publish("my/topic/string", json.dumps(msg), 1)
    print(str(d))

