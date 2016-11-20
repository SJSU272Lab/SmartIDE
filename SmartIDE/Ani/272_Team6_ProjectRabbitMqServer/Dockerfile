#Pull the rabbit mq image
#docker pull rabbitmq
#Run it
#docker run -d --hostname smartide-rabbit --name ide-rabbit rabbitmq:3
#Run rabbit mq management console
#docker run -d --hostname smartide-rabbit --name some-rabbit -p 15672:15672 rabbitmq:3-management

#Build: docker build -f Dockerfile -t smartiderabbit/node .

FROM node:argon
RUN mkdir -p /usr/src/server/app
WORKDIR /usr/src/server/app

# Install app dependencies
COPY package.json /usr/src/server/app/
RUN npm install 

# Bundle app source
COPY . /usr/src/server/app

EXPOSE 8080
CMD [ "npm", "start" ]

#Start Mongo
#docker run -d --name smartide-mongodb mongo 

#Link rabbit, mongo and node 
#docker run -d -p 3000:3000 --link smartide-mongo:mongodb --link ide-rabbit smartiderabbit/node
