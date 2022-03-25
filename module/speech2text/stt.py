from ast import Str
from email.mime import audio
import speech_recognition as sr

class stt_api():
    def __init__(self) -> None:
        self.recognizer= sr.Recognizer()
    
    def speech_to_text(self, audio_file_dir):
        audio_file = sr.AudioFile(audio_file_dir)
        with audio_file as source:
            audio_file = self.recognizer.record(source, duration = 30.0)
            result = self.recognizer.recognize_google(audio_data=audio_file)
        return result



if __name__ == '__main__':
    stt_object=stt_api()
    audio_file = sr.AudioFile('./data/testaudio.wav')
    print(type(audio_file))
    with audio_file as source:
        audio_file = stt_object.recognizer.record(source, duration = 30.0)
        result = stt_object.recognizer.recognize_google(audio_data=audio_file)
    print(type(audio_file))
    print(result)
