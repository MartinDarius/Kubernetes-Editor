from python:slim

WORKDIR /app
COPY . /app

COPY requirements.txt .

RUN pip3 install --upgrade pip 
RUN pip3  install -r requirements.txt
RUN pip3 install python-dotenv
RUN pip3 install flask-bcrypt
RUN pip3 install flask-jwt-extended
RUN pip3 install flask-mongoengine
RUN pip3 install flask_restful
RUN pip3 install flask_cors

EXPOSE 5001 

ENV FLASK_APP=app.py

CMD flask run -h 0.0.0.0 -p 5001