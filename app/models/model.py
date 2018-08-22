from flask import jsonify


class Questions(object):
    def __init__(self, questionId, question, author, create_date, answer):

        self.questionId = questionId
        self.question = question
        self.author = author
        self.create_date = create_date
        self.answer = answer

    def get_all_questions(self):
        questions = {
            'questionId': self.questionId,
            'question': self.question,
            'author': self.author,
            'create_date': self.create_date,
            'answer': self.answer
        }
        return jsonify({'questions': questions})