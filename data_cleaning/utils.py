import pandas as pd

def convert_categorical(df):
    sex_data = pd.get_dummies(df['Sex'], drop_first = True)
    embarked_data = pd.get_dummies(df['Embarked'], drop_first = True)
    titanic_data = pd.concat([df, sex_data, embarked_data], axis = 1)
    return titanic_data

