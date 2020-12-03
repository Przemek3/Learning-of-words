import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="slowka"
)

mycursor = mydb.cursor()

sql = "INSERT INTO wszystkie_dane (bezokolicznik, past_tense, past_participle, polski) VALUES (%s, %s, %s, %s)"
val = [
  	('be (am/is/are)','was, were','been','być'),
	('become','became','become','stawać się, zostawać kimś/czymś'),
	('begin','began','begun','zaczynać'),
	('break','broke','broken','łamać, pękać, rozbić, tłuc'),
	('bring','brought','brought','przynosić, przyprowadzić'),
	('build','built','built','budować'),
	('buy','bought','bought','kupować'),
	('catch','caught','caught','łapać'),
	('choose','chose','chosen','wybierać'),
	('come','came','come','przyjść, przyjechać'),
	('cost','cost','cost','kosztować'),
	('cut','cut','cut','ciąć, kroić, skaleczyć'),
	('do','did','done','robić'),
	('draw','drew','drawn','rysować, pociągnąć, remisować'),
	('dream','dreamed, dreamt','dreamed, dreamt','śnić, marzyć'),
	('drink','drank','drunk','pić'),
	('drive','drove','driven','prowadzić, kierować się czymś'),
	('eat','ate','eaten','jeść'),
	('fall','fell','fallen','padać, upadać, spadać'),
	('feel','felt','felt','czuć'),
	('find','found','found','znaleźć'),
	('fly','flew','flown','latać'),
	('get','got','got','dostawać'),
	('give','gave','given','dawać'),
	('go','went','gone','iść'),
	('grow','grew','grown','rosnąć'),
	('have','had','had','mieć'),
	('hear','heard','heard','słyszeć'),
	('hit','hit','hit','uderzać'),
	('hold','held','held','trzymać, utrzymywać, posiadać'),
	('hurt','hurt','hurt','ranić, boleć'),
	('keep','kept','kept','trzymać'),
	('know','knew','known','znać, wiedzieć'),
	('learn','learnt, learned','learnt, learned','uczyć się'),
	('leave','left','left','opuszczać, wyjeżdżać, zostawiać'),
	('lend','lent','lent','pożyczać'),
	('lose','lost','lost','tracić, zgubić'),
	('make','made','made','robić, wykonywać'),
	('mean','meant','meant','znaczyć, oznaczać; mieć na myśli'),
	('meet','met','met','spotykać, poznać'),
	('pay','paid','paid','płacić'),
	('put','put','put','kłaść'),
	('read','read','read','czytać'),
	('ride','rode','ridden','jeździć'),
	('ring','rang','rung','dzwonić'),
	('run','ran','run','biec'),
	('say','said','said','mówić'),
	('see','saw','seen','widzieć'),
	('sell','sold','sold','sprzedawać'),
	('send','sent','sent','wysyłać, słać'),
	('show','showed','shown','pokazywać'),
	('shut','shut','shut','zamykać'),
	('sing','sang','sung','śpiewać'),
	('sit','sat','sat','siedzieć, siadać'),
	('sleep','slept','slept','spać'),
	('speak','spoke','spoken','mówić, rozmawiać'),
	('spend','spent','spent','spędzać, wydawać'),
	('stand','stood','stood','stać'),
	('steal','stole','stolen','kraść'),
	('swim','swam','swum','pływać'),
	('take','took','taken','brać'),
	('teach','taught','taught','uczyć'),
	('tell','told','told','powiedzieć'),
	('think','thought','thought','myśleć, sądzić, uważać'),
	('throw','threw','thrown','rzucać'),
	('wake','woke','woken','budzić'),
	('wear','wore','worn','nosić, zakładać'),
	('understand','understood','understood','rozumieć'),
	('win','won','won','wygrywać'),
	('write','wrote','written','pisać'),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
