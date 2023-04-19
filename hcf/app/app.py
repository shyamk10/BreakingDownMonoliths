from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class hcf(Resource):
    def get(self, num1, num2):
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        hcf = gcd(num1, num2)
        return {'result': hcf}


api.add_resource(hcf, '/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=True, port=5050, host='0.0.0.0')
