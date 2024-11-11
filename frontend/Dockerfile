FROM node:18-alpine AS build

ENV TESTE=$TESTE

WORKDIR /carfeeling

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM nginx:alpine

COPY --from=build /carfeeling/dist /usr/share/nginx/html

EXPOSE 8080

CMD ["/bin/sh", "-c", "sed -i 's/listen  .*/listen 8080;/g' /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'"]
