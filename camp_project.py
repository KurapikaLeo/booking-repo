# Justyna
# R00198024
# camp project

# global variable counters
count_the_id_number = 0
total = 0
MAX_BOOKING_AMOUNT = 30


def read_data_booking_file(name_of_file):
    """
    this function reads the booking file
    :param name_of_file: str
    :return: accommodation : str
    price : float
    booking_number : int
    """
    accommodation = []
    price = []
    booking_number = []
    with open(name_of_file) as handle:
        while True:
            line = handle.readline()
            if line == "":
                break
            line_data = line.split(",")
            accommodation.append(line_data[0])
            price.append(int(line_data[1]))
            booking_number.append(int(line_data[2]))

    return accommodation, price, booking_number


def write_data_booking_file(filename, accommodation, price, booking_number):
    """
    this function writes to the booking file
    :param accommodation: str
    :param price: float
    :param booking_number: int
    :param filename: str
    :return: none
    """
    with open(filename, "w") as f:
        for q, entity in enumerate(accommodation):
            print(entity + "," + str(price[q]) + "," + str(booking_number[q]), file=f)


def create_extra_file(name_of_file):
    """
    this function reads the extra file
    :param name_of_file: str
    :return: extra
    """
    extra = []
    with open(name_of_file, 'r') as destination:
        for line in destination:
            strip_the_line = line.strip('\n')
            data = strip_the_line.split(',')
            extra.append(int(data[1]))

    return extra


def write_the_extra_file(name_of_file, extra):
    """
    this function writes to the extra file
    :param name_of_file:
    :param extra:
    :return:
    """
    headings = ['Kids Camp', 'Pool Pass']
    with open(name_of_file, 'w') as a_file:
        for q, entity in enumerate(headings):
            print(f'{entity}, {extra[q]}', file=a_file)

# menu user must choose an option 1, 2 or 3
def print_menu1():
    """
    this function creates a menu , that allows a user to choose an option
    :param : none
    :return: option - int
    """
    name = 'Long Island Holidays'
    print(name.upper())
    print('======================================')
    print('1 -- Making a booking')
    print('2 -- Review bookings')
    print('3 -- Exit')

    while True:
        try:
            option = int(input('Enter your choice here: '))
            if 1 <= option <= 3:
                break
            else:
                print('Please choose one of the options from the menu above')
        except ValueError:
            print('Please choose one of the options from the menu above')

    return option


def booking_information():
    """
    this function gathers user information about the booking
    :param: none
    :return: family_name - str
    phone_number - int
    accommodation_type - int
    family_pool - str
    number_in_group - int
    kid_club_number - int
    total - float
    """
    total = 0
    FAMILY_POOL_COST = 150
    KIDS_CAMP_COST = 100
    accommodation, price, booking_number = read_data_booking_file('bookings.txt')
    extra = create_extra_file("extras.txt")

# validation for the family name
    family_name = input('Enter the family name => ')
    while True:
        if (len(family_name) > 1 and len(family_name) <= 14) and family_name.replace("'", "").isalpha():
            break
        else:
            print('Enter a valid alphabetic name ')
            family_name = input('Enter the family name => ')

# validation to get the phone number
    phone_number = input('Enter the phone number =>')
    while True:
        if 1 <= len(phone_number) <= 12 and phone_number.isnumeric():
            break

        else:
            print('The phone number has to be less than 12 digits')
            phone_number = input('Enter the phone number =>')

# counting the accommodation type , price and the booking number
    print('Choose your accommodation type: ')
    for q, type in enumerate(accommodation):
        print(f'{q + 1} {type} €{price[q]} {booking_number[q]} is now booked')

    print('4 --No booking sorry ')
    accommodation_type = int(input('Enter the choice here =>'))

# selecting the appropriate accommodation from 1-3
    while True:
        if accommodation_type < 1:
            accommodation_type = int(input('Enter the choice here =>'))
        else:
            break

    while True:
        if accommodation_type == 1:
            total += price[accommodation_type-1]
            break
        elif accommodation_type == 2:
            total += price[accommodation_type-1]
            break
        elif accommodation_type == 3:
            total += price[accommodation_type-1]
            break
        else:
            accommodation_type = int(input('Enter the choice here =>'))

