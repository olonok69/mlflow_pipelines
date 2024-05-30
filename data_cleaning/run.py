import pandas as pd
import os
import argparse
from utils import convert_categorical
import mlflow


def run(args):

    def impute_missing_age(columns):
        age = columns[0]
        passenger_class = columns[1]
        if pd.isnull(age):
            if(passenger_class == 1):
                return df[df['Pclass'] == 1]['Age'].mean()
            elif(passenger_class == 2):
                return df[df['Pclass'] == 2]['Age'].mean()
            elif(passenger_class == 3):
                return df[df['Pclass'] == 3]['Age'].mean()
        else:
            return age

    df = pd.read_csv(os.path.join(args.data_path, "data.csv"))
    df['Age'] = df[['Age', 'Pclass']].apply(impute_missing_age, axis = 1)
    #remove cabin
    df.drop('Cabin', axis=1, inplace = True)
    df.dropna(inplace=True)
    df.to_csv(os.path.join(args.data_path, "clean_data.csv"))

    df = convert_categorical(df)
    # Removing Unnecessary Columns From The Data Set
    df.drop(['Name', 'Ticket', 'Sex', 'Embarked'], axis = 1, inplace = True)
    path = os.path.join(args.data_path, "augmented_data.csv")
    df.to_csv(path, index=False)
    mlflow.log_params({"length_dataset": len(df)})
    mlflow.log_artifact(path, artifact_path="dataset")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--data_path", type=str, required=True)
    args = parser.parse_args()
    run(args)
