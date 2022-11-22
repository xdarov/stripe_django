FROM python

COPY . /home
WORKDIR /home/django_stripe

RUN apt-get update && \
        apt-get upgrade --assume-yes && \
        apt-get install --assume-yes screen && \
        apt-get install nano && \
        pip install --upgrade pip && \
        pip install -r ../requirements.txt &&\
        chmod +x /home/django_stripe/env.sh

CMD ["bash", "/home/django_stripe/env.sh"]