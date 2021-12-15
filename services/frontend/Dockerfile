FROM node:current-alpine as base

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@4.5.14 -g

COPY package.json .
COPY package-lock.json .
RUN npm install

FROM base as test

RUN npm install --include=dev

COPY . .

CMD ["npm", "run", "test:unit"]

FROM base as final

EXPOSE 8080

CMD ["npm", "run", "serve"]
