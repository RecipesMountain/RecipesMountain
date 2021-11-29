FROM jenkins/jenkins:alpine

USER root

RUN apk add --no-cache docker docker-compose python3 py3-pip shadow \
    && groupmod -g 998 docker \
    && addgroup jenkins docker \
    && apk del --purge shadow

USER jenkins
