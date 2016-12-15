FROM python:2.7.10
COPY . /qa
WORKDIR /qa
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 2666
CMD python QA.py