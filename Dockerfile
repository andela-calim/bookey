FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /bookey
WORKDIR /bookey
ADD requirements.txt /bookey/
RUN pip install -r requirements.txt
ADD . /bookey/
