import os
import time

while True:
    file_path = r"C:\Users\bavvb\Documents\OSU\361\assignment1\images"
    images = os.listdir(r"C:\Users\bavvb\Documents\OSU\361\assignment1\images")

    # Read random number
    with open('image_service.txt', 'r') as file:
        content = file.read()

    time.sleep(1)
    if 0 < len(content) < 2:
        number = int(content)
        random_image = "\\" + images[number]
        file_path += random_image

        with open('image_service.txt', 'w') as file:
            file.write(file_path)


