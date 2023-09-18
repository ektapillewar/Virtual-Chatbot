# Virtual-Chatbot

This is a simple graphical user interface (GUI) for a chatbot. The chatbot responds to user input with predefined responses and can also speak the responses using text-to-speech (TTS) technology.

## Requirements

Before running the application, make sure you have the following requirements installed:

- Python (version 3.6 or higher)
- Tkinter (Python's standard GUI library)
- NLTK (Natural Language Toolkit)
- gTTS (Google Text-to-Speech)
- pygame (for playing audio)


You can save this content to a file named `README.md` in your project directory. Update the content as needed to provide more details about your project and its usage.


## Usage

1. Clone this repository to your local machine.

2. Ensure you have the required background image (e.g., "background_image.png") in the same directory as the script.

3. Run the script `vc.py` using Python:


4. The GUI window will appear with a chat interface and an input box. You can interact with the chatbot as follows:

   - Type a message in the input box and press "Enter" or click the "Send" button to send your message to the chatbot.
   - The chatbot will respond to your messages with predefined responses.
   - If your system has audio capabilities enabled, the chatbot will also speak its responses, providing an engaging user experience.

5. Feel free to have a conversation with the chatbot, ask questions, or simply greet it.

6. To exit the application, you can type "quit" or "bye" in the input box, and the chatbot will bid you goodbye.

## Features

- **Interactive Chatbot**: The GUI allows you to have interactive conversations with the chatbot.

- **Text-to-Speech**: The chatbot can speak its responses using gTTS, enhancing the user experience.

- **Customizable Responses**: You can easily customize the chatbot's responses by modifying the `bot_responses` list in the `vc.py` script. Add your own response patterns and replies to make the chatbot more engaging and informative.

- **User-Friendly Interface**: The GUI provides a user-friendly chat interface with a clean design.

## Customization

You can customize the chatbot's responses by modifying the `bot_responses` list in the `vc.py` script. Each response pattern is associated with a list of possible replies.

```python
bot_responses = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    # Add more response patterns and replies here
]



