# DL Lifecycle Data Management Framework front-end service

## Project setup
First of all project specific dependencies have to be installed:
```
npm install
```
After that project front-end service can be run in one of several ways: for production or for deployment (see below).

### Compile and hot-reload for development:
```
npm run serve
```

### Compile and minify for production:
```
npm run build
```

### .env files 

.env files has been set up and can be used to supply parameters to the front-end service. At the given moment the front-end service will accept only one parameter from .env file - `VUE_APP_SERVER_URL`. 
`VUE_APP_SERVER_URL` defines the address of a back-end service that gets accessed by a front-end service.   

<!-- 
### Lints and fixes files
```
npm run lint
```
 -->
