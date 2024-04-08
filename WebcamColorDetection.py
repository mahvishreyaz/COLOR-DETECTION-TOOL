
import numpy as np
import pandas as pd
import cv2
import imutils
import datetime

# Initialize variables and camera
r = g = b = xpos = ypos = 0
clicked = False
display_color_info = True  # Toggle color info display
screenshot_count = 1  # Initialize screenshot count
color_log = []  # List to store color and frame information

try:
    camera = cv2.VideoCapture(0)
except Exception as e:
    print(f"Error: Unable to access the camera - {e}")
    exit(1)

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']

try:
    df = pd.read_csv('C:\Mahvish NMIMS\Sem_5\mini project COLOR\colors.csv', names=index, header=None)
except Exception as e:
    print(f"Error: Unable to load color data - {e}")
    exit(1)

def getColorName(R, G, B):
    minimum = 10000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, "R"])) + abs(G - int(df.loc[i, "G"])) + abs(B - int(df.loc[i, "B"]))
        if (d <= minimum):
            minimum = d
            cname = df.loc[i, 'color_name'] + '   Hex=' + df.loc[i, 'hex']
    return cname

def identify_color(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked
    xpos = x
    ypos = y
    b, g, r = frame[y, x]
    b = int(b)
    g = int(g)
    r = int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image', identify_color)

while True:
    try:
        (grabbed, frame) = camera.read()
        frame = imutils.resize(frame, width=900)
        kernal = np.ones((5, 5), "uint8")
        
        # Toggle color information display
        if display_color_info:
            cv2.rectangle(frame, (20, 20), (800, 60), (b, g, r), -1)
            text = getColorName(b, g, r) + '   R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
            cv2.putText(frame, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            
            # Add a color swatch rectangle next to the color information
            swatch_size = 50
            swatch = np.zeros((swatch_size, swatch_size, 3), dtype=np.uint8)
            swatch[:] = (b, g, r)
            frame[20:20 + swatch_size, 820:820 + swatch_size] = swatch

            if (r + g + b >= 600):
                cv2.putText(frame, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        
        cv2.imshow('image', frame)

        key = cv2.waitKey(20)
        
        # Toggle color info display
        if key & 0xFF == ord('c'):
            display_color_info = not display_color_info
        
        # Capture the current frame as an image with a timestamp in the filename
        if key & 0xFF == ord('s'):
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            filename = r'C:\Users\Mahvish Reyaz Ansari\Downloads\captured_frame.png'
            cv2.imwrite(filename, frame)
            print(f'Frame captured as {filename} at timestamp: {timestamp}')
            
            # Store color and frame information in the log
            color_info = {
                "Timestamp": timestamp,
                "Color": getColorName(b, g, r),
                "FramePath": filename
            }
            color_log.append(color_info)
        
        if key & 0xFF == 27:
            break
    except Exception as e:
        print(f"An error occurred: {e}")

# Save color log to a CSV file
log_filename = r'C:\Users\Mahvish Reyaz Ansari\Downloads\color_log.csv'

log_df = pd.DataFrame(color_log)
log_df.to_csv(log_filename, index=False)
print(f"Color log saved to {log_filename}")

# Release the camera and close windows
camera.release()
cv2.destroyAllWindows()
