import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
Y = music_data["genre"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = tree.DecisionTreeClassifier()
model.fit(X, Y)

predictions = model.predict([[21, 1], [22, 0]])
# predice e gusto musical de un chico de 21 años, y de una chica de 22, datos que no estan en el dataset
print(predictions)

joblib.dump(model, "music-recomender.joblib")
# si corres esto una vez te almacena el modelo en un archivo y lo carga muucho mas rapido
model2 = joblib.load("music-recomender.joblib")

predictions2 = model2.predict([[28, 1], [33, 0]])
# predice e gusto musical de un chico de 28 años, y de una chica de 33, datos que no estan en el dataset
print(predictions2)

model.fit(X_train, Y_train)
predictions3 = model.predict(X_test)
score = accuracy_score(Y_test, predictions3)
print(score)    # si da muy bajo es que hay muy pocos datos

tree.export_graphviz(model, out_file='music-recomender.dot', feature_names=['age', 'gender'],
                     class_names=sorted(Y.unique()), label='all', rounded=True, filled=True)

