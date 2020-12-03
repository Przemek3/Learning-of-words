sciezka_pliku='C:\\Users\\Mały Araj\\Documents\\bazaDanych\\slowka\\'
import re
f= open(sciezka_pliku+"pierwszy_bledny.txt","r")
zapis=open(sciezka_pliku+"prawie.txt","w")

def listToString(s):  
    
    # initialize an empty string 
    str1 = "("  
    first = True
    # traverse in the string
    for ele in s: 
    	if first==True:
    		first=False
    		if ele.strip()[0:4] == "play":
    			str1 += '\''+ele.strip()[4:]+'\''
    		else:
    			str1 += '\''+ele.strip()+'\''
    	else:
    		str1 += "," + '\''+ ele.strip() + '\''
    
    # return string   
    return str1[:-16]+"),\n" 

for x in f:
	if x.split(' ')[0]!= "wzory":
		#print(re.split(r'\t+', x))
		zapis.write(listToString(re.split(r'\t+', x)))


zapis.close()
f.close()