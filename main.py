# https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
# export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
import argparse
import pandas as pd
import mlflow
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(ROOT_DIR, "data")
os.makedirs(DATA_FOLDER, exist_ok=True)

all_steps = ["data_download", "data_cleaning", "training"]


def run(args):
    data_url = args.data_url
    steps = args.steps
    active_steps = steps.split(",")
    print(active_steps)

    if "data_download" in active_steps:
        # Download data
        _ = mlflow.run(
            f"data_download/",
            "main",
            parameters={
                "data_url": data_url,
                "data_path": DATA_FOLDER,
            },
            run_name= "data_download",
        )

    if "data_cleaning" in active_steps:
        # data cleaning
        _ = mlflow.run(f"data_cleaning/", "main", parameters={
                "data_path": DATA_FOLDER,
            },run_name= "data_cleaning",)

    if "training" in active_steps:
        # training
        _ = mlflow.run(f"training/", "main", parameters={
                "data_path": DATA_FOLDER,
            },run_name= "training",)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=str, required=True)
    parser.add_argument("--data_url", type=str, required=True)
    args = parser.parse_args()

    run(args)