from gtts import gTTS
from pydub import AudioSegment
from playsound import playsound
import os
import time

def speak(text):
    tts = gTTS(text, lang='es')
    tts.save("/home/danielnezcano/.gemcli-py/audio.mp3")

    # Carga el audio
    audio = AudioSegment.from_mp3("/home/danielnezcano/.gemcli-py/audio.mp3")

    # Aumenta la velocidad en un 20% (ajusta el valor según tus necesidades)
    audio_acelerado = audio.speedup(playback_speed=1.3)

    # Guarda el audio acelerado
    audio_acelerado.export("/home/danielnezcano/.gemcli-py/audio_acelerado.mp3", format="mp3") 

    # Guarda el PID del proceso actual
    pid_actual = os.getpid()

    # Inicia la reproducción en segundo plano
    playsound("/home/danielnezcano/.gemcli-py/audio_acelerado.mp3", block=False)


