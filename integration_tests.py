import unittest
import requests

class IntegrationTests(unittest.TestCase):
    def test_get_data(self):
        response = requests.get('https://us-central1-latam-project.cloudfunctions.net/latam-http-endpoint')
        self.assertEqual(response.status_code, 200)

    def test_insert_data(self):
        payload = {
            'name': 'Carlos',
            'age': '30'
        }
        response = requests.post('https://us-central1-latam-project.cloudfunctions.net/latam-http-endpoint', json=payload)
        self.assertEqual(response.status_code, 201)
        # Now we verify the inserted data is available
        response = requests.get('https://us-central1-latam-project.cloudfunctions.net/latam-http-endpoint')
        self.assertIn(payload, response.json())

    def test_update_data(self):
        payload = {
            'name': 'Noel',
            'age': '45'
        }
        response = requests.put('https://us-central1-latam-project.cloudfunctions.net/latam-http-endpoint', json=payload)
        self.assertEqual(response.status_code, 200)
        # Now we verify the updated data is available
        response = requests.get('https://us-central1-latam-project.cloudfunctions.net/latam-http-endpoint/1')
        self.assertEqual(response.json()['name'], payload['name'])
        self.assertEqual(response.json()['age'], payload['age'])

if __name__ == '__main__':
    unittest.main()