#!/usr/bin/#!/usr/bin/env python3

#Importar las librerías a usar
import re #porque tengo que sacar las regex
import csv #porque tengo que generar dos archivos csv
import operator #me sirve paara ordenar los diccionarios

#Iniciar los diccionarios
errors = {}
per_user = {}

#Definir el criterio de la búsqueda
regex = r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$"

#Abrir archivo de log
with open("syslog.log") as file:
    for line in file.readlines():
        match = re.search(regex, line)
    code, error_msg, user = match.group(1), match.group(2), match.group(3)

    #Crear lista de errores y frecuencia
    if error_msg not in errors.keys():
        errors[error_msg] = 1
    else:
        error[error_msg] += 1
    #Crear lista de usuarios y frecuencia
    if user not in per_user.keys():
        per_user[user] = {} #inicializo un diccionario con los valores de las keys "users"
        per_user[user]["INFO"] = 0 #Instancio la primera clave como INFO
        per_user[user]["ERROR"] = 0 #Instancio la segunda clave como ERROR
    if code == "INFO":
        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]["INFO"] = 0 #Si no está, que no lo sume
        else:
            per_user[user]["INFO"] += 1 #Si está, que lo sume
    elif code == "ERROR":
        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]["INFO"] = 0 #le asigno un valor 0 a la instancia INFO
        else:
            per_user[user]["ERROR"] += 1 #Le aumento un número en la cuenta

#En este punto, los dos diccionarios están creados
#Ordenar los diccionarios
errors_list = sorted(errors.items(), key=operator.itemgetter(1), reverse=True) #Ordena por valor descendente los items de errors
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0)) #Ordena por valor ascendente los keys de per_user

#Cierro el archivo
file.close()

#Añadir los cabeceros de cada lista
errors_list.insert(0,("Username",{"INFO":"INFO","ERROR":"ERROR"}))
per_user_list.insert(0,("Error","Count"))

#Crear el archivo de reporte de errores CSV
with open("error_message.csv",'w',newline='') as error_csv:
    for item in errors_list:
        error_csv.write(str(item[0])+','+str(item[1])+'\n')

#Crear el archivo de reporte de usuarios CSV
with open("user_statistics.csv",'w',newline='') as user_csv:
    for key, value in per_user_list:
        user_csv.write(str(key)+','+str(value["INFO"])+','+str(value["ERROR"])+'\n')
