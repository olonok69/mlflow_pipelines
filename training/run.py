import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import mlflow

def run(args):
    mlflow.sklearn.autolog()
    titanic_data = pd.read_csv(os.path.join(args.data_path, "augmented_data.csv"))
    y_data = titanic_data['Survived']
    x_data = titanic_data.drop('Survived', axis = 1)
    x_training_data, x_test_data, y_training_data, y_test_data = train_test_split(x_data, y_data, test_size = 0.3)
    # create model
    model = LogisticRegression()
    model.fit(x_training_data, y_training_data)
    predictions = model.predict(x_test_data)
    print(classification_report(y_test_data, predictions))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True)
    args = parser.parse_args()

    run(args)