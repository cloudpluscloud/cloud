FROM node:latest

WORKDIR /app/frontend

COPY package.json package-lock.json ./

RUN npm install
RUN npm install react-bootstrap


COPY . ./
