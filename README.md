# Leistungskurve-I :chart_with_upwards_trend:
> [!NOTE]
>_Um diese Schritte in VS Code durchzuführen, müssen Sie zunächst sicherstellen, dass Sie Python und VS Code installiert haben._
README.md
# Anleitung zur Verwendung des Codes
**Dieses Repository enthält Code, der entwickelt wurde, um Daten aus einer CSV-Datei zu lesen, sie zu sortieren und sie dann in einem Plot darzustellen.**

## Vorbereitung der virtuellen Umgebung
1. Navigieren Sie in Ihrem Terminal in das Hauptverzeichnis des Projekts.
2. Führen Sie den Befehl `python -m venv venv` aus, um eine neue virtuelle Umgebung zu erstellen.
3. Aktivieren Sie die virtuelle Umgebung mit dem Befehl, der Ihrem Betriebssystem entspricht:
   - Für Windows: `\venv\Scripts\activate`
   - Für andere Betriebssysteme  (macOs,Linux) : `source venv/bin/activate`
  
> [!CAUTION]
> Falls Probleme auftreten, stellen Sie sicher, dass die Ausführungspolitik für Skripte in Ihrer Umgebung auf "Unrestricted" gesetzt ist, indem Sie `Set-ExecutionPolicy -ExecutionPolicy Unrestricted` ausführen. Beachten Sie jedoch, dass dies aus Sicherheitsgründen gemacht wird und dass Sie die möglichen Risiken verstehen sollten.

## Daten verarbeiten und visualisieren
Der Code in diesem Repository ermöglicht es, Daten aus einer CSV-Datei zu lesen, sie zu sortieren und dann in einem Plot darzustellen. Folgen Sie den untenstehenden Schritten, um dies zu erreichen:

1. Führen Sie den `load_data.py` Skript aus, um die Daten aus der `activity.csv` Datei zu laden und in einer Liste zu speichern.
2. Führen Sie den `bubble_sort.py` Skript aus, um die Daten in der Liste mittels des Bubble-Sort Algorithmus zu sortieren.
3. Führen Sie den `main.py` Skript aus, um die sortierten Daten in einem Plot darzustellen.
4. Der erzeugte Plot wird automatisch angezeigt. Um ihn als PNG-Datei zu speichern, folgen Sie den Anweisungen im Skript.

## Dateistruktur

- `activity.csv`: Die CSV-Datei, die die Aktivitätsdaten enthält.
- `load_data.py`: Das Skript zum Laden der Daten aus der CSV-Datei.
- `bubble_sort.py`: Das Skript zum Sortieren der Daten mittels des Bubble-Sort Algorithmus.
- `main.py`: Das Skript zum Darstellen der sortierten Daten in einem Plot.
- `venv/`: Das Verzeichnis der virtuellen Umgebung.
- `README.md`: Diese Datei, die Anleitungen zur Verwendung des Codes enthält.
