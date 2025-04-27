from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

import joblib
import yaml
import pandas as pd

def preparar_dado_predict(id):
    # load base de dados
    df_train = pd.read_csv('./dataset/challenge_train.csv', sep = ';')
    item = df_train[df_train['id'] == int(id)]

    numerical_features = ['mana', 'attack', 'health']
    categorical_features = ['type', 'god', 'strategy']

    numerical_data = item[numerical_features]
    categorical_data = item[categorical_features]

    # load OneHotEncoder
    enc = joblib.load("./models/OneHotEncoder_model.pkl") 

    # preparando dado para predição
    X = pd.concat([numerical_data, pd.DataFrame(enc.transform(categorical_data).toarray(), columns=enc.get_feature_names_out(categorical_features))],
              axis = 1)
    return X

def preparar_dado_trainamento():
    # load base de dados
    df_train = pd.read_csv('./dataset/challenge_train.csv', sep = ';')

    # Read YAML file
    with open("./app/conf/conf.yaml", 'r') as stream:
        conf_features = yaml.safe_load(stream)
    print(conf_features)

    numerical_features = conf_features['numerical_features']
    categorical_features = conf_features['categorical_features']
    target = conf_features['target']

    numerical_data = df_train[numerical_features]
    categorical_data = df_train[categorical_features]
    y = df_train[target[0]]

    # load OneHotEncoder
    enc = joblib.load("./models/OneHotEncoder_model.pkl") 

    # preparando dado para predição
    X = pd.concat([numerical_data, pd.DataFrame(enc.transform(categorical_data).toarray(), columns=enc.get_feature_names_out(categorical_features))],
              axis = 1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    return X_train, X_test, y_train, y_test