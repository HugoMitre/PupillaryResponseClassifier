import os
from xml.dom import minidom
from xml.dom.minidom import parse
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
import sys


def convertirTiempo(datos):   
    datos['tiempo']=0
    for x in range(1,len(datos['tiempo'])):
        if(datos.timestamp_microsec[x]>datos.timestamp_microsec[x-1]):
            datos.tiempo[x] = datos.timestamp_microsec[x]-datos.timestamp_microsec[x-1] + datos.tiempo[x-1]
        else:
            datos.tiempo[x] = 1000000 - datos.timestamp_microsec[x-1] + datos.tiempo[x-1] + datos.timestamp_microsec[x]
    return datos

def filtrarDatos(datos):
    contador = 0
    tamInicial = len(datos)
    diameter_pupil_lefteye = np.array(datos.diameter_pupil_lefteye)
    diameter_pupil_righteye = np.array(datos.diameter_pupil_righteye)
    timestamp_microsec = np.array(datos.tiempo)
    pupilsize = np.zeros(tamInicial)
    
    tiempo = 0
    inicioBlink = 0
    numeroDeBlinks = 0

    for x in range(0,tamInicial):
        if (diameter_pupil_lefteye[x] == -1 and inicioBlink == 0):
            inicioBlink = 1
        elif (diameter_pupil_lefteye[x] == -1 and inicioBlink == 1):
            tiempo = tiempo + timestamp_microsec[x]-timestamp_microsec[x-1]
        elif (diameter_pupil_lefteye[x] != -1 and inicioBlink == 1):
            if (tiempo>=100000 and tiempo<=400000):
                numeroDeBlinks = numeroDeBlinks + 1
                inicioBlink = 0
                tiempo = 0
            else:
                inicioBlink = 0
                tiempo = 0
        else:
            inicioBlink = 0
            tiempo = 0
            
    while 1:
        if contador==len(diameter_pupil_lefteye):
            break;

        if (diameter_pupil_lefteye[contador]!=-1 and diameter_pupil_righteye[contador]!=-1):
            pupilsize[contador] = (diameter_pupil_lefteye[contador] + diameter_pupil_righteye[contador])/2
            contador += 1

        elif (diameter_pupil_lefteye[contador]==-1 and diameter_pupil_righteye[contador]!=-1):
            pupilsize[contador] = diameter_pupil_righteye[contador]
            contador += 1

        elif (diameter_pupil_lefteye[contador]!=-1 and diameter_pupil_righteye[contador]==-1):
            pupilsize[contador] = diameter_pupil_lefteye[contador]
            contador += 1
        else:
            timestamp_microsec = np.delete(timestamp_microsec, contador)
            diameter_pupil_lefteye = np.delete(diameter_pupil_lefteye, contador)
            diameter_pupil_righteye = np.delete(diameter_pupil_righteye, contador)
            pupilsize = np.delete(pupilsize, contador)

    tamFinal = len(pupilsize)
    porcent = (100/tamInicial)*tamFinal
    print(porcent)
    
    return pupilsize, timestamp_microsec, porcent, numeroDeBlinks

def hampel(x,k,thr=3):
    arraySize = len(x)
    idx=np.arange(arraySize)
    newX=x.copy()
    omadIdx=np.zeros_like(x)
    for i in range(arraySize):
        mask1=np.where( idx>= (idx[i]-k) ,True, False)
        mask2=np.where( idx<= (idx[i]+k) ,True, False)
        kernel= np.logical_and(mask1,mask2)
        med0=np.median(x[kernel])
        s0=1.4826*np.median(np.abs(x[kernel]-med0))
        if np.abs(x[i]-med0)>thr*s0:
            omadIdx[i]=1
            newX[i]=med0
    return newX

def baseLine(pupilsize, timestamp_microsec):
    x=pd.DataFrame({'pupil':pupilsize,'time':timestamp_microsec})
    blps = x[x['time']<=2000000].tail(20).pupil.mean()
    i = len(x[x['time']<=2000000])
    return blps, i

def meanPupilDiameterChange(pupilsize,BLPS,i):
    pupil = np.mean(pupilsize[i+1:])
    MPDC = pupil - BLPS
    return MPDC

def avaragePercentageChangePupil(pupilsize,BLPS,i):
    pcps = 0
    pupil = pupilsize[i+1:]
    PCPS = (pupil-BLPS)/BLPS
    APCPS = PCPS.mean()
    return APCPS

def peakDilation(pupilsize,i):
    PD1 = np.max(pupilsize[i+1:])
    return PD1

