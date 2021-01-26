from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pickle

iris=load_iris()
x_train, x_test, y_train, y_test=train_test_split(iris['data'], iris['target'], random_state=0)
knn=KNeighborsClassifier(n_neighbors=10)
knn.fit(x_train, y_train)



x_data=np.array([[5,1,2,0.1]])
print("에측한 붓꽃: {}".format(iris['target_names'][(knn.predict(x_data))]))
print(knn.predict(x_data))
#
pickle.dump(knn, open("iris_model_test.sav", "wb"))