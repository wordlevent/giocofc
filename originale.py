import RPi.GPIO as GPIO
import time
import random
import sys
import array
from contextlib import ExitStack, contextmanager
from timeit import default_timer
import urllib.request as urllib2


nome = sys.argv[1]
cognome = sys.argv[2]
eta = sys.argv[3]
lista.append(nome)
lista.append(cognome)
lista.append(eta)










GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
punti = 0
punteggio = 0

END = 3


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

GPIO.setup(4,GPIO.OUT)

GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)



GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.output(4, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
GPIO.output(25, GPIO.HIGH)



def end_time():
    global punteggio
    global lista
    punteggio = 10
    end = time.time()
    temp = end -start
    hours = temp//3600
    temp = temp - 3600*hours
    minutes = temp//60
    seconds = temp - 60*minutes
    if int(seconds) >= END:
        print(punteggio)
        sys.exit()



def end_minitime(chIn, chOut, punti):
    global punteggio
    curr_time = time.time()
    finish_mini = start_mini + 5
    print ("start",start_mini)
    print ("curr",curr_time)
    print ("finish",finish_mini)
    while time.time() <= finish_mini:
        if GPIO.input(chIn):
            print("ho colpito Spengo il display acceso")
            GPIO.output(chOut,True)
            punteggio +=1
            print("punto --",punteggio)
            return punteggio
        
    print("Non hai premuto un cazzo per tutto il tempo")     
    return punteggio  
    


    



    





def pressed(num, punti):

    
    global punteggio
    global start_mini
    start_mini = 0
    while num == 1:
        
       
        start_mini = time.time()    
        punteggio = end_minitime(5,4,punti)
        print("Spengo il display 11")
        GPIO.output(4,True)
        return punteggio
        

    while num == 2:
        
       
        start_mini = time.time()    
        end_minitime(6,17,punti)
        print("Spengo il display 12")
        GPIO.output(17,True)
        punti = punteggio
        return punti
   
    

    while num  == 3:

        start_mini = time.time()    
        end_minitime(13,27,punti)
        print("Spengo il display 13")
        GPIO.output(27,True)
        punti = punteggio
        return punti


    
    while num  == 4:
        start_mini = time.time()    
        end_minitime(19,22,punti)
        print("Spengo il display 14")
        GPIO.output(22,True)
        punti = punteggio
        return punti
    

        
       

    while num == 5:

        start_mini = time.time()    
        end_minitime(26,18,punti)
        print("Spengo il display 15")
        GPIO.output(18,True)
        punti = punteggio
        return punti

    
    while num == 6:

        start_mini = time.time()    
        end_minitime(12,23,punti)
        print("Spengo il display 16")
        GPIO.output(23,True)
        punti = punteggio
        return punti

        
        
        
    while num == 7:

        start_mini = time.time()    
        end_minitime(16,24,punti)
        print("Spengo il display 17")
        GPIO.output(24,True)
        punti = punteggio
        return punti

        
        

    
    while num == 8:

        start_mini = time.time()    
        end_minitime(20,25,punti)
        print("Spengo il display 18")
        GPIO.output(25,True)
        punti = punteggio
        return punti




while True:

        numeroRandom = random.randint(1,8)
        
        if numeroRandom == 1:
           start_mini = time.time()
           punti=GPIO.output(4,False)
           print("Accendo il display1")
           punti = pressed(1,punti)
           print("<<",punti)
        
            

        if numeroRandom == 2:
            start_mini = time.time()
            GPIO.output(17,False)
            print("Accendo il display2")
            punti =pressed(2,punti)
            
            print("<<",punti )


        if numeroRandom == 3:
           start_mini = time.time()
           GPIO.output(27,False)
           print("Accendo il display3")
           punti = pressed(3,punteggio)
           
           print("<<",punti )


        if numeroRandom == 4:
           start_mini = time.time()
           GPIO.output(22,False)
           print("Accendo il display4")
           punti = pressed(4,punti)
           print("<<",punti )


        if numeroRandom == 5:
           start_mini = time.time()
           GPIO.output(18,False)
           print("Accendo il display5")
           punti = pressed(5,punti)
           print("<<",punti )


        if numeroRandom == 6:
           start_mini = time.time()
           GPIO.output(23,False)
           print("Accendo il display6")
           punti = pressed(6,punti)
           print("<<",punti )

        if numeroRandom == 7:
           start_mini = time.time()
           GPIO.output(24,False)
           print("Accendo il display7")
           punti = pressed(7,punti)
           print("<<",punti )


        
        if numeroRandom == 8:
           start_mini = time.time()
           GPIO.output(25,False)
           print("Accendo il display8")
           punti = pressed(8,punti)
           print("<<",punti )

        end_time()

GPIO.cleanup()
#test send url

