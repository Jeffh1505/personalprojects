import pytesseract
from PIL import Image
import re
import openpyxl
from openpyxl.drawing.image import Image as ExcelImage

# Function to extract data from receipt image
def extract_receipt_data(image_path):
    # Load image
    img = Image.open(image_path)
    
    # Use pytesseract to extract text from the image
    extracted_text = pytesseract.image_to_string(img)
    
    # Regular expressions to capture relevant fields
    date_pattern = re.compile(r'\b(\d{1,2}/\d{1,2}/\d{2,4})\b')
    time_pattern = re.compile(r'\b(\d{1,2}:\d{2}\s*(AM|PM)?)\b')
    amount_pattern = re.compile(r'(\$?\d+\.\d{2})')  # Match price format
    
    # Extracting fields
    date = date_pattern.search(extracted_text)
    time = time_pattern.search(extracted_text)
    amount = amount_pattern.search(extracted_text)
    
    # Assuming the first line after the date or time represents the service description
    service = ""
    if date:
        service_start = extracted_text.find(date.group()) + len(date.group())
        service_end = extracted_text.find('\n', service_start)
        service = extracted_text[service_start:service_end].strip()
    
    # Return the extracted data
    return {
        "date": date.group() if date else "N/A",
        "time": time.group() if time else "N/A",
        "service": service if service else "N/A",
        "amount": amount.group() if amount else "N/A"
    }

# Function to create an Excel spreadsheet and insert data
def create_spreadsheet(receipts_data, images_paths, output_file="receipts_data.xlsx"):
    # Create a new workbook and select the active worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Receipts"

    # Add headers to the spreadsheet
    headers = ["Date", "Time", "Service", "Amount", "Receipt Image"]
    ws.append(headers)
    
    # Add each receipt's data and corresponding image
    for i, data in enumerate(receipts_data):
        row = [data['date'], data['time'], data['service'], data['amount']]
        ws.append(row)
        
        # Insert the image into the spreadsheet
        img = ExcelImage(images_paths[i])
        img.anchor = f'E{i + 2}'  # Place the image in the appropriate row (starting from row 2)
        ws.add_image(img)
    
    # Save the workbook
    wb.save(output_file)
    print(f"Spreadsheet saved as {output_file}")

# Main function to execute the script for multiple images
def process_receipts(images_paths, output_file="receipts_data.xlsx"):
    receipts_data = []
    
    # Process each image, extract data, and store it
    for image_path in images_paths:
        receipt_data = extract_receipt_data(image_path)
        receipts_data.append(receipt_data)
    
    # Create the spreadsheet with all the extracted data and images
    create_spreadsheet(receipts_data, images_paths, output_file)

# Example usage with multiple images
image_paths = [r"C:\Users\summe\OneDrive\Pictures\Camera Roll\2024\09\20240902_211357000_iOS.jpg", r"C:\Users\summe\OneDrive\Pictures\Camera Roll\2024\09\20240902_211408000_iOS.jpg", r"C:\Users\summe\OneDrive\Pictures\Camera Roll\2024\09\20240902_211415000_iOS.jpg", r"C:\Users\summe\OneDrive\Pictures\Camera Roll\2024\09\20240902_211436000_iOS.jpg", r"C:\Users\summe\OneDrive\Pictures\Camera Roll\2024\09\20240902_211443000_iOS.jpg",r"C:\Users\summe\OneDrive\Pictures\Camera Roll\2024\09\20240902_211451000_iOS.jpg", r"C:\Users\summe\OneDrive\Pictures\Camera Roll\2024\09\20240902_211459000_iOS.jpg", r"C:\Users\summe\OneDrive\Pictures\Camera Roll\2024\09\20240902_211512000_iOS.jpg", r"C:\Users\summe\OneDrive\Pictures\Camera Roll\2024\09\20240902_211520000_iOS.jpg", r"C:\Users\summe\OneDrive\Pictures\Camera Roll\2024\09\20240902_211526000_iOS.jpg"]  # Replace with your image paths
process_receipts(image_paths)
