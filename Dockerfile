FROM python:3.8-alpine
apk --update add gcc build-base # required to build some of the following pip packages
RUN pip install --no-cache-dir kopf kubernetes requests # install our dependencies
ADD dagsync_controller.py / # copy our operator into the image
CMD kopf run /dagsync_controller.py # start our operator on container creation