import time
while True:
    user_input = input("Press 1 to generate a random image: ")

    if user_input == "1":
        # write "run" to prng service
        with open('prng-service.txt', 'w') as file:
            file.write("run")

        # read random number from prng service
        time.sleep(3)
        with open('prng-service.txt', 'r') as file:
            random_number = file.read()

        # write the prng to image service
        with open('image_service.txt', 'w') as file:
            file.write(random_number)
        
        time.sleep(3)

        # retrieve and print filepath
        with open('image_service.txt', 'r') as file:
            file_path = file.read()
            print(file_path)



