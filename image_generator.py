import os
import requests
from bs4 import BeautifulSoup
import re
from PIL import Image
from io import BytesIO
import pyttsx3
import speech_recognition as sr
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=7, phrase_time_limit=7)
        except Exception as e:
            speak("I couldn't hear you, please try again.")
            return "none"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        speak("I didn't catch that. Please say it again.")
        return "none"
    
    return query.lower()

def img_gen(num_images):  # Specify the number of images to download
    try:
        speak("Give me a prompt to generate images...")
        query = takecommand()

        # URL for Bing image search query
        search_url = f"https://www.bing.com/images/search?q={query.replace(' ', '+')}"

        # Send a request to the search page
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(search_url, headers=headers)

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all image containers
        image_elements = soup.find_all("a", {"class": "iusc"})

        # Directory to save images
        save_directory = "Images"
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # Function to get a unique filename
        def get_unique_filename(base_path, base_name, extension):
            counter = 1
            new_filename = f"{base_name}{extension}"
            while os.path.exists(os.path.join(base_path, new_filename)):
                new_filename = f"{base_name}_{counter}{extension}"
                counter += 1
            return new_filename

        # Initialize the image counter
        image_counter = 1
        image_paths = []

        # Loop through image elements and extract the URLs
        for image in image_elements:
            if image_counter > num_images:  # Stop when the specified number of images is reached
                break

            # Extract the image URL using regex
            m = re.search(r"murl\":\"(.*?)\"", str(image))
            if m:
                image_url = m.group(1)
                print(f"Downloading image: {image_url}")
                try:
                    # Fetch the image
                    img_response = requests.get(image_url)

                    # Open the image
                    img = Image.open(BytesIO(img_response.content))

                    # Generate a unique filename
                    image_name = get_unique_filename(save_directory, f"image_{image_counter}", ".png")

                    # Save the image with the unique filename
                    img_path = os.path.join(save_directory, image_name)
                    img.save(img_path)
                    image_paths.append(img_path)
                    print(f"Saved {image_name}")

                    # Increment the counter after saving the image
                    image_counter += 1

                except Exception as e:
                    print(f"Could not process image {image_url}: {e}")

        # Display images sequentially based on "next" command
        current_image_index = 0

        while current_image_index < len(image_paths):
            # Show the current image
            img = Image.open(image_paths[current_image_index])
            img.show()

            # Ask for user input to proceed
            speak("Say 'next' to view the next image or 'stop' to end.")
            command = takecommand()

            # Close the current image and move to the next
            if command == "next":
                img.close()  # Close the image viewer
                current_image_index += 1
            elif command == "stop":
                img.close()  # Close the current image
                speak("Stopping image display.")
                break
            else:
                speak("Sorry, I didn't understand. Please say 'next' or 'stop'.")

    except Exception as e:
        speak(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # You can specify how many images to download here
    img_gen(num_images=4)  # Change this to download a different number of images
