FROM python:2.7.10
COPY . /control
WORKDIR /control
RUN pip install -r requirements.txt
EXPOSE 1314
CMD python controller.py