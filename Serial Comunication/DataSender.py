#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import serial
import json
import time

ser = serial.Serial('/dev/cu.usbmodem531C0032331', 115200, timeout = 1)

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
    bigdic = {}
    bigdic["ID"]=str("1")
    bigdic["GPS"] = gps[i]
    bigdic["IMU"] = imu[i]
    bigdic["VelocidadLlantas"] = vel_llan[i]
    bigdic["PorcentajeLlenado"] = por_llen[i]
    bigdic["KilosProcesados"] = kil_pro[i]
    bigdic["VelocidadTrilladora"] = vel_tri[i]
    bigdic["NivelCombustible"] = niv_comb[i]
    bigdic["Kilometraje"] = kilom[i]
    bigdic["NivelAceite"] = niv_ace[i]
    bigdic["PresionLlantas"] = pres_llan[i]
    
    packet = json.dumps(bigdic)
    
    print(packet.encode())
    
    ser.write(packet.encode('utf-8'))
    time.sleep(3)

