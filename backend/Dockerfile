FROM python:3.9-slim

WORKDIR /backend

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

ENTRYPOINT ["uvicorn", "run:app", "--port=8080", "--host=0.0.0.0"]