#-*- coding: utf-8 -*-
import keyboard  # using module keyboard
import mysql.connector
import random
import os
from time import sleep
#from gtts import gTTS 

#def czytaj(nazwa):
	#mowa= gTTS(text="Say somethink", lang="en")
	#mowa.save("slowo.mp3")
	#os.system("mpg321 welcome.mp3") 
#	mytext = nazwa
  
	# Language in which you want to convert 
#	language = 'en'
	  
	# Passing the text and language to the engine,  
	# here we have marked slow=False. Which tells  
	# the module that the converted audio should  
	# have a high speed 
#	myobj = gTTS(text=mytext, lang=language, slow=False) 
	  
	# Saving the converted audio in a mp3 file named 
	# welcome  
#	try:
#		myobj.save("welcome.wav") 
		  
		# Playing the converted file 

#		os.system("start vlc --play-and-exit welcome.wav") 
#	except:
#		print("Nie Wyszło")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="Slowka"
)
mycursor = mydb.cursor()


while True:
	#liczba=random.randrange(1,70)
	polecenie="SELECT * FROM wszystkie_dane WHERE dobre_odpowiedzi<4 ORDER BY RAND() LIMIT 1"
	mycursor.execute(polecenie)
	dobra_odp=True
	myresult = mycursor.fetchall()
	print(myresult[0][4])

	odp=raw_input('')

	if odp==myresult[0][1]:
		print("dobrze")
	else:
		tex='zle '+myresult[0][1]
		print(tex)
		dobra_odp=False

	print("Past tense")
	odp=raw_input('')
	if odp==myresult[0][2]:
		print("dobrze")
	else:
		if myresult[0][2].find(',',2)==-1:
			print("zle "+ myresult[0][2])
			dobra_odp=False
		else:
			if myresult[0][2].split(',')[0]==odp or myresult[0][2].split(',')[1]==odp:
				print("dobrze" + myresult[0][2])

	print("Past participle")
	odp=raw_input('')
	if odp==myresult[0][3]:
		print("dobrze")
	else:
		if myresult[0][3].find(',',2)==-1:
			print("zle "+ myresult[0][3])
			dobra_odp=False
		else:
			if myresult[0][3].split(',')[0]==odp or myresult[0][3].split(',')[1]==odp:
				print("dobrze" + myresult[0][3])

	liczba=myresult[0][-1]
	if dobra_odp:
		liczba+=1
		if liczba==4:
			print("Nauczone")
	else:
		liczba=0
	#czytaj(myresult[0][1]+", "+myresult[0][2]+", "+myresult[0][3])

	sleep(1)
	

	
	mycursor.execute("UPDATE wszystkie_dane SET dobre_odpowiedzi = " + str(liczba) + " WHERE id = "+ str(myresult[0][0]))
	mydb.commit()


	os.system('clear')
