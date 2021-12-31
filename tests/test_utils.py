import unittest

from src import utils


class UtilsTest(unittest.TestCase):

    def test_extract_urls(self):
        text = '''
        this is a test with a link: https://www.google.com
        and another one http://bing.com in middle of text
        www.xlrd.org is third one in the start
        [MD test](https://play.google.com/store/apps/details?id=air.com.example) (0.00 -> 1.00)
        '''
        text_urls = [
            'https://www.google.com',
            'http://bing.com',
            'www.xlrd.org',
            'https://play.google.com/store/apps/details?id=air.com.example',
        ]

        self.assertEqual(utils.extract_urls(text), text_urls)


if __name__ == '__main__':
    unittest.main()
