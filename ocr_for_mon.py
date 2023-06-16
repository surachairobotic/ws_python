import pytesseract
from PIL import Image

def ocr_left_top(image_path):
    """
    Load an image file, apply OCR to the left-top corner of the image, and return the text.
    """
    # Load the image file
    image = Image.open(image_path)

    # Get the dimensions of the image
    width, height = image.size

    # Define the region of interest as the left-top corner of the image
    left = 0
    top = 20
    right = (width // 3) - 30
    bottom = height // 15

    # Extract the region of interest as a new image
    roi = image.crop((left, top, right, bottom))

    # Apply OCR to the region of interest using PyTesseract
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    text = pytesseract.image_to_string(roi)

    # Return the text
    return text, roi

def main():
    txt, roi = ocr_left_top("00001.jpg")
    print(txt)
    roi.show()

if __name__ == '__main__':
    main()