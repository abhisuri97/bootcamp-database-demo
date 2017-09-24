from app import app, db
from .forms import UserForm
from app.models import User
from flask import render_template


@app.route('/', methods=['GET'])
def index():
    return 'Hello world!'


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    message = ''
    if form.validate_on_submit():
        username = form.name.data
        email = form.email.data
        if User.query.filter_by(username=username).count() == 0 and \
           User.query.filter_by(email=email).count() == 0:
                user = User(username, email)
                db.session.add(user)
                db.session.commit()
                message = 'successfully added user'
        else:
            message = 'username or email already exists'
    return render_template('add-user.html', form=form, message=message)
