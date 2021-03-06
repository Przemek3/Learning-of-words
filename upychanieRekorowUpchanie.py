#-*- coding: utf-8 -*-
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="Slowka"
)

mycursor = mydb.cursor()

sql = "INSERT INTO wszystkie_dane (bezokolicznik, past_tense, past_participle, polski) VALUES (%s, %s, %s, %s)"
val = [
  	('awake','awoke','awoken','obudzić'),
	('beat','beat','beaten','bić'),
	('bite','bit','bitten','ugryźć'),
	('bleed','bled','bled','krwawić'),
	('blow','blew','blown','wiać, dmuchać'),
	('burn','burned, burnt','burned, burnt','palic, parzyc, płonąć'),
	('dig','dug','dug','kopać (np. w ziemi)'),
	('feed','fed','fed','karmić, żywić'),
	('fight','fought','fought','walczyć, bić się'),
	('forget','forgot','forgotten','zapominać'),
	('forgive','forgave','forgiven','wybaczać'),
	('freeze','froze','frozen','zamarzać'),
	('hang','hung','hung','zawieszać (coś, np. obraz)'),
	('hide','hid','hidden','chować, ukrywać'),
	('let','let','let','pozwalać'),
	('lie (recline)','lay','lain','leżeć, kłaść się'),
	('light','lighted, lit','lighted, lit','zapalać, rozpalać, oświetlać'),
	('quit','quit','quit','rzucać, opuszczać'),
	('rise','rose','risen','podnosić się, wzrastać, wschodzić (o słońcu)'),
	('shake','shook','shaken','trząść, potrząsać'),
	('shine','shone','shone','świecić, błyszczeć'),
	('shoot','shot','shot','strzelać'),
	('sink','sank','sunk','tonąć (o statku), zapadać się'),
	('stick','stuck','stuck','wbijać, wtykać, przyklejać, wystawić'),
	('strike','struck','struck','uderzyć, wybijać'),
	('tear','tore','torn','drzeć, rozdzierać'),

]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
