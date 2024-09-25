import cv2
from pyzbar.pyzbar import decode

# Load the image
image = cv2.imread('qrcode.png')

# Decode the QR code
qr_codes = decode(image)

# Process and print the decoded information
for qr_code in qr_codes:
    qr_data = qr_code.data.decode('utf-8')
    print(f"QR Code Data: {qr_data}")
