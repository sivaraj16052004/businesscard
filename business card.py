import pytesseract
import cv2
from PIL import Image
import re

# Function to extract text from an image using OCR
def extract_text_from_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Use Pytesseract to perform OCR on the grayscale image
    extracted_text = pytesseract.image_to_string(gray_image)
    return extracted_text

# Function to parse business card data from extracted text
def parse_business_card_data(extracted_text):
    # Define regular expressions to match common patterns on business cards
    name_pattern = re.compile(r"([A-Z][a-z]+) ([A-Z][a-z]+)")
    phone_pattern = re.compile(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")
    email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

    # Find name, phone, and email using regular expressions
    name_match = name_pattern.search(extracted_text)
    phone_match = phone_pattern.search(extracted_text)
    email_match = email_pattern.search(extracted_text)

    # Extracted data
    name = name_match.group() if name_match else "Name not found"
    phone = phone_match.group() if phone_match else "Phone not found"
    email = email_match.group() if email_match else "Email not found"

    return {
        "Name": name,
        "Phone": phone,
        "Email": email,
    }

if __name__ == "__main__":
    # Path to the image of the business card
    image_path = "business_card.jpg"  # Replace with your image file

    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)

    # Parse business card data from the extracted text
    business_card_data = parse_business_card_data(extracted_text)

    # Display the extracted data
    print("Extracted Business Card Data:")
    for key, value in business_card_data.items():
        print(f"{key}: {value}")
