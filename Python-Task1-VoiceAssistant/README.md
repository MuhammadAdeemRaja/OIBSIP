# Python Voice Assistant

## Oasis Infobyte Internship — Task 1

### Developed By
Muhammad Adeem Raja

### Track
Python Programming

### Task
Task 1 — Voice Assistant




## Project Overview

This project is a Python-based Voice Assistant developed as part of the Oasis Infobyte Python Programming Internship.

The assistant accepts voice commands through a microphone, converts speech into text, processes the command, and responds using text-to-speech.




## Features

- Voice input using a microphone
- Responds to "Hello" and "Hi"
- Provides the current time
- Provides the current date
- Performs Google searches using voice commands
- Provides voice feedback using text-to-speech
- Handles unclear voice input gracefully
- Handles speech recognition service errors
- Allows the user to exit using "Goodbye", "Exit", "Quit", or "Stop"




## Technologies Used

- Python 3.10.11
- SpeechRecognition
- PyAudio
- pyttsx3
- datetime
- webbrowser


## Installation

Install the required Python libraries using:

'bash
pip install SpeechRecognition pyttsx3 PyAudio
'



## How to Run

Open the project folder in VS Code and run:

`bash
python voice_assistant.py
`

Make sure your computer has a working microphone and speakers.




## Example Commands

| Voice Command             | Action                 |
| ------------------------- | ---------------------- |
| Hello                     | Gives a greeting       |
| What is the time?         | Tells the current time |
| What is today's date?     | Tells the current date |
| Search Python programming | Opens Google search    |
| Goodbye                   | Exits the assistant    |



## Text-to-Speech

The project uses the `pyttsx3` library to provide spoken responses to the user.




## Error Handling

If the assistant cannot understand the user's speech, it asks the user to repeat the command.

The application also handles microphone timeout and speech recognition service errors without crashing.



## Privacy

The application uses the microphone only when listening for a voice command.

Speech recognition is performed using the speech recognition service used by the SpeechRecognition library. No personal information is intentionally stored by this project.



## Future Improvements

Possible future improvements include:

* Natural language understanding
* Weather information
* Voice-controlled reminders
* General knowledge questions
* Custom user commands
* Additional web services and APIs



## Internship

This project was developed as part of the Oasis Infobyte Python Programming Internship.


