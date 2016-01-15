'''
Author: Ramiro Aznar
Web: www.ramiroaznar.com
Language: Python
Date: January 15th 2016
Code: a Python program to geocode csv files using Geopy
Note: the printed statements are in Spanish and the files are based on bank offices. 
The instructions are first insert directory, and second insert csv file from the list in order to geocode
your address.
'''
#Import modules
from time import sleep
import os
import csv
import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim()

#Get directory and csv files
dir_path = raw_input('Introduce directorio: ')
listFiles = os.listdir(dir_path)
print "Lista de archivos:"
for f in listFiles:
        if f.endswith(".csv"):
                print f

#Introduce csv file
fname = raw_input('Introduce archivo csv: ')
fname_split = fname.split(".")
banco = fname_split[0]
f = open(fname, 'r')
listCajeros = f.readlines()

#Count number of lines
count = len(open(fname).readlines())
print "Número total de sucursales:"
print count

#Open a new file and write a header
banco_geo = banco + "_geo.csv"
fw = open(banco_geo, 'a')
writer = csv.writer(fw)
writer.writerow(("Banco", "Sucursal", "Direccion", "Ciudad", "Pais", "Latitud", "Longitud"))

#Start to geocode
print "---Geolocalizando...---"

try:
        for cajero in listCajeros:
                listValues = cajero.split(";")
                banco = str(listValues[0])
                sucursal = str(listValues[1])
                direccion = str(listValues[2])
                ciudad = str(listValues[3])
                pais = str(listValues[4])
                location = geolocator.geocode(direccion, timeout=None)
                latitude = location.latitude
                longitude = location.longitude
                count = count - 1
                print count
                print banco, sucursal, direccion, ciudad, pais, latitude, longitude
                writer.writerow((banco, sucursal, direccion, ciudad, pais, str(latitude), str(longitude)))
                sleep(1)
except:
        pass

print "---...Finalizado---"

f.close()
fw.close()
