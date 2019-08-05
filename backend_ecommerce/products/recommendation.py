import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from ecom import settings

def most_frequent(List): 
    return max(set(List), key = List.count) 

def recommend(input_pd_dataframe):
    # testset = pd.read_csv('./Test.csv',header= None)
    testset = input_pd_dataframe
    print(testset)
    myrow= testset
    settings.BASE_DIR
    dataset = pd.read_csv(settings.BASE_DIR + '/static_my_proj/Dataset.csv',header= None)
  
    frames = [dataset, myrow]
    dataset = pd.concat(frames)
    
    pd.options.display.max_columns=1000
    pd.options.display.max_rows=1000
    
    dataset = dataset.iloc[1:, :]
    y= dataset.iloc[:-1,-1:]

    dataset = dataset.iloc[:, :-1]

    x = dataset.values
    #encoding categorical data
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder

    #first applying label encoding to convert strings to number.
    # display(x[:,2])
    labelencoder_x_1 = LabelEncoder()
    labelencoder_x_2 = LabelEncoder()
    labelencoder_x_3 = LabelEncoder()
    labelencoder_x_4 = LabelEncoder()
    x[:, 2] = labelencoder_x_1.fit_transform(x[:, 2])
    x[:, 4] = labelencoder_x_2.fit_transform(x[:, 4])
    x[:, 5] = labelencoder_x_3.fit_transform(x[:, 5])
    x[:, 8] = labelencoder_x_4.fit_transform(x[:, 8])

    onehotencoder_1 = OneHotEncoder(categorical_features = [2])
    x = onehotencoder_1.fit_transform(x).toarray()

    df=pd.DataFrame(x)

    onehotencoder_2 = OneHotEncoder(categorical_features = [7])
    x = onehotencoder_2.fit_transform(x).toarray()

    onehotencoder_3 = OneHotEncoder(categorical_features = [12])
    x = onehotencoder_3.fit_transform(x).toarray()

    onehotencoder_4 = OneHotEncoder(categorical_features = [19])
    x = onehotencoder_4.fit_transform(x).toarray()

    dataset_train= x

    dataset_train1 = dataset_train[:-1]
    x_train =  dataset_train1
    y_train = y

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(dataset_train1, y, test_size = 0.01, random_state = 0)

    #feature scaling
    from sklearn.preprocessing import StandardScaler
    sc_x = StandardScaler()
    x_train = sc_x.fit_transform(x_train)
    x_test = sc_x.transform(x_test)

    df2 = pd.DataFrame(x_train)

    models = []
    models.append(('Logistic Regression', LogisticRegression()))
    models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))
    #models.append(('K-Nearest Neighbour ', KNeighborsClassifier()))
    models.append(('Decison Tree', DecisionTreeClassifier()))
    models.append(('Guassian Naive Bayes', GaussianNB()))
    models.append(('SVM', SVC()))

    for name,model in models:
        
        # Fitting Naive Bayes to the Training set
        classifier = model
        classifier.fit(x_train, y_train)

        # Predicting the Test set results
        y_pred = classifier.predict(x_test)

        # Making the Confusion Matrix
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(y_test, y_pred)

        # Applying k-Fold Cross Validation
        from sklearn.model_selection import cross_val_score
        accuracies = cross_val_score(estimator = classifier, X = x_train, y = y_train, cv = 10)
        accuracies.mean()
        accuracies.std()
        
        # print()
        # print("For {0} The Performance result is: ".format(name))
        # print()

        #the performance of the classification model
        # print("the Accuracy is: "+ str((cm[0,0]+cm[1,1])/(cm[0,0]+cm[0,1]+cm[1,0]+cm[1,1])))
        recall = cm[1,1]/(cm[0,1]+cm[1,1])
        # print("Recall is : "+ str(recall))
        # print("False Positive rate: "+ str(cm[1,0]/(cm[0,0]+cm[1,0])))
        precision = cm[1,1]/(cm[1,0]+cm[1,1])
        # print("Precision is: "+ str(precision))
        # print("F-measure is: "+ str(2*((precision*recall)/(precision+recall))))
        from math import log
        # print("Entropy is: "+ str(-precision*log(precision)))

    #####################
    x_test= dataset_train[-1:,:]
    x_train= dataset_train[:-1,:]
    y_train = y

    from sklearn.model_selection import train_test_split

    #feature scaling
    from sklearn.preprocessing import StandardScaler
    sc_x = StandardScaler()
    x_train = sc_x.fit_transform(x_train)
    x_test = sc_x.transform(x_test)

    df2 = pd.DataFrame(x_train)

    models = []
    models.append(('Logistic Regression', LogisticRegression()))
    models.append(('Linear Discriminant Analysis', LinearDiscriminantAnalysis()))
    #models.append(('K-Nearest Neighbour ', KNeighborsClassifier()))
    models.append(('Decison Tree', DecisionTreeClassifier()))
    models.append(('Guassian Naive Bayes', GaussianNB()))
    models.append(('SVM', SVC()))
    # print("asd")

    output = []

    for name,model in models:


        classifier = model
        classifier.fit(x_train, y_train)

        # Predicting the Test set results
        y_pred = classifier.predict(x_test)
        output.append(y_pred[0])

    return most_frequent(output)

# # df = pd.
# test = [1, 15.3, "C", 8, "R", "WI", 1.5, 50000, "Programmer"]
# test_df = pd.DataFrame(test)
# print(recommend(test_df.T))
