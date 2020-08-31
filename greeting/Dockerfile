FROM node:lts-alpine

WORKDIR /usr/src/apps/greeting

COPY package*.json ./

RUN npm install 

COPY hello.js .

EXPOSE 8181
CMD ["npm", "run", "serve"]
