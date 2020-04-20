#No 1
class MhsTIF(object):
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.KotaTinggal = kota
        self.UangSaku = us

c0 = MhsTIF('Ika',10,'Sukoharjo',240000)
c1 = MhsTIF('Budi',51,'Sragen',230000)
c2 = MhsTIF('Ahmad',2,'Surakarta',250000)
c3 = MhsTIF('Chandra',18,'Surakarta',235000)
c4 = MhsTIF('Eka',4,'Boyolali',240000)
c5 = MhsTIF('Fandi',31,'Salatiga',250000)
c6 = MhsTIF('Deni',13,'Klaten',245000)
c7 = MhsTIF('Galuh',5,'Wonogiri',245000)
c8 = MhsTIF('Janto',23,'Klaten',245000)
c9 = MhsTIF('Hasan',64,'Karanganyar',270000)
c10 = MhsTIF('Khalid',29,'Purwodadi',230000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

def array(koleksi):
    index = []
    for i in Daftar:
        index.append(i.NIM)
    return index

def sorting(koleksi):
    output = []
    n = len(koleksi)
    for i in range(n-1):
        for j in range(n-i-1):
            if koleksi[j] > koleksi[j+1]:
                temp = koleksi[j]
                koleksi[j] = koleksi[j+1]
                koleksi[j+1] = temp

def printArray(koleksi):
    for i in koleksi:
        print(i,end=" ")

index = array(Daftar)
sorting(index)
printArray(index)
print()

#No 2
A = [7,11,13,16,19]
B = [8,12,14,15,20]

def gabungList(A,B):
    la = len(A)
    lb = len(B)
    C = list()
    i = 0; j=0
    while i < la and j < lb:
         if A[i] < B[j]:
             C.append(A[i])
             i += 1
         else:
             C.append(B[j])
             j += 1
    while i < la:
        C.append(A[i])
        i += 1
    while j < lb:
        C.append(B[j])
        j += 1
    print(C)

gabungList(A,B)
print()

#No 3
def bubbleSort(koleksi):
    n = len(koleksi)
    for i in range(n-1):
        for j in range(n-i-1):
            if koleksi[j] > koleksi[j+1]:
                temp = koleksi[j]
                koleksi[j] = koleksi[j+1]
                koleksi[j+1] = temp

def selectionSort(koleksi):
    n = len(koleksi)
    for i in range(n-1):
        index = i
        for j in range(i+1,n):
            if koleksi[j] < koleksi[index]:
                index = j
        temp = koleksi[index]
        koleksi[index] = koleksi[i]
        koleksi[i] = temp

def insertionSort(koleksi):
    i = 1
    temp = 0
    n = len(koleksi)
    while i < n:
        j = i
        while j>0 and koleksi[j-1]>koleksi[j]:
            temp = koleksi[j]
            koleksi[j] = koleksi[j-1]
            koleksi[j-1] = temp
            j -=1
        i += 1 
                   
from time import time as detak
from random import shuffle as kocok
k = list(range(1,6001))
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw = detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw = detak();insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw));
