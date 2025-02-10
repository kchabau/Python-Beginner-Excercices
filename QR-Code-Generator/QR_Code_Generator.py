import qrcode # Import the qrcode module

data = input("Enter text or URL to generate QR Code: ").strip() # Prompt the user to enter text or URL to generate QR Code
filename = input("Enter the filename to save the QR Code (e.g. my_qr_code.png): ").strip() # Prompt the user to enter the filename to save the QR Code

qr = qrcode.QRCode(box_size=14, border=8) # Create a QRCode object
qr.add_data(data) # Add the data to the QRCode object
image = qr.make_image(fill_color="black", back_color="white") # Generate the QR Code image
image.save(filename) # Save the QR Code as an image file

print(f"QR Code generated and saved as {filename}!") # Print a message to confirm that the QR Code has been generated and saved