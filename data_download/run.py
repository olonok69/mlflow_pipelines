import argparse
import pandas as pd
import os
from datetime import datetime
import mlflow

def run(args):
    # name = "data_download_" +datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    df = pd.read_csv(args.data_url)
    path = os.path.join(args.data_path, "data.csv")
    df.to_csv(path, index=False)
    mlflow.log_params({"length_dataset": len(df)})
    mlflow.log_artifact(path, artifact_path="dataset")
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_url", type=str, required=True)
    parser.add_argument("--data_path", type=str, required=True)
    args = parser.parse_args()

    run(args)