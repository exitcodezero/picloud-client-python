FROM python:2.7.10
ADD . /src/
RUN cd /src && pip install ipython && pip install -r requirements.txt && pip install .
WORKDIR /src
