# Sync_Projects

This repository contains a collection of projects that cover various domains and functionalities. Each project is designed to serve a specific purpose, and you can explore them individually.

## Projects

1. **Alarm_clock**
   - Description: This is a simple alarm clock application developed using Python's tkinter for the graphical user interface, PIL (Python Imaging Library) for image handling, and pygame for audio playback. It allows you to set a specific time for the alarm to go off and play an alarm sound.
   
   - Features
        - Set the alarm time in hours, minutes, seconds, and AM/PM.
        - Activate and deactivate the alarm.
        - Play an alarm sound when the alarm time is reached.
      
2. **ChatBot**
   - Description: This Python code implements a simple chat bot that responds to user input based on the probability of recognizing words and keywords in the user's message. The bot selects the best response from a predefined set of responses.
   - Usage: 
        1. Ensure you have Python installed on your system.

        2. Run the script in a Python environment.

        ```bash
        python chat_bot.py
        ```

        3. The bot will continuously prompt for user input and provide responses based on the recognition probabilities.


3. **OTP_Verification**
   - Description: This Python script generates a 6-digit OTP (One-Time Password) and sends it to a specified email address using a Gmail account. It is a simple example of sending OTPs via email.
   - Usage: 
        1. In the file named `credentials.py` in the project directory enter the following content:

        ```python
        email = "your_email@gmail.com"      # Your Gmail email address
        password = "your_email_password"    # Your Gmail App Password
        ```

        Replace `"your_email@gmail.com"` with your Gmail email address and `"your_email_password"` with your Gmail App Password.

        2. Run the script:

        ```shell
        python main.py
        ```

        3. You will be prompted to enter the recipient's email address.

        4. Check your recipient's email inbox for the OTP.

        5. Enter the OTP when prompted.

        6. The script will verify the OTP, and you will receive a verification message.

4. **URL_Shortener**

   - Description: This is a simple GUI-based URL shortener application built in Python using the Tkinter library and the PyShorteners library. It allows users to enter a long URL and get a shortened URL using the TinyURL service.

   - Features: 
        - User-friendly graphical interface.
        - Quickly shortens URLs using the TinyURL service.
        - Easy to use - just input the URL and click the "Submit" button.

## Getting Started

To get started with any of the projects, navigate to the respective project folder and follow the instructions provided in their individual README files.


## Issues and Contributions

If you encounter any issues with any of the projects or would like to contribute improvements, please feel free to open an issue or submit a pull request. Your contributions are greatly appreciated!

Happy coding!
