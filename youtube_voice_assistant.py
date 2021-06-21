# Prompt user for a channel name
# Get channel name from voice
# Prompt user for first video, latest video, channel
# Pull up Youtube accordingly

import speech_recognition

youtube_recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as user_voice:
    while True:
        try:
            print("What Youtube Channel name do you want?")
            channel_name_audio = youtube_recognizer.listen(user_voice)
            channel_name = youtube_recognizer.recognize_google(channel_name_audio)
            print(channel_name)
            break
        except:
            print("Couldn't detect your voice. Try again")
        
    while True:
        try:
            print("Do you want the channel page, their first video, or their most recent video?")
            page_name_audio = youtube_recognizer.listen(user_voice)
            page_name = youtube_recognizer.recognize_google(page_name_audio)
            print(page_name)
            break
        except:
            print("Couldn't detect your voice. Try again")
