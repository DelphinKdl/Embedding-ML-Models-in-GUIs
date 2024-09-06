FROM ubuntu:latest

WORKDIR /usr/app/src/

ARG LANG="en_US.UTF-8"

# Install  packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    locales \
    python3-pip \
    python3-venv \
    python3-yaml \
    rsyslog \
    systemd \
    systemd-cron \
    sudo && apt-get clean


RUN python3 -m venv GUIenv

COPY requirements.txt ./

RUN . ./GUIenv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

COPY ./ ./


ENV PATH="/usr/app/src/GUIenv/bin:$PATH"

# Image purpose
CMD ["streamlit", "run", "1_Home.py"]

LABEL maintainer="Delphin K. <delphin.kaduli@gmail.com>"