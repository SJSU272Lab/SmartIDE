#Build: docker build -f Dockerfile -t smartide/node .

#Start Mongo
#docker run -d --name smartide-mongodb mongo 

#Link mongodb and node js 
#docker run -d -p 3000:3000 --link smartide-mongodb:mongodb smartide/node


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