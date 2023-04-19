from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class modulus(Resource):
    def get(self, num1, num2):
        result = num1 % num2
        return {'result': result}


api.add_resource(modulus, '/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=True, port=5050, host='0.0.0.0')
