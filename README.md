# MLFLOW Projects
### Documentation

https://mlflow.org/docs/latest/projects.html

# mlflow.run()
https://mlflow.org/docs/latest/python_api/mlflow.projects.html#mlflow.projects.run

you can download the titanic file from https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

# MLFLOW
if you have already a tracking server set before run the variable  MLFLOW_TRACKING_URI 
```bash
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
```
In my case I have MLflow infrastructure running in docker

![alt text](images/mlflow.png)



# Project Organization

![alt text](images/project.png)

# Run the pipeline

```python
mlflow run . -P steps="data_download,data_cleaning,training" -P data_url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv" --experiment-name pipelines
```