import requests

api_key = "39efaf07570d46a3b7305601241202"


def main():
    # Introduction
    print("\nWelcome to the Weather App! You are able to enter your current "
          "location and retrieve various information about the weather in "
          "that location. This app is designed to help you make informed "
          "decisions on your outfits, plans, and general preparedness for "
          "the day.")
    print("Using this application is designed to be simple and quick. You will be "
          "prompted with a few questions - please choose a response to each "
          "and you can get weather information in a seconds!\n")

    # Location selection, only zipcode is currently functional
    location_type, location_string, current_location = get_location()

    # TODO: unit selection/conversion

    # Main menu: option selection
    print(f"You are located in {location_string}: {current_location}")
    option_input = 1
    while 0 < option_input < 3:
        print("Choose an option (press the option number):")
        option_input = int(input("1) Current Weather\n"
                                 "2) Weekly Weather\n"
                                 "3) Exit\n"))
        if option_input == 3:
            print("Thank you for using the Weather App. Goodbye.")
            break
        if option_input == 1:
            url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={current_location}&aqi=no'
            response = requests.get(url)
            current_weather = response.json()
            current_temperature = current_weather["current"]["temp_f"]
            print(f"The current temperature in {current_location} is {current_temperature} degrees Fahrenheit!")
        if option_input == 2:
            url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={current_location}&days=7'
            response = requests.get(url)
            weekly_weather = response.json()
            daily_data = weekly_weather["forecast"]["forecastday"]
            for day in daily_data:
                date = day["date"]
                average_temp = day["day"]["avgtemp_f"]
                print(f"The average temperature on {date} is {average_temp} degrees Fahrenheit.3")

    # wrong input error handling



def get_location():
    valid_location = 2
    location_string = ""
    current_entry = ""

    while valid_location == 2:
        # print("Would you like to use your zip code, city/state, or longitude/latitude "
        #       "coordinates?")
        # valid_input = False
        # while not valid_input:
        #     location_type = int(input("1) Zipcode (press 1)\n"
        #                               "2) City/State (press 2)\n"
        #                               "3) Coordinates (press 3)\n"))
        #
        #     valid_input = True
        #     if location_type == 1:
        #         location_string = "Zipcode"
        #     elif location_type == 2:
        #         location_string = "City/State"
        #     elif location_type == 3:
        #         location_string = "Coordinates"
        #     else:
        #         print("You have made an invalid input, please try again.")
        #         valid_input = False

        # TODO: Automatic location conversion

        # Location input
        location_type = 1
        if location_type == 1:
            zipcode = input("Please enter your Zipcode.\n")
            current_entry = zipcode

        valid_location = int(input(f"You have chosen {location_string} at {current_entry}. Is this correct?\n"
                                   f"1) Yes (Press 1)\n"
                                   f"2) No (Press 2)\n"))

    return [location_type, location_string, current_entry]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
