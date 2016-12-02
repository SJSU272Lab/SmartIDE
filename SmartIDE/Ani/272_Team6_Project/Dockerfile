#Build: docker build -f Dockerfile -t smartide/node .

FROM node:argon
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install

# Bundle app source
COPY . /usr/src/app

EXPOSE 3000
CMD [ "npm", "start" ]


#Once we have build this image follow the below steps 

#Run the dockerfile of 272_Team6_ProjectRabbitMqServer 

#Link container of the above run server, rabbit and node js 
#docker run -d -p 3000:3000 --link stupefied_carson(this is the name of the container in which the 272_Team6_ProjectRabbitMqServer server is running) --link ide-rabbit smartide/node