"""
Arbeidskrav 1
Py1010
Marie Kristine Grech (mk.brandrud@outlook.com)
Oppdatert 2026 09 24
"""
#Årlig totalkostnad av elbil versus besinbil

FOR1=5000 # [forsikring for elbilen]
a=8.38 # [trafikkavgift for elbilen - kr/dag]
t=365 # [tidsperiode for beregningen i dager]
D1=0.2 # [drivstoffbruk - kWh/km]
s=2.00 # [strømpris kr/kWh]
BOM1=0.1 # [bomavgift - kr/km]
l=10000 # [lengde - km]

#Kostnad Elbil
EL=FOR1+(a*t)+(D1*l*s)+(BOM1*l)

FOR2=7500 # [forsikring for bensinbilen]
D2=1 # [drivstoffbruk - kr/km]
BOM2=0.3 # [bomavgift - kr/km]

#Kostnad bensinbil
BE=FOR2+(a*t)+(D2*l)+(BOM2*l)

print("Årlige kostnadene ved elbil =", EL)
print("Årlige kostnadene ved bensinbil =", BE)