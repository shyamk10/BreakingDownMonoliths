from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class lcm(Resource):
    def get(self, n1, n2):
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        result = (n1 * n2) // gcd(n1, n2)

        return {'result': result}


api.add_resource(lcm, '/<int:n1>/<int:n2>')

if __name__ == '__main__':
    app.run(debug=True, port=5050, host='0.0.0.0')
