import time
import unittest

import requests

BASE_URL = "http://localhost:5000/api/accounts" 

class TestApiPerformance(unittest.TestCase):

    def test_api_response_time(self):
        for i in range(100):
            start_time = time.time()

            requests.post(f"{BASE_URL}", json={"name": f"User{i}", "surname": "Testowy", "pesel": f"1234567890{i:02}"})
            requests.delete(f"{BASE_URL}/1234567890{i:02}")
            end_time = time.time()
            response_time = end_time - start_time

            self.assertLess(response_time, 2, f"Response time exceeds 2 seconds: {response_time} seconds")

if __name__ == '__main__':
    unittest.main()
