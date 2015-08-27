# coding=utf8

import paho.mqtt.client as paho
import datetime
import json

def on_connect(mqttc, obj, rc):
 #   mqttc.subscribe("$SYS/#", 0)
    print("rc: "+str(rc))

def on_message(mqttc, obj, msg):
    d = datetime.datetime.now()
    msg_obj = json.loads(msg.payload)
    d0 = datetime.datetime.strptime(msg_obj["@timestamp"], "%Y-%m-%d %H:%M:%S.%f")
    print("%s %s %s %s[%s]" % (msg.topic, str(msg.qos), str(msg.payload), str(d), d-d0))

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

if __name__ == '__main__':
    import sys
    p = sys.argv
    mqttc = paho.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe

    mqttc.connect(p[1], 1883, 60)

    mqttc.subscribe("my/topic/string", 0)

    mqttc.loop_forever()
