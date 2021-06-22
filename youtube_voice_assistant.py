# Prompt user for a channel name
# Get channel name from voice
# Prompt user for first video, latest video, channel
# Pull up Youtube accordingly

import speech_recognition
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_driver = webdriver.Chrome(PATH)
chrome_driver.get("https://youtube.com")

search_bar = chrome_driver.find_element_by_id("search")
search_bar.send_keys(channel_name)
search_button = chrome_driver.find_element_by_id("search-icon-legacy")
search_button.click()

try:
    channel_page = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.ID, "main-link"))
    )
    channel_page.click()
except:
    chrome_driver.quit()
    print("Sorry! Can't find channel name. Try again")

if page_name.lower() == "first video":
    pass

if page_name.lower() == "most recent video":
    pass

if page_name.lower() == "most popular video":
    pass