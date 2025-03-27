FROM node:lts-alpine

ARG HOST

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV VITE_SERVER_URL=http://${HOST}:8000
ENV VITE_WS=ws://${HOST}:8000  

RUN npm run build

EXPOSE 80
CMD [ "http-server", "dist", "-p", "80" ]