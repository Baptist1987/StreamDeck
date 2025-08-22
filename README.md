# Stream Deck für Windows

Ein leichtgewichtiges Stream Deck für Windows, umgesetzt mit FastAPI und einer einfachen HTML-Button-Oberfläche. Über den Browser (z.B. von einem Tablet im gleichen Netzwerk) lassen sich vordefinierte Aktionen am PC ausführen – wie Programme starten oder Fenster schließen.

## Features

- **Browser-basierte Bedienung**: Steuerung über jedes Gerät mit Webbrowser im lokalen Netzwerk
- **Responsive Design**: Optimiert für Desktop, Tablet und mobile Geräte
- **Vordefinierte Aktionen**: 
  - Programme starten (z.B. Notepad)
  - Fenster schließen (Alt+F4)
  - Alt+Tab Navigation
  - Enter und Tab Tasteneingaben
- **Moderne UI**: Dunkles Design mit professionellen Buttons und Animationen

## Projektstruktur

```
PythonProject1/
├── main.py              # FastAPI Server und Routing
├── remote_functions.py  # Implementierung der Button-Aktionen
├── main.html           # HTML Template für die Button-Oberfläche
└── static/
    └── main.css        # Styling für responsive UI
```

## Installation

### Voraussetzungen

- Python 3.7+
- pip

### Abhängigkeiten installieren

```bash
pip install fastapi uvicorn pyautogui
```

## Verwendung

### Server starten

```bash
python main.py
```

Anschließend ist die Web-Oberfläche unter `http://localhost:8000` erreichbar.

### Mit uvicorn starten (empfohlen)

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Die Anwendung ist dann von allen Geräten im lokalen Netzwerk unter `http://[PC-IP-ADRESSE]:8000` erreichbar.

## Button-Funktionen

| Button     | Funktion | Beschreibung |
|------------|----------|--------------|
| ping       | Test | Einfacher Test-Button |
| pong       | Test | Weiterer Test-Button |
| notepad    | Programm starten | Öffnet Notepad |
| puff       | Fenster schließen | Alt+F4 Tastenkombination |
| select     | Fenster wechseln | Alt+Tab Tastenkombination |
| bestätigen | Enter | Enter Taste |
| move>      | Navigation | Tab Taste |

## Anpassung

### Neue Buttons hinzufügen

1. **Funktion definieren** in `remote_functions.py`:
   ```python
   def rm9():
       # Ihre Aktion hier
       return "Erfolgsmeldung"
   ```

2. **Button registrieren** in `main.py`:
   ```python
   Buttons = {
       # ... bestehende Buttons
       "rm9": rmf.rm9
   }
   ```

3. **UI erweitern** in `main.html`:
   ```html
   <form method="get" action="action/rm9">
       <button class="btn">Neuer Button</button>
   </form>
   ```

### Verfügbare Aktionen

Das Projekt nutzt `pyautogui` für Tastatur- und Maus-Automatisierung. Beispiele:

```python
import pyautogui
import subprocess

# Tastenkombinationen
pyautogui.hotkey("ctrl", "c")  # Kopieren
pyautogui.hotkey("win", "r")   # Ausführen-Dialog

# Programme starten
subprocess.Popen(["notepad.exe"])
subprocess.Popen(["calc.exe"])

# Text eingeben
pyautogui.write("Hello World")

# Klicks
pyautogui.click(100, 100)
```

## Technische Details

- **Backend**: FastAPI für schnelle API-Entwicklung
- **Frontend**: Vanilla HTML/CSS mit modernem responsive Design
- **Automatisierung**: pyautogui für System-Interaktionen
- **Styling**: CSS Grid Layout mit Dark Theme
- **Responsive**: Unterstützt Desktop (3x2), Tablet (2x3) und Mobile (1x6) Layouts

## Sicherheitshinweise

- Die Anwendung sollte nur in vertrauenswürdigen Netzwerken betrieben werden
- Für Produktionsumgebungen sollte Authentifizierung hinzugefügt werden
- pyautogui kann alle Systemfunktionen steuern - Vorsicht bei neuen Funktionen

## Lizenz

Dieses Projekt steht zur freien Verfügung für private und kommerzielle Nutzung.