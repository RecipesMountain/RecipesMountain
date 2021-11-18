FROM node:current-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@4.5.14 -g

COPY package.json .
COPY package-lock.json .
RUN npm install

EXPOSE 8080

CMD ["npm", "run", "serve"]