# find the number of members in the group
    while True:
        number_in_group = int(input('How many people in your group? '))
        if number_in_group <= 0:
            print('The number of people should be greater than 0')
            number_in_group = int(input('How many people in your group? '))
        else:
            break

# determines whether or not the members in the group would like a family pool pass
    family_pool = input('Would you like a family pool pass ? (y/n)')
    while True:
        if family_pool.lower() != 'y' and family_pool.lower() != 'n':
            family_pool = input('Would you like a family pool pass ? (y/n)')
        elif family_pool.lower() == 'y':
            total += FAMILY_POOL_COST
            extra[1] += 1
            break
        else:
            break

# determines the number of kids
    while True:
        kid_club_number = int(input('Enter the number of kids who wish to join the kids club: '))
        if kid_club_number < 0 or kid_club_number >= number_in_group:
            print('the number should be less than the number of people in total')
        else:
            total += kid_club_number * KIDS_CAMP_COST
            extra[0] += kid_club_number
            break

# counts the id number made during each booking
    global count_the_id_number
    count_the_id_number += 1

# prints the required information into the file as an output
    filename = f'{family_name}{count_the_id_number:02d}.txt'
    with open(filename, 'w') as output:
        print(f'Identification No. : {count_the_id_number:02d}', file=output)
        print(f'Family Name : {family_name}', file=output)
        print(f'Phone No. : {phone_number}', file=output)
        print(f'Type of Accommodation: {accommodation_type}', file=output)
        print(f'Amount of people in total : {number_in_group}', file=output)
        print(f'Amount of children: {kid_club_number}', file=output)
        print(f'Price: €{total}', file=output)
    accommodation_type = accommodation[accommodation_type - 1]
    write_the_extra_file('extras.txt', extra)

    return family_name, phone_number, accommodation_type, family_pool,  number_in_group, kid_club_number, total

# prints the receipt into the console
def booking_details_about_holidays():
    """
    this function takes the details about the holidays given from the booking_information function
    :param: none
    :return: total - float
    """
    accommodation, price, booking_number = read_data_booking_file("bookings.txt")



    family_name, phone_number, type, family_pool, number_in_group, kid_club_number, total = booking_information()
    print('Booking Details')
    print('=====================================================================')
    print(f'Booking id: {count_the_id_number} ')
    print(f'Type of accommodation :{type}')
    print(f'Number of people in total: {number_in_group}')
    print(f'Family pool pass: {family_pool}')
    print(f'Amount of kids for the kids club: {kid_club_number}')
    print(f'The cost for the holiday:  €{total}')
    print('=====================================================================')

    for q, entity in enumerate(accommodation):
        if type == entity:
            booking_number[q] = booking_number[q] + 1

    write_data_booking_file('bookings.txt', accommodation, price, booking_number)

    return total

def booking_reviews(total):
    """
    this function reviews the details about the holidays and calculates the total
    :param: none
    :return: none
    """
    global count_the_id_number
    price, accommodation, booking_number = read_data_booking_file('bookings.txt')
    kids_camp, family_pool = create_extra_file('extras.txt')
    print('======================================================================')
    print(f'{accommodation[0]} now booked ---- {booking_number[0]}')
    print(f'{accommodation[1]} now booked ---- {booking_number[1]}')
    print(f'{accommodation[2]} now booked ----{booking_number[2]}')
    print(f'kids camp ---- {kids_camp}')
    print(f'Family pool ---- {family_pool}')
    print(f'The total amount for the holiday ---- €{total}')
    print(f'Average amount ---- €{total/count_the_id_number}')
    print(f'The amount of spaces left over ---- {MAX_BOOKING_AMOUNT}')
    print('=======================================================================')


def main():
    counter = 0
    global MAX_BOOKING_AMOUNT
    while True:
        option = print_menu1()
        if option == 1:
            MAX_BOOKING_AMOUNT -= 1
            counter += 1
            total = booking_details_about_holidays()
        elif option == 2:
            if counter == 0:
                print('error no booking, try again ... ')
            else:
                booking_reviews(total)
        elif counter:
            break


main()