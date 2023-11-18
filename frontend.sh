#!/bin/bash

# Przejście do katalogu frontend
cd frontend

# Sprawdzenie, czy npm jest zainstalowany
if ! command -v npm &> /dev/null
then
    echo "npm nie został znaleziony. Upewnij się, że Node.js i npm są zainstalowane."
    exit 1
fi

# Instalacja zależności, jeśli jest to potrzebne
echo "Instalowanie zależności..."
npm install

# Uruchomienie projektu
echo "Uruchamianie projektu React..."
npm start
