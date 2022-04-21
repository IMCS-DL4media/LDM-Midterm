# DL Lifecycle Data Management Framework back-end service

## Installation
Before running back-end locally (not inside docker container) you need to install python tools (python, pip, ... ) and project specific python dependencies. Project specific dependencies are stored in the requirements.txt file. To install them run the following command:  

``` bash
pip install -r requirements.txt
```

## Runnning
It is possible to pass Mongo DB URI as a parameter to run.py. You pass it as a command line argument. In case if it is passed, backend will connect to a DB, located at a passed URI. Otherwise (if no parameters has been passed) a default Mongo URI of "mongodb://localhost:27017/logging_db" is used.

To run back-end with a default Mongo URI:
``` bash
python run.py
```

To run back-end with a user supplied Mongo URI (for example):
``` bash
python run.py mongodb://localhost:27017/logging_db_paper
```