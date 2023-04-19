from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Add(Resource):
    def get(self, num1, num2):
        if isinstance(num1, int) and isinstance(num2, int):
            result = num1 + num2
        else:
            result = float(num1) + float(num2)
        return {'result': result}


api.add_resource(Add, '/<num1>/<num2>')

if __name__ == '__main__':
    app.run(debug=True, port=5050, host='0.0.0.0')

