# WhatsApp Automation Project

This project demonstrates how to send messages, images, or files to WhatsApp numbers using Python and the `pywhatkit` library.

## Requirements

Before using this project, you need to install the required Python libraries. You can install them using pip:

````bash
pip install pywhatkit

````

## How to Use
Set up WhatsApp Web: Open WhatsApp Web in your browser and scan the QR code with your phone to log in. Make sure you are logged into your WhatsApp Web account.

Run the Script: Execute the Python script and follow the prompts to send messages, images, or files. The script will ask you to input the recipient's phone number (with the country code), the content (message, image path, or file path), and any additional details (e.g., image caption).

Example of running the script:
    `python send_whatsapp.py`

Choose the Action: You will be prompted to choose one of the following actions:

    *Send a message.    `send_message("+1234567890", "Hello!")`
    *Send an image.     `send_image("+1234567890", "path/to/image.jpg", "Check this out!")`
    *Send a file.       `send_file("+1234567890", "path/to/document.pdf")`

Enter the Recipient's Phone Number: The script will prompt you to enter the recipient's phone number in the international format (e.g., +1 for the USA, +44 for the UK).

Provide the Content: Depending on the action chosen, you will be asked for the relevant content (message text, image path, or file path).

Automatic Sending: After a short delay, the script will automatically send the message, image, or file via WhatsApp Web.
