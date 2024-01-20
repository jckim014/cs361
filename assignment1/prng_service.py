import random
import time

while True:
    # check for "run" in prng service
    with open('prng-service.txt', 'r') as file:
        file_content = file.read()
    
    time.sleep(1)
    if file_content == "run":
        with open('prng-service.txt', 'w') as file:
            random_number = str(random.randrange(4))
            file.write(random_number)


