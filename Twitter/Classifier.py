
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
dirpath = os.getcwd()+'/Twitter/'

def KNN(dataset):
    # Importing the dataset

    X = dataset.iloc[:, [0,1,2,3,4]].values
    y = dataset.iloc[:, 6].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Fitting classifier to the Training set
    # Create your classifier here
    classifier = KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
    classifier.fit(X_train,y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)

    # print(cm)
    return cm

def NaiveBayesClassifier(dataset):
    # Importing the dataset
    X = dataset.iloc[:, [0,1,2,3,4]].values
    y = dataset.iloc[:, 6].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Fitting classifier to the Training set
    # Create your classifier here
    classifier=GaussianNB()
    classifier.fit(X_train,y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)

    # print(cm)
    return cm


def SVM(dataset):
    # Importing the dataset
    X = dataset.iloc[:, [0,1,2,3,4]].values
    y = dataset.iloc[:, 6].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Fitting classifier to the Training set
    # Create your classifier here
    classifier = SVC(kernel='linear',random_state=0)
    classifier.fit(X_train,y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)

    # print(cm)
    return cm


def DecisionTree(dataset):
    # Importing the dataset
    # dataset = pd.read_csv('dataset_gen.csv')
    X = dataset.iloc[:, [0,1,2,3,4]].values
    y = dataset.iloc[:, 6].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Fitting classifier to the Training set
    # Create your classifier here
    classifier = DecisionTreeClassifier(criterion='entropy',random_state=0)
    classifier.fit(X_train,y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)

    # print(cm)
    return cm


def RandomForest(dataset):
    # Importing the dataset
    # dataset = pd.read_csv('dataset_gen.csv')
    X = dataset.iloc[:, [0,1,2,3,4]].values
    y = dataset.iloc[:, 6].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Fitting classifier to the Training set
    # Create your classifier here
    classifier = RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
    classifier.fit(X_train,y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)

    # print(cm)
    return cm

dataset=None
try:
    dataset = pd.read_csv(dirpath+'dataset_gen.csv')
except:
    dataset = pd.read_csv('dataset_gen.csv')
cm=KNN(dataset)
cm=NaiveBayesClassifier(dataset)
cm=DecisionTree(dataset)
cm=RandomForest(dataset)
cm=SVM(dataset)
