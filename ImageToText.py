from PIL import Image
import pytesseract


def image_to_text(image_path):
   
    try:
        img = Image.open(image_path)

        text = pytesseract.image_to_string(img)

        return text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")
    extracted_text = image_to_text(image_path)
    print("Extracted Text:\n")
    print(extracted_text)
