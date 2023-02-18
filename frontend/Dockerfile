FROM node:16 as build

WORKDIR /app/src

COPY ./package.json ./

RUN npm install

COPY ./ ./

RUN npm run build

# ---

FROM nginx:1.23-alpine-slim

RUN rm -rf /usr/share/nginx/html

COPY --from=build /app/src/dist /usr/share/nginx/html
