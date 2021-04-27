import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix
import itertools
from sklearn.preprocessing import StandardScaler

# Se carga archivo csv con las métricas calculadas para cada prueba.
datos = pd.read_csv('D:/GoogleDriveCIMAT/CIMAT/Tesis/Memoria de trabajo/Analisis/analisis-tareas-de-memoria-de-trabajo/VariablesVisualActualizado.csv')
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
    #print('Cantidad de pruebas por nivel:')
    #print(datos['nivel'].value_counts())
    #print(X.columns)
    
    # Se separan los datos para entrenamiento (80%) y evaluación (20%).
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        random_state=42,
                                                        stratify=y)
    sc = StandardScaler()
    X_train_array = sc.fit_transform(X_train.values)
    X_train = pd.DataFrame(X_train_array, index=X_train.index, columns=X_train.columns)
    X_test_array = sc.transform(X_test.values)
    X_test = pd.DataFrame(X_test_array, index=X_test.index, columns=X_test.columns)
    
    C = 1.0
    models = svm.SVC(kernel='poly', degree=3, gamma='auto', C=C)
    
    #print(models)
    models.fit(X_train,y_train)
    y_pred = models.predict(X_test)
    # reporte de estadísticas.
    reporte = classification_report(y_test,y_pred)
     
    uno.append(reporte[74:78])
    tres.append(reporte[128:132])
    seis.append(reporte[182:186])
    macro.append(reporte[291:295])
    weighted.append(reporte[345:349])
    subconjunto.append('/'.join(features))
    print(count)
    count += 1
    #print("********************")
reporte = pd.DataFrame({'subconjunto':subconjunto,'uno':uno,'tres':tres,'seis':seis,'macro':macro,'weighted':weighted})
reporte.to_excel('poly2.xlsx')