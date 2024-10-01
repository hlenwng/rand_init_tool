import cv2

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Error: Camera not accessible.")
else:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Camera Feed', frame)
        cv2.waitKey(0)  # Wait for a key press
    else:
        print("Error: Unable to read frame.")
    
cap.release()
cv2.destroyAllWindows()
