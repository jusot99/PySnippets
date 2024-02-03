from captcha.image import ImageCaptcha
from PIL import Image
import random
import string

# Function to generate a random string for the CAPTCHA
def generate_random_string(length=6):
    # Define characters for the CAPTCHA (letters and digits)
    characters = string.ascii_letters + string.digits
    # Use random.choice to pick characters randomly and join them into a string
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate a CAPTCHA image and return the CAPTCHA text
def generate_captcha():
    # Generate a random string for the CAPTCHA
    captcha_text = generate_random_string()
    # Create an ImageCaptcha object and generate an image for the CAPTCHA text
    image = ImageCaptcha().generate_image(captcha_text)
    # Save the generated image to a file (e.g., captcha.png)
    image.save('captcha.png')
    # Return the CAPTCHA text
    return captcha_text

# Function to verify if the user input matches the generated CAPTCHA text
def verify_captcha(user_input, captcha_text):
    # Compare user input and CAPTCHA text, case-insensitive
    return user_input.lower() == captcha_text.lower()

if __name__ == "__main__":
    # Generate a CAPTCHA and get the CAPTCHA text
    captcha_text = generate_captcha()
    print(f"Generated captcha: {captcha_text}")

    # Prompt the user to enter the CAPTCHA
    user_input = input("Enter the captcha: ")
    
    # Verify the user input against the generated CAPTCHA text
    if verify_captcha(user_input, captcha_text):
        print("Captcha verification successful!")
    else:
        print("Captcha verification failed.")
