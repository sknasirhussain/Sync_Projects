# OTP Email Sender

This Python script generates a 6-digit OTP (One-Time Password) and sends it to a specified email address using a Gmail account. It is a simple example of sending OTPs via email.

## Prerequisites

Before running the script, you need to have the following prerequisites:

- Python 3 installed on your system.
- A Gmail account to send emails from.
- Enable "Less secure apps" in your Gmail account settings, or use an "App Password" for authentication.

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/otp-email-sender.git
   ```

2. Navigate to the project directory:

   ```shell
   cd otp-email-sender
   ```

3. Install the required Python packages if not already installed:

   ```shell
   pip install smtplib
   ```

## Usage

1. In the file named `credentials.py` in the project directory enter the following content:

   ```python
   email = "your_email@gmail.com"      # Your Gmail email address
   password = "your_email_password"    # Your Gmail App Password
   ```

   Replace `"your_email@gmail.com"` with your Gmail email address and `"your_email_password"` with your Gmail App Password.

2. Run the script:

   ```shell
   python otp_sender.py
   ```

3. You will be prompted to enter the recipient's email address.

4. Check your recipient's email inbox for the OTP.

5. Enter the OTP when prompted.

6. The script will verify the OTP, and you will receive a verification message.

## Security Note

- Ensure you keep your `credentials.py` file and Gmail App Password secure. Do not share them with others.
