FROM python

ADD requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD consumer.py consumer.py

ENTRYPOINT ["python", "consumer.py"]

