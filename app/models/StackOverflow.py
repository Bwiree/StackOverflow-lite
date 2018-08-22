from flask import Flask, Blueprint, request, Response, jsonify, json
from flask_restful import Api


app = Flask(__name__)

blue_print = Blueprint('questions_bp', __name__, url_prefix='/api/v1')
api = Api(blue_print)

questions = [
    {
        'questionId': 1,
        'question': 'What is programming?',
        'author': 'Bwire',
        'create_date': '24-08-2018 02:27',
        'answer': 'Programming is the process of creating instructions that tell a computer how to perform a task'

    },
    {
        'questionId': 2,
        'question': 'When is the next bootcamp?',
        'author': 'Rechael',
        'create_date': '20-09-2018 18:09',
        'answer': 'It shall be communicated'
    },
    {
        'questionId': 3,
        'question': 'What makes programming fun?',
        'author': 'Opio',
        'create_date': '07-10-2018 10:24',
        'answer': 'Actually I should say Andela makes programming fun'
    },
    {
        'questionId': 4,
        'question': 'Why should programmers be creative?',
        'author': 'Patrick',
        'create_date': '17-10=2018 12:13',


    }

]


@app.route('/api/v1/questions')
def get_all_questions():
    questionz = []
    for question in questions:
        questionz.append(question)
    return jsonify(questionz)


@app.route('/api/v1/questions', methods=['POST'])
def add_a_question():
    qn = {'questionId': request.json['questionId'],
          'question': request.json['question'],
          'author': request.json['author'],
          'create_date': request.json['create_date'],
          }
    if isinstance(qn, dict):
        questions.append(qn)
        response = Response("Question added", 201, mimetype="application/json")
        response.headers['Location'] = "questions/" + str(request.json['questionId'])
        return response

    else:
        bad_object = {
            "error": "Invalid question object",
            "help_string":
                "Request format should be {'questionId': 10,"
                "'question': 'What is your question?','author': 'name', 'create_date': '07-10-2018 10:24' }"
        }
        response = Response(json.dumps(bad_object), status=400, mimetype="application/json")
        return response


@app.route('/api/v1/questions/<int:questionId>')
def get_a_question(questionId):
    for question in questions:
        if question['questionId'] == questionId:
            qn = {
                'question': question['question'],
                'author': question['author']
            }
            return jsonify(qn)
    return jsonify({'message': 'question not found'})


@app.route('/api/v1/questions/<int:questionId>/answer', methods=['POST'])
def add_an_answer(questionId):
    for question in questions:
        if question['questionId'] == questionId:
            new_answer = {'answer': request.json['answer']}
            list(questions).append(new_answer)
            response = Response("Answer posted", 201, mimetype="application/json")
            return response
    return jsonify({'message': 'question not found'})


if __name__ == "__main__":
    app.run(debug=True)
