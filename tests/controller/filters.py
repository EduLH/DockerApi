import unittest
from unittest import mock, IsolatedAsyncioTestCase
from src.controller.filters import *


class UserQuery(IsolatedAsyncioTestCase):
    async def test_invalid_input(self):
        resp = await user_query('a')
        self.assertEqual(resp, [])
    async def test_valid_input(self):
        resp = await user_query('2')
        self.assertEqual(resp.json()[0]['userId'], 2)


class IdQuery(IsolatedAsyncioTestCase):
    async def test_invalid_input(self):
        resp = await id_query('a')
        self.assertEqual(resp, [])
    async def test_valid_input(self):
        resp = await id_query('2')
        self.assertEqual(resp.json()[0]['id'], 2)


class completedQuery(IsolatedAsyncioTestCase):
    async def test_invalid_input(self):
        resp = await completed_query('a')
        self.assertEqual(resp, [])
    async def test_valid_input(self):
        resp = await completed_query('True')
        self.assertEqual(resp.json()[0]['completed'], True)


class titleQuery(IsolatedAsyncioTestCase):
    async def test_valid_input(self):
        resp = await title_query("delectus aut autem")
        self.assertEqual(resp.json()[0]['title'], 'delectus aut autem')


class allQuery(IsolatedAsyncioTestCase):
    async def test_invalid_input(self):
        resp = await all_query({})
        self.assertTrue(len(resp.json()) == 0)
    async def test_valid_input(self):
        resp = await all_query({
                        "user_id": 1,
                        "completed": 'False',
                        "id": 5,
                        "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
                    })
        self.assertTrue(len(resp.json()) == 1)


class searchLike(IsolatedAsyncioTestCase):
    async def test_invalid_input(self):
        resp = await search_like({})
        self.assertTrue(len(resp) > 0)
    async def test_valid_input(self):
        resp = await search_like({
                        "user_id": 1,
                        "completed": 'False',
                        "id": 5,
                        "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
                    })
        self.assertTrue(len(resp) > 1)


if __name__ == '__main__':
    unittest.main()
