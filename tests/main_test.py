# import unittest
# from flask import Flask
# from main import app

# class TestMain(unittest.TestCase):

#     def setUp(self):
#         self.app = app.test_client()
#         self.app.testing = True

#     def test_weather_report_success(self):
#         response = self.app.get('/weather/Dallas/Texas/imperial')

#         self.assertEqual(response.status_code, 200)
#         self.assertIn('weather_report', response.json)

#     def test_weather_report_error(self):
#         response = self.app.get('/weather/NOCITYNAME/NOSTATENAME/imperial')

#         self.assertEqual(response.status_code, 400)
#         self.assertIn('error', response.json)

#     def test_server_initialization(self):
#         try:
#             self.app.get('/')
#             self.assertTrue(True)
#         except Exception as e:
#             self.fail(f"Server did not initialize correctly: {e}")

# if __name__ == '__main__':
#     unittest.main()
