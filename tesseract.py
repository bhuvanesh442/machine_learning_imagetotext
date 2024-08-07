import webbrowser

# Define the search query
# search_query = "React"
search_query = input()
# Construct the YouTube search URL
url = f"https://www.youtube.com/results?search_query={search_query}"

# Open the URL in the default web browser
webbrowser.open(url)












# import pytesseract as pyt
# import cv2
# import os

# # Define the image path and Tesseract executable path
# # image_path = r"C:\Users\LENOVA\Downloads\OIP.jpeg"

# image_path = r"C:\Users\LENOVA\Pictures\Screenshot 2024-08-07 184345.png"
# tesseract_path = r"C:\Users\LENOVA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# # Check if the image file exists
# if not os.path.exists(image_path):
#     print(f"Image file not found: {image_path}")
#     exit(1)

# # Set the Tesseract executable path
# if not os.path.exists(tesseract_path):
#     print(f"Tesseract executable not found: {tesseract_path}")
#     exit(1)

# pyt.pytesseract.tesseract_cmd = tesseract_path
# print(f"Tesseract path set to: {tesseract_path}")

# # Read the image using OpenCV
# img = cv2.imread(image_path)
# if img is None:
#     print("Failed to read the image.")
#     exit(1)
# else:
#     print("Image read successfully.")

# # Perform OCR on the image
# try:
#     text = pyt.image_to_string(img)
#     print("OCR performed successfully.")
#     print("Extracted Text:")
#     print(text)
# except pytesseract.TesseractError as e:
#     print(f"Tesseract error: {e}")
# except Exception as e:
#     print(f"Error: {e}")

















# import pytesseract as pyt
# import cv2

# # Read the image using OpenCV
# img = cv2.imread("C:\\Users\\LENOVA\\Downloads\\OIP.jpeg")

# # Set the Tesseract executable path
# pyt.pytesseract.tesseract_cmd = "C:\\Users\\LENOVA\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

# # Perform OCR on the image
# text = pyt.image_to_string(img)

# # Print the extracted text
# print(text)

# import pytesseract as pyt
# import cv2
# import os

# # Define the image path and Tesseract executable path
# image_path = r"C:\Users\LENOVA\Downloads\OIP.jpeg"
# tesseract_path = r"C:\Users\LENOVA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# # Check if the image file exists
# if not os.path.exists(image_path):
#     print(f"Image file not found: {image_path}")
#     exit(1)

# # Set the Tesseract executable path
# if not os.path.exists(tesseract_path):
#     print(f"Tesseract executable not found: {tesseract_path}")
#     exit(1)

# pyt.pytesseract.tesseract_cmd = tesseract_path

# # Read the image using OpenCV
# img = cv2.imread(image_path)

# # Perform OCR on the image
# text = pyt.image_to_string(img)

# # Print the extracted text
# print(text)

