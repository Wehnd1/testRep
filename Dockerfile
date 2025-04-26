FROM python:3
WORKDIR /app
COPY avrg.py /app/avrg.py
CMD ["python", "/app/avrg.py"]
