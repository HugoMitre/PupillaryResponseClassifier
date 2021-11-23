import numpy as np
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import itertools

# Se carga archivo csv con las métricas calculadas para cada prueba.
datos = pd.read_csv('C:/Users/josan/OneDrive/Documentos/Tesis/Memoria de trabajo/Analisis/analisis-tareas-de-memoria-de-trabajo/VariablesVisualActualizado.csv')
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
recallUno=[]
recallTres=[]
recallSeis=[]
recallMacro=[]
recallWeighted=[]
f1Uno=[]
f1Tres=[]
f1Seis=[]
f1Macro=[]
f1Weighted=[]
count = 1
for features in all_combinations:
    features = list(features)
    X=datos[features]
    #print('Cantidad de pruebas por nivel:')
    #print(datos['nivel'].value_counts())
    #print(X.columns)
    
    # Se separan los datos para entrenamiento (80%) y evaluación (20%).
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

    # Se crea y entra el modelo
    rf=RandomForestClassifier(n_estimators=100)
    rf.fit(x_train,y_train)

    # Matriz de confusión y reporte de estadísticas.
    y_pred = rf.predict(x_test)
    #print(confusion_matrix(y_test,y_pred))
    #print(classification_report(y_test,y_pred))
    reporte = classification_report(y_test,y_pred)
     
    uno.append(reporte[74:78])
    tres.append(reporte[128:132])
    seis.append(reporte[182:186])
    macro.append(reporte[291:295])
    weighted.append(reporte[345:349])
    subconjunto.append('/'.join(features))
    recallUno.append(reporte[84:88])
    recallTres.append(reporte[138:142])
    recallSeis.append(reporte[192:196])
    recallMacro.append(reporte[301:305])
    recallWeighted.append(reporte[355:359])
    f1Uno.append(reporte[94:98])
    f1Tres.append(reporte[148:152])
    f1Seis.append(reporte[202:206])
    f1Macro.append(reporte[311:315])
    f1Weighted.append(reporte[365:369])
    print(count)
    count += 1
    #print("********************")
reporte = pd.DataFrame({'Subset':subconjunto,'Precision:L':uno,'Precision:M':tres,'Precision:H':seis,'Precision:Macro':macro,'Precision:Weighted':weighted,'Recall:L':recallUno,'Recall:M':recallTres,'Recall:H':recallSeis,'Recall:Macro':recallMacro,'Recall:Weighted':recallWeighted,'F1:L':f1Uno,'F1:M':f1Tres,'F1:H':f1Seis,'F1:Macro':f1Macro,'F1:Weighted':f1Weighted})
reporte.to_excel('randomForest2.xlsx')