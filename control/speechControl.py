'''
Created Date: Sunday, November 14th 2021
Author: Pawel Kremienowski
Author email: Kremienowski33@gmail.com
-----
Last Modified: Sun Nov 14 2021
Modified By: Pawel Kremienowski
'''


import speech_recognition
import pyttsx3
import zmq

recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 135)
# voice list may vary - choose english one
# check available voices by running:
# voices = engine.getProperty('voices')
# for voice in voices:
#     print("Voice:")
#     print(" - ID: %s" % voice.id)
#     print(" - Name: %s" % voice.name)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

ctx = zmq.Context()
sendSocket = ctx.socket(zmq.REQ)
sendSocket.connect("tcp://localhost:5555")


if __name__ == "__main__":
    try:
        while True:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic)
                audio = recognizer.listen(mic)

                print("Recognizing...")

                try:
                    data = recognizer.recognize_google(audio)
                    data = data.strip().lower()
                    print(f"You said: {data}")
                    sendSocket.send_string(f"{data}")
                    sendSocket.recv()
                except speech_recognition.RequestError:
                    print("Api unreachable")
                except speech_recognition.UnknownValueError:
                    print("Unable to recognize speech")
                except Exception:
                    print("Sth failed, restarting...")
                    recognizer = speech_recognition.Recognizer()
    except KeyboardInterrupt:
        print("CTRL+C pressed. Finishing")
        exit
