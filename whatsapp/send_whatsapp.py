import pywhatkit as pwlib
import time

# Function to send a text message


def send_message(phone_number, message, wait_time=15):
    """
    phone_number: Recipient's phone number (with country code)
    message: The message to send
    wait_time: The time to wait before sending the message (in seconds)
    """
    pwlib.sendwhatmsg(phone_number, message, time.localtime(
    ).tm_hour, time.localtime().tm_min + wait_time)

# Function to send an image


def send_image(phone_number, image_path, caption=""):
    """
    phone_number: Recipient's phone number (with country code)
    image_path: The file path of the image to send
    caption: Optional caption to add to the image
    """
    pwlib.sendwhats_image(phone_number, image_path, caption)

# Function to send a file


def send_file(phone_number, file_path):
    """
    phone_number: Recipient's phone number (with country code)
    file_path: The file path of the file to send
    """
    pwlib.sendwhatmsg(phone_number, "Sending file.",
                      time.localtime().tm_hour, time.localtime().tm_min + 15)
    time.sleep(30)  # Wait for the message to be sent
    pwlib.sendwhats_file(phone_number, file_path)


# User input to choose the action
action = input("Choose an action (message, image, file): ").lower()

phone_number = input(
    "Enter the phone number (with country code, e.g., +1 for USA): ")

if action == "message":
    message = input("Enter the message you want to send: ")
    send_message(phone_number, message)

elif action == "image":
    image_path = input("Enter the path of the image you want to send: ")
    caption = input(
        "Do you want to add a caption to the image? (yes/no): ").lower()
    if caption == "yes":
        caption_text = input("Enter the caption: ")
        send_image(phone_number, image_path, caption_text)
    else:
        send_image(phone_number, image_path)

elif action == "file":
    file_path = input("Enter the path of the file you want to send: ")
    send_file(phone_number, file_path)

else:
    print("Invalid choice.")
