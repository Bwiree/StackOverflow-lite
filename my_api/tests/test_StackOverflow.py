import unittest

from my_api.api import create_app
from my_api.instance.config import TestingConfig

BASE_URL = 'http://127.0.0.1:5000/api/v1/questions'


class TestStackOverflow(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()

    def test_get_questions(self):
        with self.client as client:
            client.post(BASE_URL, json=dict(questionId=1, question='What is programming?', author='Bwire',
                                            create_date='24-12-2018 11:10', answers=[]))
            response = client.get(BASE_URL)
            self.assertEqual(response.status_code, 200)

    def test_get_a_question(self):
        with self.client as client:
            client.post(BASE_URL, json=dict(questionId=1, question='What is programming?', author='Bwire',
                                            create_date='24-12-2018 11:10', answers=[]))
            response = client.get(BASE_URL+'/1', json=dict(questionId=1))
            self.assertEqual(response.status_code,200)

    def test_question_not_existing(self):
        with self.client as client:
            response = client.get(BASE_URL+'/5', json=dict(questionId=1))
            self.assertEqual(response.status_code, 404)

    def test_post_question(self):
        with self.client as client:
            response = client.post(BASE_URL, json=dict(question='How many programmers designed facebook?', author='Mike', create_date='234556776', answers=['It think twenty two']))
            self.assertEqual(response.status_code,201)

    def test_question_not_found_for_added_answer(self):
        with self.client as client:
            client.post(BASE_URL, json=dict(question='What is programming?', author='Bwire', answers=['Programming is the process of writing instructions that tell a computer what to do']))
            response = client.post(BASE_URL+'/21/answers', json=dict(answers='Iam lost'))
            self.assertEqual(response.status_code, 404)

    def test_question_not_string(self):
        with self.client as client:
            response = client.post(BASE_URL, json=dict(question=100000, author='Celine'))
            self.assertEqual(response.status_code, 406)

    def test_Invalid_question_added_spaces(self):
        with self.client as client:
            response = client.post(BASE_URL, json=dict(question='       ', author='Solomon'))
            self.assertEqual(response.status_code, 406)
