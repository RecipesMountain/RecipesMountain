FROM node:lts-alpine as base

WORKDIR /app

ENV VUE_APP_ENV=production

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM base as test

RUN npm ci --include=dev

COPY . .

CMD ["npm", "run", "test:unit"]

FROM nginx:stable-alpine as final

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=base /app/dist /usr/share/nginx/html

EXPOSE 8080
