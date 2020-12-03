#-*- coding: utf-8 -*-
import mysql.connector
from time import sleep
#from gtts import gTTS 
import random
import os
import numpy
def czytaj(nazwa):
	mytext = nazwa
	language = 'en'
	myobj = gTTS(text=mytext, lang=language, slow=False) 
	  
	try:
		myobj.save("welcome.wav") 
		os.system("start vlc --play-and-exit welcome.wav") 
	except:
		print("Nie Wyszło")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="tlumaczenia"
)
mycursor = mydb.cursor()
polecenie="SELECT * FROM podstawa WHERE dobre_odp<1 ORDER BY RAND() LIMIT 20"
mycursor.execute(polecenie)
myresult = mycursor.fetchall()

np = numpy.zeros(20, dtype= int)
#np[0]=7
for i in range(0,19):
	np[i]=myresult[i][3]
while True:
	liczba=random.randrange(0,19)
	while np[liczba]>3:
		liczba=random.randrange(0,19)
	

	dobra_odp=True
	print(myresult[liczba][2])

	odp=raw_input('')

	if odp==myresult[liczba][1]:
		print("dobrze")
		np[liczba]=np[liczba]+1
	else:
		
		if odp=='znam':
			mycursor.execute("DELETE FROM podstawa WHERE id = "+ str(myresult[liczba][0]))
			np[liczba]=10
			print(myresult[liczba][1])
		else:
			print("zle "+myresult[liczba][1])
			dobra_odp=False
			np[liczba]=0
			#czytaj(myresult[liczba][1])

	
	sleep(1)
	

	
	mycursor.execute("UPDATE podstawa SET dobre_odp = " + str(np[liczba]) + " WHERE id = "+ str(myresult[liczba][0]))
	mydb.commit()


	os.system('clear')
