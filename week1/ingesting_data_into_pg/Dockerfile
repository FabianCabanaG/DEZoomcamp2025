FROM python:3.9

RUN pip install pandas
WORKDIR /app/pipelines

COPY pipeline.py pipeline_inside.py

# ENTRYPOINT ["bash"] -- bash default on run
ENTRYPOINT [ "python","pipeline_inside.py" ]