FROM python:3.8-alpine
LABEL maintainer="Jose Camarena"

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]