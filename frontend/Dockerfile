FROM node:18-alpine AS build

WORKDIR /carfeeling

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM nginx:alpine

COPY --from=build /carfeeling/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]