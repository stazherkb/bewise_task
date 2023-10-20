FROM python:3.11

# WORKDIR /app

COPY main.py .
COPY requirements.txt .
COPY server/ server/
# COPY venv311/ venv311/

RUN pip install -r requirements.txt --no-cache-dir
# RUN ./venv311/Scripts/activate

CMD ["python", "main.py"]
# CMD ["python", "main.py"]