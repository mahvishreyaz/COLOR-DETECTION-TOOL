# COLOR-DETECTION-TOOL
In today's visual landscape, precise color detection is crucial. Our project introduces the Color Detection Tool with accurate color identification in digital and real-world images. Leveraging computer vision and image processing, it supports both static and real-time analyses, aiding in accessibility enhancement.

Software Description (Image):
The code starts by importing the necessary libraries, including OpenCV (cv2) for image 
processing and pandas for data handling. An image is loaded from the specified file path using 
OpenCV’s ‘cv2.imread’ function. This image will be used in colour detection. A CSV file is 
loaded into the environment that contains information about different colours, including their 
names, hexadecimal values, and RGB values. A list called detected_colours is created to store 
information about detected colours, including the position of the pixel, the colour name, and the 
RGB values. The first function is used to calculate the euclidean distance that is the minimum distance 
between the RGB values of the clicked pixel and the colours in the loaded CSV file. It returns 
the name of the colour that closely matches the clicked pixel's colour. The second function is 
called when the user double clicks the mouse, it retrieves the RGB values of the clicked pixel 
and appends the colour name and pixel coordinates to the ‘detected_colours’ list. If the ’s’ key is 
pressed, the code saves the detected colours to a text file named ‘detected_colours.txt’. To exit 
the program, the user must press the ‘esc’ key.

Software Description (Webcam):
Like the last code, this one also has the same basic integration of NumPy, Pandas ans OpenCV 
libraries. The code attempts to access the camera using OpenCV’s ‘cv2.VideoCapture(0)’ and 
can handle exceptions if the camera fails. The CSV file containing colour information is also 
read by the compiler. Similar to the first tool both the functions work in parallel to that code 
where the first function is used to calculate euclidean distance between the colour values in the 
dataset and the RGB values picked up by the cursor whilst the second function is used to identify 
colours through the cursor. A key difference is inside the main loop, the code captures frames 
from the camera and resizes them for display using imutils. Additionally, a colour swatch is 
provided to pin point the detected colour under the cursor. The program will continue till the user 
presses the 'esc' key to exit the program
