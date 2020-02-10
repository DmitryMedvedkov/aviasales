
from web_service import app
import unittest

class BasicTestCase(unittest.TestCase):

    def test_load(self):
        tester = app.test_client(self)
        response = tester.get('/load')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"dictionary_of_anagrams":["foobar","aabb","baba","boofar","test"]}\n')

    def test_show_foobar(self):
        tester = app.test_client(self)
        response = tester.get('/foobar')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"boofar":null,"foobar":null}\n')

    def test_raboof(self):
        tester = app.test_client(self)
        response = tester.get('/raboof')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"boofar":null,"foobar":null}\n')

    def test_show_abba(self):
        tester = app.test_client(self)
        response = tester.get('/abba')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"aabb":null,"baba":null}\n')

    def test_show_test(self):
        tester = app.test_client(self)
        response = tester.get('/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"test":null}\n')

    def test_show_qwerty(self):
        tester = app.test_client(self)
        response = tester.get('/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"test":null}\n')


if __name__ == '__main__':
  unittest.main()
#{"dictionary_of_anagrams": ["foobar","aabb","baba","boofar","test"]}