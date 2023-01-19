FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED 1

# create and activate virtual environment
RUN apt-get update && apt-get install -y python3-venv
COPY create_venv.sh /app/
RUN chmod +x /app/create_venv.sh && /app/create_venv.sh
ENV PATH="/app/venv/bin:$PATH"

WORKDIR /app
COPY . /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000