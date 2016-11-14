FROM ubuntu:14.04
MAINTAINER KHWu <bondk818@gmail.com>
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-all python-pip 
ADD ./GoogleAPI/requirements.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt
ADD ./GoogleAPI /opt/GoogleAPI/
WORKDIR /opt/GoogleAPI/
EXPOSE 5000
CMD ["python", "googleapi.py"]
