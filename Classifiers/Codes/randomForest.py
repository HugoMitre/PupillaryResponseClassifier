import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import itertools

# Se carga archivo csv con las métricas calculadas para cada prueba.
datos = pd.read_csv('D:/VariablesVisual.csv')
datos=datos[['nivel','blps','mpdc','apcps','pd1','entropy','TTP','PST']]
datos=datos.astype(float)

a_list= ['blps','mpdc','apcps','pd1','entropy','TTP','PST']
all_combinations = []
for r in range(len(a_list) + 1):
    combinations_object = itertools.combinations(a_list, r)
    combinations_list = list(combinations_object)
    all_combinations += combinations_list
all_combinations=all_combinations[1:]

# y=Nivel de dificultad de la prueba, x=Características
y=datos.nivel

uno = []
tres = []
seis = []
macro = []
weighted = []
subconjunto=[]
count = 1
for features in all_combinations:
    features = list(features)
    X=datos[features]
    
    # Se separan los datos para entrenamiento (80%) y evaluación (20%).
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

    # Se crea y entra el modelo
    rf=RandomForestClassifier(n_estimators=100)
    rf.fit(x_train,y_train)

    # Matriz de confusión y reporte de estadísticas.
    y_pred = rf.predict(x_test)
    reporte = classification_report(y_test,y_pred)
     
    uno.append(reporte[74:78])
    tres.append(reporte[128:132])
    seis.append(reporte[182:186])
    macro.append(reporte[291:295])
    weighted.append(reporte[345:349])
    subconjunto.append('/'.join(features))
    print(count)
    count += 1
reporte = pd.DataFrame({'subconjunto':subconjunto,'uno':uno,'tres':tres,'seis':seis,'macro':macro,'weighted':weighted})
reporte.to_excel('randomForest.xlsx')