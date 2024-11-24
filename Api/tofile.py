from io import StringIO, BytesIO
from pypdf import PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import csv
import json
import os

def new_pdf(data):
    name = f"pdfs/{str(len(os.listdir('pdfs')))}.pdf"
    # Initialize the PdfWriter object
    new_pdffile = canvas.Canvas(name, pagesize=letter)
    inch = 0.3125*5
    # Get the width and height of the page in points
    width, height = letter
    # Set initial position for writing text
    y_position = height - 40 * inch  # Convert pixels to inches
    
    # Write JSON data to PDF
    for i in data["ips"]:
        for key, value in i.items():
            new_pdffile.drawString(1 * inch, y_position, f"{key}: {value}")
            y_position -= 20 * inch  # Move down for next line
            
            # If we reach the bottom of a page, create a new one
            if y_position < 30 * inch:
                new_pdffile.showPage()
                y_position = height - 40 * inch    
    # Finalize the PDF
    new_pdffile.save()
    # Return None as we've already saved the PDF to disk
    return name












"""
def new_pdf(data):
    new_pdffile = BytesIO()
    pdf = canvas.Canvas(new_pdffile, pagesize=letter)
    width, height = letter
    # Set initial position for writing text
    y_position = height - 40
    # Write JSON data to PDF
    for i in data["ips"]:
        for key, value in i.items():
            pdf.drawString(40, y_position, f"{key}: {value}")
            y_position -= 20  # Move down for next line
            if y_position < 40:  # If we reach the bottom, create a new page
                pdf.showPage()
                y_position = height - 40
    # Finalize the PDF
    pdf.save()
    # Move the buffer position to the beginning
    new_pdffile.seek(0)
    return new_pdffile.getvalue()  # Return the PDF bytes

def new_csv(data):
    new_csvfile = StringIO()
    writer = csv.writer(new_csvfile)
    keys = data[0].keys() if data else []
    writer.writerow(keys)
    for entry in data:
        writer.writerow(entry.values())
    csv_content = new_csvfile.getvalue()
    new_csvfile.close()
    return csv_content
"""