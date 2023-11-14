import PySimpleGUI as sg
import speech_recognition as sr
import subprocess
import os
import threading
import pyperclip

# Umwandeln in wav durch ffmpeg
def convert_ogg_to_wav(ogg_file_path):
    wav_file_path = ogg_file_path[:-4] + ".wav"
    subprocess.call(['ffmpeg', '-i', ogg_file_path, wav_file_path])
    os.remove(ogg_file_path)
    return wav_file_path

# Transkribieren und speichern der Ausgabe in einer Text-Datei
def transcribe_and_save(file_path, language):
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)
    text = r.recognize_google(audio, language=language)
    with open(file_path[:-4] + ".txt", "w") as f:
        f.write(text)
    return text

# GUI ----------------------------------------------------------------------------------------------------
sg.theme('Reddit')

layout = [
    [sg.Input(key='-FILE-', enable_events=True, visible=True, default_text='Bitte Pfad zur Audio-Datei angeben'),
     sg.FileBrowse('Datei auswählen', file_types=(("Audio-Dateien"),))],
    
    [sg.Text('Sprache:'), sg.Combo(['de-DE', 'en-us'], default_value='de-DE', key='-LANGUAGE-', size=(6, 1)),
     sg.Button('Transkribieren', key='-TRANSCRIBE-', expand_x=True)],
    
    [sg.Multiline(key='-OUTPUT-', size=(60,40), expand_x=True)],
    [sg.Button('Kopieren', key='-COPY-', expand_x=True)],
]

window = sg.Window('Audio-Transkription', layout)
# --------------------------------------------------------------------------------------------------------

# Event-Loop für PySimpleGUI
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    # Auswahl der Audio-Datei
    if event == '-FILE-':
        file_path = values['-FILE-']
        
    # Kopieren der Transkription in die Zwischenablage
    if event == '-COPY-':
        pyperclip.copy(values['-OUTPUT-'])
        
    # Transkription starten
    if event == '-TRANSCRIBE-':
        # überprüfen ob es eine wav-Datei ist, ansonsten umwandeln
        if not file_path.endswith(".wav"):
            file_path = convert_ogg_to_wav(file_path)
        
        # Sprache auswählen
        t_language = values['-LANGUAGE-']
        
        # Threading für parallele Ausführung
        thread = threading.Thread(target=lambda: window['-OUTPUT-'].update(transcribe_and_save(file_path, language = t_language)))
        thread.start()
    
window.close()
