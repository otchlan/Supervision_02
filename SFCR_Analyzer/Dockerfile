# Użyj oficjalnego obrazu Pythona jako obrazu bazowego
FROM python:3.9-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj plik wymagań i zainstaluj zależności
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztę kodu aplikacji do katalogu roboczego w kontenerze
COPY . .

# Ustaw zmienną środowiskową wskazującą na plik, który uruchamia aplikację
ENV FLASK_APP=app.py

# Uruchom aplikację Flask na porcie 5000
CMD ["python", "src/run.py", "--host=0.0.0.0", "--port=5000"]

