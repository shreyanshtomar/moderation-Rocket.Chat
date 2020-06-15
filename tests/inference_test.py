import requests, unittest, base64
from server.server import app

import requests
from io import BytesIO

class BasicTestCase(unittest.TestCase):
    test_image_directory = 'tests'

    def test_sfw_image(self):
        tester = app.test_client(self)
        path = f"{self.test_image_directory}/test_images/park.jpeg"
        resp = tester.post('/predict', data={"file": open(path,'rb')})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, b'{"class_name":"sfw"}\n')

    def test_sfw_image_sent_as_base64(self):
        tester = app.test_client(self)
        image_path = f"{self.test_image_directory}/test_images/park.jpeg"
        image_file_handle = open(image_path, "rb")
        base64_string = base64.b64encode(image_file_handle.read())
        resp = tester.post('/predict', data={"file": base64_string})

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, b'{"class_name":"sfw"}\n')

if __name__ == '__main__':
    unittest.main()