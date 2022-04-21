FROM node:lts-alpine

# RUN date

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

RUN npm config set strict-ssl false
RUN npm config set unsafe-perm true

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

ARG dck_build_arg_server_url

ENV VUE_APP_SERVER_URL=$dck_build_arg_server_url

# build app for production with minification
#RUN npm run build


EXPOSE 8000
ENV PORT=8000
CMD [ "npm", "run" , "serve" ]
