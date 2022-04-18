FROM python:3.8.2

RUN mkdir app
WORKDIR /app
COPY ./app/requirements.txt /app
RUN pip install -r requirements.txt
COPY app app
EXPOSE 8000
CMD [ "python", "api/app.py" ]