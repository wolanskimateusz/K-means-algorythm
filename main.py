import numpy as np
import math


#przykladowe dane
dane_wej = [[1,2],
            [2,3],
            [7,6],
            [7,8]]

#wstepne zalozenia
centra = [[1,2],
         [2,3]]

ilosc_grup = 2

#Algorytm
def wyzMacierzyD(dane_wej, ilosc_grup,centra):
    macierzD = np.zeros((ilosc_grup,len(dane_wej)))
    for j in range(ilosc_grup):
        for i in range(len(dane_wej)):
            macierzD[j][i] = math.hypot(dane_wej[i][0] - centra[j][0], dane_wej[i][1] - centra[j][1])

    return macierzD
    
def wyzMacierzyG(macierzD):
    macierzG = np.zeros((macierzD.shape[0],macierzD.shape[1]))
    for j in range(macierzD.shape[1]):
        min_wartosc = np.min(macierzD[:,j])
        for i in range(macierzD.shape[0]):
            if macierzD[i][j] == min_wartosc:
                macierzG[i][j] = 1
            else:
                macierzG[i][j] = 0
    return macierzG

            
def wyzNowychC(macierzG,dane_wej,ilosc_grup):
    C = np.zeros((ilosc_grup,len(dane_wej[0])))
    for i in range(ilosc_grup):
        licznik = np.zeros(len(dane_wej[0]))
        mianownik = 0
        for j in range(len(dane_wej)):
            licznik += macierzG[i][j] * np.array(dane_wej[j])
            mianownik += macierzG[i][j]
        
        if(mianownik != 0):
            C[i] = licznik / mianownik
        else: 
            C[i] = np.zeros(len(dane_wej[0]))
    return C


    
#wywolanie   
max_iter = 0
macierzG = np.zeros((ilosc_grup,len(dane_wej)))
while(max_iter < 100):
    macierzD = wyzMacierzyD(dane_wej, ilosc_grup, centra)
    macierzGnowe = wyzMacierzyG(macierzD)
    if(np.allclose(macierzG,macierzGnowe)): 
        break
    else: 
        macierzG = macierzGnowe
    centra = wyzNowychC(macierzG, dane_wej, ilosc_grup)
    max_iter += 1
    
print(macierzG)
print(max_iter)
