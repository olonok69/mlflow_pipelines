FROM jupyter/pyspark-notebook

RUN pip3 install mlflow  numpy scipy pandas scikit-learn cloudpickle faker tensorflow==2.12.0 keras requests click pip pyspark

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/

WORKDIR /work

COPY *.py .

