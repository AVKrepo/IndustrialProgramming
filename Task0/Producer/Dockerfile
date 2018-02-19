FROM python

ADD requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD producer.py producer.py

ENTRYPOINT ["python", "producer.py"]

