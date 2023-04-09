# OpenAI-Waifu-Assistant

[![vtuberlogo.png](https://i.postimg.cc/pT87KyBw/vtuberlogo.png)](https://postimg.cc/yg1vH1tj)

Hi, I made this AI to help you with your tasks. It can listen to you through the microphone and respond accordingly. I created it using an OpenAI model in Python, along with a JSON file for configuration. In this JSON file, you can adjust your OpenAI API key and the language of the voices, which uses pyttsx3. If you want to change the language of the voices, simply adjust the number in the "config" section of the JSON file - 0 for Spanish, 1 for English, and there are more voices available (I think from 0 to 3), so you can choose the one you like the most. I'm currently working on making it compatible with Twitch and YouTube. You can choose to communicate with it via text or voice, and also adjust the personality in the JSON file for the way you want it to respond.

Requeriments
------------------
openai
speech_recognition
pyttsx3
json


[![vtuber.png](https://i.postimg.cc/xTKf91DF/vtuber.png)](https://postimg.cc/rKwXJcpS)


Installation
----------------
Install Python on your computer if you haven't already. You can download it from the official website: https://www.python.org/downloads/

Open the command line on your operating system (cmd on Windows, Terminal on macOS) and make sure you have pip, the Python package manager, installed. To check if you have pip installed, type the following command and press Enter:

css
Copy code
pip --version
If pip is already installed, it will show the current version. If not, you'll need to install it. Follow the instructions on this website to do so: 

https://pip.pypa.io/en/stable/installing/

Install the required packages. To do this, type the following commands one by one and press Enter after each one:

pip install openai
pip install speechrecognition
pip install pyttsx3

Download the config.json file and save it in the same folder as the Python file you provided. This file contains the necessary configuration information for the code.

Open the Python file in your favorite code editor (such as Visual Studio Code, PyCharm, etc.) and run it. To do this, you can click the "Run" button or press the F5 key.

The code will ask you to select the mode of interaction with Sayaka. Type "text" if you want to interact with her through text, or "voice" if you prefer to use your voice.

If you have selected the text mode, simply type your questions and wait for Sayaka to respond. If you have selected the voice mode, make sure you have a microphone connected to your computer and speak clearly so that Sayaka can understand you.

To switch back to text or voice mode, simply say or type "switch to text mode" or "switch to voice mode", respectively.

That's it! With these steps you should be able to install and run the code without any problems.
