import unittest
from customers_in_range import get_customers_in_range, calculate_distance_from_office, read_from_file


class CustomersInRangeTest(unittest.TestCase):

    def test_read_from_file_returns_correct_data(self):
        customers_list = read_from_file("test_data.txt")
        expected_customers_list = [
            {"latitude": "53.1229599", "user_id": 6, "name": "Theresa Enright", "longitude": "-6.2705202"},
            {"latitude": "52.366037", "user_id": 16, "name": "Ian Larkin", "longitude": "-8.179118"},
            {"latitude": "53.0033946", "user_id": 39, "name": "Lisa Ahearn", "longitude": "-6.3877505"},
            {"latitude": "52.966", "user_id": 15, "name": "Michael Ahearn", "longitude": "-6.463"},
            {"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}]
        self.assertEqual(customers_list, expected_customers_list)

    def test_calculate_distance_from_office_is_correct(self):
        # Distance computed for a customer whose distance from office is verified from reliable source = 24.09 Km
        distance = calculate_distance_from_office(53.1229599, -6.2705202)
        self.assertEqual(round(distance, 2), 24.09)

    def test_get_customers_in_range_is_correct_and_sorted(self):
        customers_in_range = get_customers_in_range("test_data.txt")

        # Distances of customers within range specified. Range is 100 here
        expected_customers_list = [(24.085360019144144, 6, 'Theresa Enright'),
                                   (41.768725500836176, 12, 'Christina McArdle'),
                                   (43.72248745925148, 15, 'Michael Ahearn'),
                                   (38.35801477480546, 39, 'Lisa Ahearn')]

        self.assertEqual(customers_in_range, expected_customers_list)


if __name__ == '__main__':
    unittest.main()
