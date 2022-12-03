from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/sign-up')
def sign_up():
    # some sign up operations
    pass
