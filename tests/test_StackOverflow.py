import unittest, json
from app.models import create_app
from instance.config import TestingConfig
from app.models.model import Questions


BASE_URL = 'http://localhost:5000/api/v1/questions'


class TestStackOverflow(unittest.TestCase):
    def setUp(self):
        self.StackOverflow = create_app(config=TestingConfig)
        self.client = self.StackOverflow.test_client()
        self.question = Questions(questionId=1,
                                  question='What is programming?',
                                  author='Bwire',
                                  create_date='24-08-2018 02:27',
                                  answer='Programming is the process of creating instructions that tell a computer'
                                         ' how to perform a task')

    def test_get_all_questions(self):
        res = self.client.get('/api/v1/questions')
        self.assertEqual(res.status_code, 200)
        self.assertIn('programming is the process  a computer how to perform a task', str(res.data))

    def test_get_a_question(self):
        with self.client as client:
            res = client.get('/api/v1/questions/1')
            self.assertEqual(res.status_code, 200)
            self.assertIn('What is programming?', str(res.data))

    def test_add_a_answer(self):
        res = self.client.post(BASE_URL+'/1/answers', content_type='application/json',
                               data=json.dumps(dict(answer='Programming is the process of creating instructions that tell a computer how to perform a task')))
        self.assertEqual(res.status_code, 201)

    def test_add_a_question(self):
        res = self.client.get(BASE_URL+'/1', content_type='application/json', data=json.dumps(dict(questionId=1)))
        self.assertEqual(res.status_code, 201)

    def test_model_function(self):
        self.assertIsInstance(self.question, Questions)


if __name__ == "__main__":
    unittest.main()




