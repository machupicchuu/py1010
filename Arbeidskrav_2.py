# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:51:47 2026

Arbeidskrav 2
Marie Kristine Grech

@author: mariekbr
"""
from time import sleep
###Oppg1###
print ("Regn ut alder fra fødselsår ")
sleep(2)
#Be om input når brukeren er født
alder = int(input('Hvilket år er du født? ') )
#Definerer året i år
år=2026
#Regner ut alder
alder_i_år=år-alder

#Skriver ut alder i løpet av dette året
print ("I løpet av", år, "blir du", alder_i_år, "år gammel")

sleep(3)
###Oppg2###
print ("Utregning av antall pizzaer til en klassefest")
sleep(2)
import math

#ber om input antall elever
antall_elever = int(input("Skriv inn antall elever: " ))
#Definerer hvor mye pizza hver elev spiser
pizza_per_elev = 0.25

#Utregning av antall pizza til klassefest
#round() runder både og opp ned, til det som er nærmest
#fant en annen funksjon slik at man styrer at den runder opp - math.ceil
pizza=math.ceil(antall_elever*pizza_per_elev)

#Skriver ut hvor mye pizza som må handles inn til festen
print("Det må handles inn", pizza, "pizzaer til festen")

sleep(3)
###Oppg3###
print("program som regner om fra grader til radianer")
sleep(2)
import numpy as np

#ber om input gradtall
v_grad = float(input("Skriv inn gradtallet: " ))
#utregning
v_rad = float(v_grad*np.pi/180)

#skriver ut svaret i radianer
print("Dette tilsvarer", v_rad, "radianer, eller", v_rad/np.pi,"π (radianer)")

sleep(3)
###Oppg4###
print("Dictionary")
#a
#Opprett dictionary
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

#b
#Be bruke skrive et land det ønsker informasjon om
land = input("Skriv et land ")
print(data[land][0], "er hovedstaden i", land, "og det er", data[land][1], "mill. innbyggere i", data[land][0]) 

#c
#Legg til flere land i dictionaryen
#Be bruker om inputten som trengs      
land_ny = input("Skriv et land du ønsker å legge til dictionaryen ")
hovedstad_ny = input("Skriv hovedstaden til det nye landet ")
innbyggertall_ny = input("Skriv innbyggertallet i mill. for hovedstaden ")

print("Dataene legges til nå..... ") 
data[land_ny] = [hovedstad_ny, innbyggertall_ny]
#eksempel: data["Malta"] = ["Valetta", 0.005]

#Skriv ut dictionaryen inkludert den nye daten
print(data)  

sleep(3)
###Oppg5###
print("Areal og Omkrets av figur")
import math
#La bruker oppgi verdi for a og b
a=float(input("skriv verdien for a "))
b=float(input("skriv verdien for b "))

#definerer variabelen r for å gjøre regnestykket lettere
r=a/2
#utregning for arealet
A=(a*b/2)+(math.pi*r*r/2)
#utregning for ytre omkrets
O=(math.pi*r)+b+math.sqrt((b*b)+(a*a))

#skriver ut arealet og omkrets
print("Arealet av figuren er ", A)
print("Ytre omkrets av figuren er ", O)

sleep(3)
###Oppg6###
print("plot funksjon")
import numpy as np
import matplotlib.pyplot as plt

#Definer interval
x = np.linspace(-10, 10, 200)
#Definer funksjon
y = -(x*x) - 5

#plot
plt.figure
plt.plot(x,y)
 