FROM python:3.10-slim

WORKDIR /HIITTimer-flask

COPY . /HIITTimer-flask

RUN pip3 install flask
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=HIITTimer.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]