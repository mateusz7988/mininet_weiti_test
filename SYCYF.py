import matplotlib.pyplot as plt
import scipy.signal as scp
import numpy as np
lista = []
og_pattern = []  # lista, na ktorej sa wspolne
                 # punkty umiejscowione w tym samym miejscu i w tym samym czasie w sygnalach A i B
twoja_stara=[]  #lista dla beki lol
siema = []

def PunktyA(sciezkaA):
    punkcikA = open(sciezkaA, "r")             #ta czesc kodu zmienia plik .txt na liste z wartosciami sygnalu A
    linesA = punkcikA.read().split("\n")
    for i in range(0, 5):
        linesA.pop(0)
    for i in range(0,len(linesA)):
        linesA[i] = float(linesA[i])

    return linesA

def PunktyB(sciezkaB):
    punkcikB = open(sciezkaB, "r")
    linesB = punkcikB.read().split("\n")     #ta robi to samo ale dla sygnalu B
    for i in range(0, 5):
        linesB.pop(0)
    for i in range(0,len(linesB)):
        linesB[i] = float(linesB[i])
    return linesB

def PunktyX(sciezkaX):
    punkcikX = open(sciezkaX, "r")
    linesX = punkcikX.read().split("\n")     #ta robi to samo ale dla sygnalu X
    for i in range(0, 5):
        linesX.pop(0)
    for i in range(0,len(linesX)):
        linesX[i] = float(linesX[i])
    plt.plot(linesX)
    plt.show()
    return linesX


def Dictionary(linesA, linesB):
    for i in range(0, len(linesA)):      #ta funkcja wstawia do pustej listy wartosc 1 gdy sygnal w A i B ma taka sama wartosc
                                            # lub 0 gdy sygnaly sie roznia
        if linesA[i] == linesB[i]:
            lista.append(1)
        else:
            lista.append(0)
    print(lista)
    print(len(lista))
    print(lista.index(1))
    return lista

def gowienko(lista, linesA):
    for i in range(0,len(lista)):
        if lista[i] == 1:                  #ta funkcja wypisuje wartosci, ktore sa wspolne dla A i B w okreslonej jednostce czasu
            og_pattern.append(linesA[i])
        else:
            pass
    return og_pattern

def StrToFloat_Ogpattern(og_pattern):
    for i in range(0,len(og_pattern)):
        og_pattern[i] = float(og_pattern[i])           #zamienia string na float
    print(og_pattern)
    print(len(og_pattern))
    plt.plot(og_pattern)
    plt.show()
    #plt.savefig("D:\SYCYF\Projekt\Zadanie projektowe\wykresOG.png")
    return og_pattern

def StrToFloat_linesA(linesA):
    for i in range(0,len(linesA)):
        linesA[i] = float(linesA[i])              #zamienia string na float
    print(linesA)
    return linesA

def StrToFloat_linesB(linesB):
    for i in range(0,len(linesB)):
        linesB[i] = float(linesB[i])              #zamienia string na float
    print(linesB)
    return linesB

def StrToFloat_linesX(linesX):
    for i in range(0,len(linesX)):
        linesX[i] = float(linesX[i])              #zamienia string na float
    print(linesX)
    return linesX

def Finder(linesX, linesA):
    for i in linesA:
        if i in linesX:
            twoja_stara.append(1)
        else:
            twoja_stara.append(0)
    print(twoja_stara)
    print(len(twoja_stara))
    print(twoja_stara.index(1))
    print(twoja_stara.count(1))
    return twoja_stara

def Finder2(twoja_stara,linesA):
    for i in range(0, len(twoja_stara)):
        if twoja_stara[i] == 1:
            siema.append(linesA[i])
        else:
            pass
    print(siema)
    print(len(siema))
    return siema

def FindingSin(twoja_stara):
    for i in range(0, len(twoja_stara)):
        while (twoja_stara[i] == 1 and twoja_stara[i+1] == 1):
            print("chuj?")
            i = i+1
        else:
            pass

def Filter(linesA, linesX):
    x = np.arange(1, 100, 0.1)
    n = 1000  # the larger n is, the smoother curve will be
    b = [1.0 / n] * n
    a = 1
    yyy = scp.lfilter(b, a, linesX)
    yy = scp.lfilter(b, a, linesA)
    s = scp.savgol_filter(linesA, 5000, 2)
    plt.plot(yy, linewidth=2, linestyle="-", c="b")  # smooth by filter
    y = scp.lfilter(b, a, yy)
    p = scp.lfilter(b, a, y)
    fgust = scp.filtfilt(b, a, yy, method="gust")
    fpad = scp.filtfilt(b, a, p, padlen=50)
    plt.plot(yy, 'k-', label='input')
    plt.plot(fgust, 'b-', linewidth=4, label='gust')
    #plt.plot(fpad, 'g-', linewidth=4, label='y')
    plt.show()
    plt.plot(linesX)
    plt.show()
if __name__ == "__main__":
    FindingSin(Finder2(Finder(PunktyX("D:\SYCYF\Projekt\Zadanie projektowe\sent8.txt"),
                   PunktyA("D:\SYCYF\Projekt\Zadanie projektowe\PunktA.txt")),
            PunktyA("D:\SYCYF\Projekt\Zadanie projektowe\PunktA.txt")))
    Filter(PunktyA("D:\SYCYF\Projekt\Zadanie projektowe\PunktA.txt"), PunktyX("D:\SYCYF\Projekt\Zadanie projektowe\sent8.txt"))
    Filter(PunktyB("D:\SYCYF\Projekt\Zadanie projektowe\PunktB.txt"), PunktyX("D:\SYCYF\Projekt\Zadanie projektowe\sent8.txt"))