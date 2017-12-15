# 131044019 - Gozde DOGAN
# CSE321_Introduction to Algorithm Design
# Homework 2 - Question 4
# Towers Of Hanoi Problem, recursive

import sys

def main():
    #mesafeler icin global degiskenler tanimladim
    global distance2 
    global distance1     
    distance2 = 2
    distance1 = 1
    
    
    SRC = [1, 2, 3, 4] #tasinacak liste
    copySRC = SRC[:] #Hangi diskin tasindigini anlayabilmek icin tasinacak listeyi yedekledim
    AUX = [] #listeyi tasirken yardimci olacak liste
    DST = [] #listenin tasinacagi liste
    sizeSRC = len(SRC) #listenin boyutu
    diskTimes = [] #disklerin kat edildigi mesafeyi tutan liste
    
    #diskTimes'daki degerler toplanarak gidilecegi icin ilk degerlerini 0 yaptim
    i=0
    while i<sizeSRC:
        diskTimes.insert(i, 0);
        i=i+1
    
    #tasinacak liste ve tasinacagi listenin ilk hali ekrana yazildi
    print "\nSRC:", SRC
    print "DST:", DST , "\n"
    
    print "\ninput size is", sizeSRC, "\n"
    
    #diskleri diger listeye tasiyacak metot cagrildi
    towersOfHanoi(SRC, AUX, DST, sizeSRC, copySRC, diskTimes)
    
    #tasinan liste ve tasindigi listenin son hali ekrana yazildi
    print "\nSRC:", SRC
    print "DST:", DST , "\n"
    
    #disklerin tasinma sureleri yazdirildi
    i=0
    while i<len(copySRC):
        print "Elapsed Time Disk" , copySRC[i], ":", diskTimes[i]
        i=i+1

#derste kurulan algoritma kullanildi, mesafe hesabi icin eklemeler yapildi
def towersOfHanoi(SRC, AUX, DST, sizeSRC, copySRC, diskTimes):
    if sizeSRC==1:
        temp = SRC.pop(0) #listeden eleman cekildi
        DST.append(temp)  #cekilen eleman diger listeye eklendi 
        calculateDistance(diskTimes, temp, sizeSRC, copySRC)       
        print "Disk", temp, ":", "SRC to DST"
    else:
        temp = SRC.pop(0) #listeden eleman cekildi
        AUX.append(temp)  # cekilen eleman diger listeye eklendi 
        calculateDistance(diskTimes, temp, sizeSRC, copySRC)          
        print "Disk", temp, ":", "SRC to AUX"
        towersOfHanoi(SRC, DST, AUX, sizeSRC-1, copySRC, diskTimes)
        #listeden ilk eleman cekildigi icin size 1 eksilterek yollandi
        
        temp = AUX.pop(0) #listeden eleman cekildi
        DST.append(temp)  # cekilen eleman diger listeye eklendi 
        calculateDistance(diskTimes, temp, sizeSRC, copySRC)
        print "Disk", temp, ":", "AUX to DST"
        towersOfHanoi(AUX, SRC, DST, sizeSRC-1, copySRC, diskTimes)
        #listeden ilk eleman cekildigi icin size 1 eksilterek yollandi
        
#elemanlari tasiyan ve mesafeyi hesaplayan fonksiyon 
#mesafe hesabi, diskin agirligi*kat edilen mesafe seklinde yapildi  
def calculateDistance(diskTimes, temp, sizeSRC, copySRC):
    i=0
    while i<sizeSRC:
        if copySRC[i] == temp:
            diskTimes.insert(i, diskTimes[i]+(distance1*temp));
        i=i+1

#Bu dosya calistirildginda calistirilacak fonksiyon belirtildi        
if __name__ == "__main__":
    main()
