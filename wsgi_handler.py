from app import app  # tu Flask app.py debe tener `app = Flask(__name__)`

def handler(event, context):
    from flask_lambda import FlaskLambda
    lambda_app = FlaskLambda(app)
    return lambda_app(event, context)
