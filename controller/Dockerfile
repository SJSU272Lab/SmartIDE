FROM python:2.7.10
COPY . /control
WORKDIR /control
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python controller.py