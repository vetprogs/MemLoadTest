#Автор https://github.com/vetprogs
#По вопросам и предложениям:  vetprogs@rambler.ru

import time
import random
import hashlib

massshash=[]

mymax=50000 #начинаем с 100к хешей

while True:
    st_run=time.time()
    z=0
    mymax=mymax*2
    
    while z<mymax:
        rawdata = 1000*random.random() #добавим рандома по фану, для получения разных хешей, чтобы избежать возможного кеширования
        mysha = hashlib.sha256(str(rawdata).encode("utf-8")).hexdigest() #For Sha256 hash 64 символа
        massshash.append(mysha)
        z+=1
    print(len(massshash)/1000,'k хешей в памяти')    
    print(f'Выполнено за: {(time.time()-st_run)*1000:1.2f} ms')
    pp=input('Нажмите Enter, 1 = выход')
    if pp == '1':
        exit()
