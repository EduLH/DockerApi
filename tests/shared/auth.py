import unittest
from src.shared.auth import Auth

class generateToken(unittest.TestCase):
    # def test_invalid_input(self):
    #     with self.assertRaises(Exception) as context:
    #         resp = Auth.generate_token()
    #     self.assertTrue('missing 1 required positional argument' in context.exception)
    def test_valid_input(self):
        resp = Auth.generate_token('nice@email.com')
        self.assertTrue(resp)


class decodeToken(unittest.TestCase):
    def test_invalid_input(self):
        resp = Auth.decode_token('invalidtoken')
        self.assertTrue(resp['error'])
    def test_valid_input(self):
        resp = Auth.decode_token("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTQyMDYwODYsImlhdCI6MTY1NDExOTY4Niwic3ViIjp7ImVtYWlsIjoic29tZV9lbWFpbEBnbWFpbC5jb20ifX0.DmozZ3A2kHPk9tU70zmlPI4aI1muzAPOo5y0lXJCCdU")
        self.assertTrue(resp['data'])



if __name__ == '__main__':
    unittest.main()
