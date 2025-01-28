from PIL import Image
import pytesseract
from reportlab.pdfgen import canvas
import os

def jpeg_to_text_pdf(input_dir, output_dir):
    """
    Convert JPEG images with text into text-based PDF files.

    :param input_dir: Directory containing JPEG files.
    :param output_dir: Directory to save the generated PDF files.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpeg', '.jpg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.pdf")

            try:
                # Open the image
                img = Image.open(input_path)

                # Extract text from the image
                extracted_text = pytesseract.image_to_string(img)

                # Create a PDF with the extracted text
                c = canvas.Canvas(output_path)
                c.setFont("Helvetica", 12)
                c.drawString(100, 750, f"Extracted text from {filename}:")

                # Break the text into lines and write to PDF
                text_lines = extracted_text.splitlines()
                y_position = 730  # Initial position on the page
                for line in text_lines:
                    if y_position < 50:  # Move to the next page if necessary
                        c.showPage()
                        c.setFont("Helvetica", 12)
                        y_position = 750
                    c.drawString(50, y_position, line)
                    y_position -= 15

                c.save()
                print(f"PDF created: {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    # Define input and output directories
    input_directory = "/mnt/c/Users/****/OneDrive/Documents/Jpeg2PDF/input"
    output_directory = "/mnt/c/Users/****/OneDrive/Documents/Jpeg2PDF/output"

    jpeg_to_text_pdf(input_directory, output_directory)

