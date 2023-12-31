FROM python:3.8-slim-buster


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chmod +x run.sh
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /code
# USER appuser

CMD ["bash", "run.sh"]