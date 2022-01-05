FROM python:3.10.1-buster

# copy files
ADD . /

# install pip dependencies
RUN pip install kafka-python

RUN chmod +x /entrypoint.sh

# run
CMD [ "/entrypoint.sh" ]