def pupilEntropy(pupilsize,i):
    A = pupilsize[i+1:]
    pA = A / A.sum()
    Shannon2 = -np.sum(pA*np.log2(A))
    return Shannon2

def timeToPeakPupilSize(pupilsize,i,pd1,timestamp_microsec,blps):
    x=pd.DataFrame({'pupil':pupilsize,'time':timestamp_microsec})
    ttp = x[x['pupil'] == (pd1+blps)].head(1).time.values[0]
    return ttp

def peakDilationSpeed(pupilsize,i,timestamp_microsec, pd1,blps):
    mincuadrados=pd.DataFrame({'y':pupilsize[i+1:],'x':timestamp_microsec[i+1:]})
    indexpd = mincuadrados[mincuadrados['y']==(pd1+blps)].head(1).index[0]
    if(indexpd>=1):
        mincuadrados = mincuadrados.iloc[:indexpd]
        mincuadrados['xy'] = mincuadrados.x*mincuadrados.y
        mincuadrados['x2'] = mincuadrados.x**2
        m = (np.mean(mincuadrados.xy)-np.mean(mincuadrados.x)*np.mean(mincuadrados.y))/(np.mean(mincuadrados.x2)-np.mean(mincuadrados.x)**2)
        PDS = np.arctan(m)
    else:
        PDS=0
    return PDS

def inform(subject, archivos):
    informacion = pd.read_csv("InformacionPruebasVisual.csv")
    name = archivos[0:-4]
    posicion = -99
    for x in range(0,len(informacion)):
        if (name == informacion.Name[x] and informacion.Subject[x]==subject):
            posicion = x
            break
    if posicion == -99:
        nivel = 0
    elif str(informacion.Stimulus_sequence[posicion])=='nan':
        nivel = 0
    else:
        nivel = len(informacion.Stimulus_sequence[posicion])-((len(informacion.Stimulus_sequence[posicion])-1)/2)-2

    training = informacion.Training[posicion]


    return subject, name, training, nivel

def archivo(subject, name, training, nivel, blps, mpdc, apcps, pd1, entropy, TTP, PDS):
    if os.path.isfile('VariablesVisual.csv')==False:
        data = pd.DataFrame(columns=('subject', 'name', 'training', 'nivel', 'blps', 'mpdc', 'apcps', 'pd1', 'entropy', 'TTP','PDS'))
        data.loc[len(data)]=[subject, name, training, nivel, blps, mpdc, apcps, pd1, entropy, TTP, PDS]
        data.to_csv('VariablesVisual.csv', index = None, header=True)
    else:
        data = pd.read_csv('VariablesVisual.csv')
        data.loc[len(data)]=[subject, name, training, nivel, blps, mpdc, apcps, pd1, entropy, TTP, PDS]
        data.to_csv('VariablesVisual.csv', index = None, header=True)

participantes = 17
epsilon = sys.float_info.epsilon

for x in range(1,participantes+1):
    if x<=9:
        origen = "D:/visual-data/s0"+str(x)
    else:
        origen = "D:/visual-data/s"+str(x)

    for carpetas in os.listdir(origen):
        if (carpetas[0]=='S' or carpetas[0]=='s'):      
            for archivos in os.listdir(os.path.join(origen,carpetas)):
                if archivos[-1]=='v':
                    csv = origen+'/'+carpetas+'/'+archivos
                    datos = pd.read_csv(csv)
                    print("####"+csv+"###")
                    datos = convertirTiempo(datos)
                    [pupilsize, timestamp_microsec, porcent, numeroDeBlinks] = filtrarDatos(datos)
                    [subject, name, training, nivel] = inform(origen[-3:],archivos)
                    if(training == False and (nivel==1 or nivel==3 or nivel==6) and porcent>=70):
                        pupilsize = savgol_filter(pupilsize, 13, 2)
                        [blps,i] = baseLine(pupilsize, timestamp_microsec)
                        mpdc = meanPupilDiameterChange(pupilsize,blps, i)
                        apcps = avaragePercentageChangePupil(pupilsize,blps,i)
                        pd1 = peakDilation(pupilsize,i)-blps
                        entropy = pupilEntropy(pupilsize,i)
                        TTP = timeToPeakPupilSize(pupilsize,i,pd1,timestamp_microsec,blps)
                        PDS = peakDilationSpeed(pupilsize,i,timestamp_microsec, pd1, blps)
                        print(nivel)
                        archivo(subject, name, training, nivel, blps, mpdc, apcps, pd1, entropy, TTP, PDS) 
