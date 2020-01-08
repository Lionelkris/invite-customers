import json
from config import OFFICE_LATITUDE, OFFICE_LONGITUDE
from math import radians, sin, cos, asin, sqrt


def read_from_file(customer_file):
    """
    This function reads the customer file and returns a list of dictionaries containing customer data.
    :param customer_file: Full path to the file that contains customer info in json format
    :return: A list of dictionaries containing customer data.
    Note: Expensive IO is taken care of by the with statement.
    """
    json_lines = []

    try:
        with open(customer_file) as file_handler:
            for line in file_handler:
                json_lines.append(json.loads(line))
            return json_lines
    except FileNotFoundError:
        raise FileNotFoundError(
            "File {} does not exist. Please ensure you have sent full path to the file".format(customer_file))


def calculate_distance_from_office(lat, lng):
    """
    :param lat: customer's latitude
    :param lng: customer's longitude
    :return: distance in kilometers between office and customer's location using the haversine's formula.
    """
    office_lat, office_lng, customer_lat, customer_lng = map(radians,
                                                             [OFFICE_LATITUDE, OFFICE_LONGITUDE, float(lat), float(lng)])
    diff_in_lat = customer_lat - office_lat
    diff_in_lng = customer_lng - office_lng

    # formula used from Great-circle distance https://en.wikipedia.org/wiki/Great-circle_distance
    a = sin(diff_in_lat/2) ** 2 + cos(office_lat) * cos(customer_lat) * sin(diff_in_lng/2) ** 2

    # Average earth radius in KM = 6371
    distance_in_km = 2 * 6371 * asin(sqrt(a))

    return distance_in_km


def get_customers_in_range(customer_file='customers.txt', distance_allowed=100):
    """
    :param customer_file: Full path to a file with customer details, defaults to customers.txt in current location.
    :param distance_allowed: distance in Km within which the customer should be located, defaults to 100 km.
    :return: Prints the names and ID of customers within allowed range to STDOUT sorted by customer ID.
    """

    customer_data = read_from_file(customer_file)
    # Returns a generator object that returns (distance, customer_id, customer_name) in a tuple.
    distance_from_office = (
        (calculate_distance_from_office(customer['latitude'], customer['longitude']),
                                        customer['user_id'], customer['name']) for customer in customer_data)

    # Returns a list that has the filtered customers that are within the distance_allowed in
    # (distance, customer_id, customer_name) format

    customers_in_range = list(filter(lambda x: x[0] <= distance_allowed,  distance_from_office))

    # Sort the above iterator based on the second key, ie. customer id.
    customers_in_range = sorted(customers_in_range, key=lambda x: x[1])

    return customers_in_range


def main():
    customers_in_range = get_customers_in_range()
    for each_customer in customers_in_range:
        print(each_customer[1], each_customer[2])


if __name__ == "__main__":
    main()
