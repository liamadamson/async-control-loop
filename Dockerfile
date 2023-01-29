FROM python:3.11.1-slim-buster

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH = "${PYTHONPATH}:/code/src"

CMD ["python3", "-m", "async_control_loop"]