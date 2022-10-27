FROM python:3.8

ENV PYTHONUNBUFFERED 1

EXPOSE 8000 

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt /app/

COPY . /app/ 

RUN pip install -r requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0" , "--reload", "--port", "8000", "main:app"]
