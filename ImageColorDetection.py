import cv2
import pandas as pd

img_path = r'C:\Mahvish NMIMS\Sem_5\mini project COLOR\colorpic.jpg'
img = cv2.imread(img_path)

# declaring global variables (are used later on)
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('C:\Mahvish NMIMS\Sem_5\mini project COLOR\colors.csv', names=index, header=None)

# List to store detected colors and their coordinates
detected_colors = []

# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        detected_colors.append((x, y, get_color_name(r, g, b), (r, g, b)))

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
    cv2.imshow("image", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked = False

    # Break the loop when user hits 'esc' key
    key = cv2.waitKey(20) & 0xFF
    if key == 27:
        break
    
    # Save the detected colors when 's' key is pressed
    elif key == ord('s'):
        with open("detected_colors.txt", "w") as file:
            for color_info in detected_colors:
                file.write(f"Color: {color_info[2]}, RGB: {color_info[3]}, Position: {color_info[0]}, {color_info[1]}\n")

print("Saved Colors:")
# Open the text file in read mode
with open('detected_colors.txt', 'r') as file:
    # Read and print the entire content of the file
    file_contents = file.read()
    print(file_contents)



cv2.destroyAllWindows()
