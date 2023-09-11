FROM python:3-alpine3.9
WORKDIR /user/src/app
COPY './requirements.txt' .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "pyton", "app.py" ]