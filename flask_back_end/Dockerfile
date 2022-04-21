FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

ENV TZ=Europe/Riga
RUN date
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update && apt install
RUN date


COPY ./static/ /flask_app/static/

#COPY ./app.py /flask_app/
COPY ./run.py /flask_app/
COPY ./routes.py /flask_app/
COPY ./global_vars.py /flask_app/
COPY ./__init__.py /flask_app/

COPY ./requirements.txt /flask_app/

RUN mkdir ./uploads/

WORKDIR /flask_app
RUN pip install -r requirements.txt

ARG dck_build_arg_mongo_uri
ENV MONGO_URI=$dck_build_arg_mongo_uri

#ENTRYPOINT ["python"]
#CMD ["app.py"]
#CMD ["run.py", "$MONGO_URI"]
CMD python run.py $MONGO_URI
