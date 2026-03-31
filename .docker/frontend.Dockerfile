FROM node:lts-alpine as base
WORKDIR /app
COPY apps/frontend/package*.json ./
RUN npm install
COPY . .

FROM base as development
EXPOSE 8080
CMD ["npm", "run", "dev"]

FROM base as build-stage
RUN npm run build

FROM nginx:stable-alpine as production
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]