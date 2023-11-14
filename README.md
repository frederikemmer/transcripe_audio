# Audio-Transkriptionstool

Dieses Tool bietet eine grafische Benutzeroberfläche (GUI), um Audio-Dateien in Text umzuwandeln. Es verwendet PySimpleGUI für die GUI, speech_recognition für die Transkription und ffmpeg für die Konvertierung von Audioformaten.

## Funktionen

- Konvertierung von OGG-Audiodateien in das WAV-Format.
- Transkription von WAV-Audiodateien in Text.
- Kopieren des transkribierten Textes in die Zwischenablage.
- Einfache und benutzerfreundliche GUI.

## Voraussetzungen

Bevor Sie dieses Tool verwenden können, stellen Sie sicher, dass folgende Bibliotheken installiert sind:

- PySimpleGUI
- speech_recognition
- pyperclip

Außerdem ist `ffmpeg` erforderlich, um Audio-Dateien zu konvertieren.

## Installation

Zum Installieren der benötigten Python-Bibliotheken führen Sie folgenden Befehl aus:

```bash
pip install PySimpleGUI speech_recognition pyperclip
```
## Verwendung
Starten Sie das Programm, indem Sie das Skript in Python ausführen. Wählen Sie über die GUI eine Audiodatei aus und klicken Sie auf "Transkribieren", um den Text zu erhalten.

## Lizenz
Dieses Tool ist freie Software und kann unter den Bedingungen der MIT-Lizenz weiterverbreitet und/oder modifiziert werden.

## Autor
Frederik Emmer