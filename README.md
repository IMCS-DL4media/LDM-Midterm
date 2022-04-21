# DL4media_framework

A framework for capturing all relevant events and artefacts during the DL training process, 
as well as a web interface for inspecting them.

The most important features of our framework are abilities:
 - to create a new experiment - a project
 - to add training data sets (training data set, test data set) to this project
 - to record the progress of an ongoing experiment (create log entries and save experiment run metadata)
 - to save files used in the experiment
 
## How to run with docker-compose:
 
 Probably, the easiest way to run LDM framework locally is to use docker-compose and provided docker-compose.yml file.
 To do that you need to clone this repo and have docker and docker-compose installed on your machine. After that you just navigate to the root of the cloned repo and from there execute the following comands:
 
``` bash
docker-compose build
docker-compose up
```
If the execution of above mentioned commands is successful - the framework is ready.  You should now be able to point your browser to http://localhost:8000 and see the system in action.

## How to run without docker:
 It is possible to run LDM framework locally without using docker and docker-compose as well. 
 LDM framework consists of 3 parts: Mongo DB service, back-end service and front-end service. As a consequnce to start the framework without docker you just need to start these 3 services "manually". Mongo DB service needs to be started in a usual way. Instructions on how to start back-end and front-end services can be found in the appropriate folders [front-end](./front_end_sbadmin/README.md) and [back-end](./flask_back_end/README.md). 
 
## Tutorial:
 
 [LDM framework quick start](./docs/Tutorial/README.md)
