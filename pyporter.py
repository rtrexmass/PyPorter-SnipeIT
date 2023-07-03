# SUP, THIS IS A SCRIPT TO GET MULTIPLE OR ONE BARCODE DATA FROM A PHOTO (PLEASE SHOOT THE FUCKING PHOTO WITH GOOD QUALITY WITHOUT COMPRESSION)
# THEM WILL ASK FOR THINGS TO PUT IN A CSV SO IT CAN BE IMPORTED TO SNIPEIT, PROMPT THE FIELDS WITH THE CORRECT VALUES PLEASE, LOOK THEM UP IN SNIPEIT
# AFTER YOU PROMPETD ALL THE THINGS, IT WILL SHOW THE DATA GATHERED, CHECK THEM PLEASE (COUNT IF THE QUANTITY IS RIGHT).
# THE DATA WILL BE SERVED IN "barcode_data.csv" IN THIS EXACT DIRECTORY
import csv
import cv2
from pyzbar import pyzbar

def scan_barcodes():
    image_path = input("Enter the path to the image file: ")
    image = cv2.imread(image_path)
    barcodes = pyzbar.decode(image)

    csv_file = open("barcode_data.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(csv_file)
    writer.writerow(["Category", "Location", "Model Name", "Manufacturer", "Serial Number", "Status", "Default Location"])

    category = input("Category: ")
    location = input("Location: ")
    model_name = input("Model Name: ")
    manufacturer = input("Manufacturer: ")
    default_location = input("Default Location: ")

    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        serial_number = barcode_data

        print("Barcode Data: {}".format(barcode_data))

        writer.writerow([category, location, model_name, manufacturer, serial_number, "Ready To Deploy", default_location])

    csv_file.close()

# YOUR IMAGE GOES HERE
scan_barcodes()
# YOU NEED THE FLAG "R" BECAUSE PYTHON IS DUMB AND CANT ESCAPE THE FUCKING "\" PROPERLY :), BUT IF YOU ARE USING LINUX, I DONT WANNA TALK TO YOU.
