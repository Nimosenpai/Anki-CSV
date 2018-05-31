import csv
import requests
import json
import io
import time
from bs4 import BeautifulSoup
from pprint import pprint
# Stupid script to read from the jisho api and the first entry into a csv
# May modify to add multiple entries which match the word, or
# all entries which contain the word in it

completestring = "" #Define Complete string
fileswords = io.open(r"targetfilepath.txt", mode="r", encoding="utf-8")
fileswrite = io.open("output.txt", mode="w", encoding="utf-8")
for line in fileswords:
    time.sleep(.400) #Don't wanna overload the API haha
    url = 'https://jisho.org/api/v1/search/words?keyword='+line
    response = requests.get(url)
    html =  response.content

    soup = BeautifulSoup(html)
    data = json.loads(html)
    print(len(data["data"]))
    #Check against values which return nothing (so it doesn't get oob crash
    if(len(data["data"])>0):
        #For all the stuff thats in the 
        for x in range(0, len(data["data"][0]["japanese"])):
            if(len(data["data"][0]["japanese"][x])>1):
                if (x==0):
                    
                    completestring +='"'+(data["data"][0]["japanese"][x]['word'])+'"'+","+'"'
                else:
                    completestring +="<br>"+(data["data"][0]["japanese"][x]['word'])+"</br>"
                completestring+="<br>"+(data["data"][0]["japanese"][x]['reading'])+"</br>"
        print("END OF LINE \n")
        for y in range(0, len(data["data"][0]["senses"])):
            completestring+="<br>"
            for p in range(0, len(data["data"][0]["senses"][y]["parts_of_speech"])):
                completestring+=(data["data"][0]["senses"][y]["parts_of_speech"][p])+","
            completestring+="</br>"
            completestring+="<br>"
            for p in range(0, len(data["data"][0]["senses"][y]["english_definitions"])):
                completestring+=(data["data"][0]["senses"][y]["english_definitions"][p])+","
            completestring+="</br>"   
           

        print("END OF LINE \n")
    
    completestring+='"\n'
print(completestring)
fileswrite.write(completestring)
fileswrite.close()
    
    
        


 
