#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import serial
import json
import time

ser = serial.Serial('/dev/ttyACM2', 115200, timeout = 1)

dataframe = pd.read_csv("DatosPruebaMQTT.csv",index_col = 0)
dataframe.head()

dataframe.describe(include = "all")
df = dataframe.dropna()


gps = df.GPS.tolist()
imu = df.IMU.tolist()
vel_llan = df.VelocidadLLantas.tolist()
por_llen = df.PorcentajeLlenado.tolist()
kil_pro = df.KilosProcesados.tolist()
vel_tri = df.VelocidadTrilladora.tolist()
niv_comb = df.NivelCombustible.tolist()
kilom = df.Kilometraje.tolist()
niv_ace = df.NivelAceite.tolist()
pres_llan = df.PresionLlantas.tolist()


for i in range(0,len(gps)):
    dict_obj = {}
    dict_obj["GPS"] = gps[i]
    dict_obj["IMU"] = imu[i]
    dict_obj["VelocidadLlantas"] = vel_llan[i]
    dict_obj["PorcentajeLlenado"] = por_llen[i]
    dict_obj["KilosProcesados"] = kil_pro[i]
    dict_obj["VelocidadTrilladora"] = vel_tri[i]
    dict_obj["NivelCombustible"] = niv_comb[i]
    dict_obj["Kilometraje"] = kilom[i]
    dict_obj["NivelAceite"] = niv_ace[i]
    dict_obj["PresionLlantas"] = pres_llan[i]
    
    packet = json.dumps(dict_obj)
    
    print(packet.encode())
    
    ser.write(packet.encode('utf-8'))
    time.sleep(3.2)
