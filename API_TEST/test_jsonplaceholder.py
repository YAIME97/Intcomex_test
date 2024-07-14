import unittest
import requests

class TestJSONPlaceholderAPI(unittest.TestCase):

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def test_get_todo(self):
        # Realizar una solicitud GET
        url = f"{self.BASE_URL}/todos/1"
        response = requests.get(url)

        # Ver en consola la respuesta de GET
        print(response.json())

        # Verificar que el estado de la respuesta sea 200
        self.assertEqual(response.status_code, 200)

        # Verificar que el cuerpo de la respuesta contenga los datos esperados
        expected_keys = ['userId', 'id', 'title', 'completed']
        response_json = response.json()

        for key in expected_keys:
            self.assertIn(key, response_json)

        # Verificar los valores específicos
        self.assertEqual(response_json['userId'], 1)
        self.assertEqual(response_json['id'], 1)
        self.assertEqual(response_json['title'], "delectus aut autem")
        self.assertEqual(response_json['completed'], False)

if __name__ == "__main__":
    unittest.main()
