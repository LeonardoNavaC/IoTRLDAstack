#!/usr/bin/env python
# coding: utf-8

import serial
import json
import time
import paho.mqtt.client as mqttClient
from datetime import datetime


ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)


def on_connect(client, userdata, flags, rc):
    """Función que establece la conexión"""
    if rc==0:
        print("Conectado al broker")
        global Connected
        Connected = True
    else:
        print("Falla en la conexión")

tag1 = "/CADI/I40/GPS"  #tag, etiqueta o tópico
tag2 = "/CADI/I40/IMU"  #tag, etiqueta o tópico
tag3 = "/CADI/I40/VelocidadLlantas"  #tag, etiqueta o tópico
tag4 = "/CADI/I40/PorcentajeLlenado"  #tag, etiqueta o tópico
tag5 = "/CADI/I40/KilosProcesados"  #tag, etiqueta o tópico
tag6 = "/CADI/I40/VelocidadTrilladora"  #tag, etiqueta o tópico
tag7 = "/CADI/I40/NivelCombustible"  #tag, etiqueta o tópico
tag8 = "/CADI/I40/Kilometraje"  #tag, etiqueta o tópico
tag9 = "/CADI/I40/NivelAceite"  #tag, etiqueta o tópico
tag10 = "/CADI/I40/PresionLlantas"  #tag, etiqueta o tópico

Connected = False  #variable para verificar el estado de la conexión
broker_address="192.168.0.102" #dirección del Broker
port= 1883 #puerto por defecto de MQTT
client = mqttClient.Client("identificador") #instanciación
client.on_connect = on_connect #agregando la función
client.connect(broker_address, port)
client.loop_start() #inicia la instancia

while True:
    try:
        time.sleep(0.1)
        packet = ser.readline().decode('ascii')
        if packet:
        
            parse_packet = packet.split('}')[0]+'}'
            if parse_packet.find('"ID": "1"')!=-1:
            
                try:
                    ##print(parse_packet)
                    dict_obj = json.loads(parse_packet)
            
                    if dict_obj['ID']=="1":
                    
                        try:
                            float(dict_obj['GPS'])
                            float(dict_obj['IMU'])
                            float(dict_obj['VelocidadLlantas'])
                            float(dict_obj['PorcentajeLlenado'])
                            float(dict_obj['KilosProcesados'])
                            float(dict_obj['VelocidadTrilladora'])
                            float(dict_obj['NivelCombustible'])
                            float(dict_obj['Kilometraje'])
                            float(dict_obj['NivelAceite'])
                            float(dict_obj['PresionLlantas'])
                        
                            val1=str(dict_obj['GPS']) #json.dumps("GPS: "+str(i))
                            val2=str(dict_obj['IMU']) #json.dumps("IMU: "+str(j))
                            val3=str(dict_obj['VelocidadLlantas']) #json.dumps("VelocidadLlanta: "+str(k))
                            val4=str(dict_obj['PorcentajeLlenado']) #json.dumps("PorcentajeLlenado: "+str(l))
                            val5=str(dict_obj['KilosProcesados']) #json.dumps("KilosProcesados: "+str(m))
                            val6=str(dict_obj['VelocidadTrilladora']) #json.dumps("VelocidadTrilladora: "+str(n))
                            val7=str(dict_obj['NivelCombustible']) #json.dumps("NivelCombustible: "+str(o))
                            val8=str(dict_obj['Kilometraje']) #json.dumps("Kilometraje: "+str(p))
                            val9=str(dict_obj['NivelAceite']) #json.dumps("NivelAceite: "+str(q))
                            val10=str(dict_obj['PresionLlantas']) #json.dumps("PresionLlantas: "+str(r))
                
                            print(tag1,val1,'\n',tag2,val2,'\n',tag3,val3,'\n',tag4,val4,'\n',tag5,val5,'\n',tag6,val6,'\n',tag7,val7,'\n',tag8,val8,'\n',tag9,val9,'\n',tag10,val10)
                            client.publish(tag1,val1,qos=2)
                            client.publish(tag2,val2,qos=2)
                            client.publish(tag3,val3,qos=2)
                            client.publish(tag4,val4,qos=2)
                            client.publish(tag5,val5,qos=2)
                            client.publish(tag6,val6,qos=2)
                            client.publish(tag7,val7,qos=2)
                            client.publish(tag8,val8,qos=2)
                            client.publish(tag9,val9,qos=2)
                            client.publish(tag10,val10,qos=2)
                            
                        except Exception as e:
                            print(e)
                
                    else:
                
                        pass
                
                except Exception as e:
                    print(e)
    except:
        
        pass
