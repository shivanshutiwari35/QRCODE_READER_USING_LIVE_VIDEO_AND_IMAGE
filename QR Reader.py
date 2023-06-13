import numpy as np
from pyzbar.pyzbar import decode
import cv2

# Open the camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set the width of the frame
cap.set(4, 480)  # Set the height of the frame

while True:
    # Read the frame from the camera
    success, img = cap.read()

    # Decode barcodes in the frame
    for barcode in decode(img):
        print(barcode.data)

        # Convert barcode data to string
        mydata = barcode.data.decode('utf-8')
        print(mydata)

        # Get the polygon points of the barcode
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))

        # Draw the polygon around the barcode
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)

    # Display the resulting frame
    cv2.imshow('Result', img)

    # Wait for key press
    cv2.waitKey(1)
