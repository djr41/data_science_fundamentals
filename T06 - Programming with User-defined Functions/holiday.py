# ========= Task 6 - holiday.py =========
# This script calculates the total cost of a holiday based on user input for
# city_flight - destination
# num_nights - number of nights stay
# rental_days - number of days for the car rental

# hotel_cost: This function takes num_nights as an argument, and
# return a total cost for the hotel stay based on a price per night of £100.
def hotel_cost(num_nights):
    hotel_cost = num_nights*100
    return hotel_cost

# I could have defined new varibles for the outputs instead of using the function name
# maybe the following is better practice(?)
# def hotel_cost(num_nights):
#     hotel_total = num_nights*100
#     return hotel_total

# plane_cost: This function takes city_flight as an argument
# and returns a cost for the flight based on the chosen city, 
# if the chosen city is not part of the prescribed options this
# function will return 0 
def plane_cost(city_flight):
    if city_flight == "Rome":
        plane_cost = 410
    elif city_flight == "Milan":
        plane_cost = 390
    elif city_flight == "Turin":
        plane_cost = 350
    elif city_flight == "Bologna":
        plane_cost = 430
    elif city_flight == "Florence":
        plane_cost = 350
    elif city_flight == "Venice":
        plane_cost = 540
    else:
        plane_cost =0
        print("That city is not available, please try again")
    return plane_cost

# car_rental: This function takes rental_days as an argument
# and returns the total cost of the car rental based on a day rate of £60.
def car_rental(rental_days):
    car_rental = rental_days*60
    return car_rental

# holiday_cost: This function takes the arguments
# hotel_cost, plane_cost, car_rental and returns the total cost of the holiday.
def holiday_cost(hotel_cost, plane_cost, car_rental):
    holiday_cost=hotel_cost+plane_cost+car_rental
    return holiday_cost


# Get the city_flight from the user
city_flight = input("\nWhich city would you like to fly to?\nPlease choose one from the follwing options: Rome, Milan, Turin, Bologna, Florence, Venice\n")
plane_cost=plane_cost(city_flight)

# If the city is available then the script proceed to ask the user for 
# num_nights, rental_days, calculates the holiday_total and prints the result for the user. 
if plane_cost != 0:
    num_nights = int(input("\nHow many nights would you like to stay?: "))
    rental_days = int(input("\nHow many days would you like to hire a car for?: "))
    hotel_cost=hotel_cost(num_nights)
    car_rental=car_rental(rental_days)
    holiday_cost = holiday_cost(hotel_cost, plane_cost, car_rental)
    # Print out all the details about the holiday in a readable way.
    print(f"\nYou have chosen to fly to {city_flight} for a {num_nights} night stay and will be hiring a car for {rental_days} day(s).\nThe total cost for your holiday will be £{holiday_cost}\n")