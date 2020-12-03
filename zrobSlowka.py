sciezka_pliku='C:\\Users\\Mały Araj\\Documents\\bazaDanych\\slowka\\'
import re
f= open(sciezka_pliku+"slowka.txt","r")
zapis=open(sciezka_pliku+"doSql2.txt","w")

def listToString(s):
	str1 = '(\''+s[0]+'\',\''+s[1]+'\'),\n'
	return str1

for x in f:
	if len(x)>1:
		zapis.write(listToString(re.split(r'\t+', x)))

zapis.close()
f.close()