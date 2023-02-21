FROM python:3.9.6-alpine
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /home/app/backend
ADD . .
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev musl-dev libxml2-dev libxslt-dev libffi-dev
RUN apk add make automake gcc g++ subversion python3-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./entrypoint.sh /home/app/backend/entrypoint.sh
RUN ["chmod", "+x", "/home/app/backend/entrypoint.sh"]

COPY .env.example .env
# run entrypoint.sh
ENTRYPOINT ["/home/app/backend/entrypoint.sh"]