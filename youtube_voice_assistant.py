# Prompt user for a channel name
# Get channel name from voice
# Prompt user for channel, trending, latest video of channel
# Pull up Youtube accordingly

import speech_recognition
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def main():
    youtube_recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as user_voice:

        valid_command = False

        while not valid_command:
            while True:
                try:
                    print("Do you want to see what's trending or a channel?")
                    print("Say 'trending' or 'channel'")
                    trending_or_channel_audio = youtube_recognizer.listen(user_voice)
                    trending_or_channel_name = youtube_recognizer.recognize_google(
                        trending_or_channel_audio
                    )
                    print(trending_or_channel_name)
                    break
                except:
                    print("Couldn't detect your voice. Try again")

            if trending_or_channel_name.lower() == "channel":
                while True:
                    try:
                        print("What Youtube Channel name do you want?")
                        channel_name_audio = youtube_recognizer.listen(user_voice)
                        channel_name = youtube_recognizer.recognize_google(
                            channel_name_audio
                        )
                        print(channel_name)
                        break
                    except:
                        print("Couldn't detect your voice. Try again")

                page_or_video_command = False

                while not page_or_video_command:
                    while True:
                        try:
                            print(
                                "Do you want their channel page or their most recent video?"
                            )
                            print("Say 'channel page' or 'most recent video'")
                            page_name_audio = youtube_recognizer.listen(user_voice)
                            page_name = youtube_recognizer.recognize_google(
                                page_name_audio
                            )

                            if (
                                page_name.lower() == "channel page"
                                or page_name.lower() == "most recent video"
                            ):
                                page_or_video_command = True
                                valid_command = True
                                print(page_name)
                            else:
                                print(
                                    "Not a valid command. Channel page or most recent video?"
                                )

                            break
                        except:
                            print("Couldn't detect your voice. Try again")

            elif trending_or_channel_name.lower() == "trending":
                valid_command = True
                pass

            else:
                print("Not a valid command. Try again")

    options = Options()
    options.add_experimental_option("detach", True)
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    chrome_driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)

    chrome_driver.get("https://youtube.com")

    if trending_or_channel_name.lower() == "channel":

        search_bar = chrome_driver.find_element_by_id("search")
        search_bar.send_keys(channel_name)
        search_button = chrome_driver.find_element_by_id("search-icon-legacy")
        search_button.click()

        if page_name.lower() == "channel page":
            try:
                channel_page = WebDriverWait(chrome_driver, 10).until(
                    EC.presence_of_element_located((By.ID, "main-link"))
                )
                channel_page.click()
            except:
                print(
                    "Sorry! Can't find channel name. Here are the search results for "
                    + channel_name
                )

        else:
            try:
                first_video = WebDriverWait(chrome_driver, 10).until(
                    EC.presence_of_element_located((By.ID, "video-title"))
                )
                first_video.click()
            except:
                print("Sorry could not pull up first video")
    else:
        explore_button = chrome_driver.find_element_by_xpath("//*[@title='Explore']")
        explore_button.click()

        try:
            trending_page = WebDriverWait(chrome_driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@href='/feed/trending?bp=6gQJRkVleHBsb3Jl']")
                )
            )
            trending_page.click()

        except:
            print("Error. Could not pull up trending page")


main()
