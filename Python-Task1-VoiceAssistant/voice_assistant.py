import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


# change text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 170)


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")

        # Reduce background noise
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

            command = recognizer.recognize_google(audio)

            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I did not understand. Please repeat.")
            return ""

        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""


def handle_command(command):

    # Greeting
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    # Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    # Date
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}.")

    # Google search
    elif command.startswith("search"):
        search_query = command.replace("search", "", 1).strip()

        if search_query:
            speak(f"Searching for {search_query}.")

            url = (
                "https://www.google.com/search?q="
                + search_query.replace(" ", "+")
            )

            webbrowser.open(url)

        else:
            speak("Please tell me what you want to search for.")

    # Exit
    elif (
        "goodbye" in command
        or "exit" in command
        or "quit" in command
        or "stop" in command
    ):
        speak("Goodbye! Thank you for using the voice assistant.")
        return False

    # Unknown command
    else:
        speak(
            "I can help with greetings, time, date, "
            "and web searches. Please try again."
        )

    return True


def main():

    speak("Hello! I am your Python voice assistant.")

    speak(
        "You can say hello, ask for the time or date, "
        "or say search followed by a topic."
    )

    while True:

        command = listen()

        if command:
            if not handle_command(command):
                break


if __name__ == "__main__":
    main()