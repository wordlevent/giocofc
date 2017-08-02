#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import datetime
import random
import sys
from contextlib import ExitStack, contextmanager
from timeit import default_timer



path ="/home/pi/GIOCO/log.txt"

#Open a file
fo = open(path,"w")
fo.write("------------ START --------------\n")
fo.write(time.ctime()+"\n")
lista =[]
livello = 1#sys.argv[1]
lista.append(livello)

if int(lista[0]) == 1:
    choose = 5.5
    
if int(lista[0]) == 2:
    choose = 5.0

if int(lista[0]) == 3:
    choose = 4.5


if int(lista[0]) == 4:
    choose = 4.0


if int(lista[0]) == 5:
    choose = 3.5


if int(lista[0]) == 6:
    choose = 3.0


if int(lista[0]) == 7:
    choose = 2.5
    

if int(lista[0]) == 8:
    choose = 2.0    
    
fo.write("time 1 :" +str(choose)+" secondi \n")


END = 30
END_POLL = choose


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

punti = 0
punteggio = 0


start_mini = 0
start = time.time()


seconds_mini = 0
seconds = 0
finish_mini = 0

ch1 = False
ch2 = False
ch3 = False
ch4 = False
ch5 = False
ch6 = False
ch7 = False
ch8 = False



GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#output
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

#input
GPIO.output(4, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
GPIO.output(25, GPIO.HIGH)



def end_time():
    end = time.time()
    temp = end -start
    hours = temp//3600
    temp = temp - 3600*hours
    minutes = temp//60
    seconds = temp - 60*minutes
    if int(seconds) >= END:
        print(" ",punteggio)
        #chiudo il log
        fo.write("fn(end_minitime) punteggio =>" +str(punteggio) + " \n")
        fo.write(time.ctime()+" FINE GIOCO \n\n")
        fo.close()
        sys.exit()



def end_minitime(chIn, chOut, punti):
    global punteggio
    curr_time = time.time()
    finish_mini = start_mini + END_POLL
    print ("start",start_mini)
    print ("curr",curr_time)
    print ("finish",finish_mini)
    while time.time() <= finish_mini:
        end_time()
        if not GPIO.input(chIn):
            print("Colpito ")
            GPIO.output(chOut,True)
            punteggio +=1
            print("punto --",punteggio)
            fo.write("fn(end_minitime colpito => punteggio :" + str(punteggio)+"\n\n")
            return punteggio
        
    sec = curr_time - start_mini
    print("TIME:  => Non hai premuto nulla")
    fo.write("fn(end_minitime) Non hai premuto nulla \n")
    return punteggio  
    


    



    





def pressed(num, punti):

   
    
    global punteggio
    global start_mini
    start_mini = 0


    
    while num == 1:
        if punti == "None":
            punti = 0
        fo.write("fn(pressed): num "+str(num)+"\t punti:"+str(punti)+"\n")            
        start_mini = time.time()    
        punteggio = end_minitime(5,4,punti)
        fo.write("fn(pressed): SPENGO IL DISPLAY: 1 \n")
        GPIO.output(4,True)
        return punteggio
        

    while num == 2:
        
        if punti == "None":
            punti = 0
        fo.write("fn(pressed): num "+str(num)+"\t punti:"+str(punti)+"\n") 
        start_mini = time.time()    
        end_minitime(6,17,punti)
        fo.write("fn(pressed): SPENGO IL DISPLAY: 2 \n")
        GPIO.output(17,True)
        punti = punteggio
        return punti
   
    

    while num  == 3:

        if punti == "None":
            punti = 0
        fo.write("fn(pressed): num "+str(num)+"\t punti:"+str(punti)+"\n") 
        start_mini = time.time()    
        end_minitime(13,27,punti)
        fo.write("fn(pressed): SPENGO IL DISPLAY: 3 \n")
        GPIO.output(27,True)
        punti = punteggio
        return punti


    
    while num  == 4:
        if punti == "None":
            punti = 0
        fo.write("fn(pressed): num "+str(num)+"\t punti:"+str(punti)+"\n") 
        start_mini = time.time()    
        end_minitime(19,22,punti)
        fo.write("fn(pressed): SPENGO IL DISPLAY: 4 \n")
        GPIO.output(22,True)
        punti = punteggio
        return punti
    

        
       

    while num == 5:
        if punti == "None":
            punti = 0
        fo.write("fn(pressed): num "+str(num)+"\t punti:"+str(punti)+"\n") 
        start_mini = time.time()    
        end_minitime(26,18,punti)
        fo.write("fn(pressed): SPENGO IL DISPLAY: 5 \n")
        GPIO.output(18,True)
        punti = punteggio
        return punti

    
    while num == 6:
        if punti == "None":
            punti = 0
        fo.write("fn(pressed): num "+str(num)+"\t punti:"+str(punti)+"\n") 
        start_mini = time.time()    
        end_minitime(12,23,punti)
        fo.write("fn(pressed): SPENGO IL DISPLAY: 6 \n")
        GPIO.output(23,True)
        punti = punteggio
        return punti

        
        
        
    while num == 7:
        if punti == "None":
            punti = 0
        fo.write("fn(pressed): num "+str(num)+"\t punti:"+str(punti)+"\n") 
        start_mini = time.time()    
        end_minitime(16,24,punti)
        fo.write("fn(pressed): SPENGO IL DISPLAY: 7 \n")
        GPIO.output(24,True)
        punti = punteggio
        return punti

        
        

    
    while num == 8:
        if punti == "None":
            punti = 0
        fo.write("fn(pressed): num "+str(num)+"\t punti:"+str(punti)+"\n") 
        start_mini = time.time()    
        end_minitime(20,25,punti)
        fo.write("fn(pressed): SPENGO IL DISPLAY: 8 \n")
        GPIO.output(25,True)
        punti = punteggio
        return punti




fo.write("entro in while \n")
fo.write("Azzero i punti \n")
punti = 0
while True:

        numeroRandom = random.randint(1,8)
       
        
        if numeroRandom == 1:
           start_mini = time.time()
           punti=GPIO.output(4,False)
           punti = pressed(1,punti)
           
            

        if numeroRandom == 2:
            start_mini = time.time()
            GPIO.output(17,False)
            punti =pressed(2,punti)

        if numeroRandom == 3:
           start_mini = time.time()
           GPIO.output(27,False)
           punti = pressed(3,punteggio)
           
          

        if numeroRandom == 4:
           start_mini = time.time()
           GPIO.output(22,False)
           punti = pressed(4,punti)


        if numeroRandom == 5:
           start_mini = time.time()
           GPIO.output(18,False)
           punti = pressed(5,punti)


        if numeroRandom == 6:
           start_mini = time.time()
           GPIO.output(23,False)
           punti = pressed(6,punti)
 
        if numeroRandom == 7:
           start_mini = time.time()
           GPIO.output(24,False)
           punti = pressed(7,punti)
 
       
        if numeroRandom == 8:
           start_mini = time.time()
           GPIO.output(25,False)
           punti = pressed(8,punti)

        
        end_time()

        
GPIO.cleanup()
#test send url


    







