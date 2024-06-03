from flask import Flask, render_template, session, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for session handling

class User:
    def __init__(self, is_authenticated):
        self.is_authenticated = is_authenticated

    def to_dict(self):
        return {'is_authenticated': self.is_authenticated}

    @staticmethod
    def from_dict(data):
        return User(is_authenticated=data['is_authenticated'])

@app.context_processor
def inject_user():
    current_user = session.get('current_user')
    if current_user:
        current_user = User.from_dict(json.loads(current_user))
    else:
        current_user = User(is_authenticated=False)
    return {'current_user': current_user}

@app.route('/')
def index():
    current_user = session.get('current_user')
    if current_user:
        current_user = User.from_dict(json.loads(current_user))
        if current_user.is_authenticated:
            return redirect(url_for('home'))
    return render_template('index.html')

@app.route('/home')
def home():
    current_user = session.get('current_user')
    if current_user:
        current_user = User.from_dict(json.loads(current_user))
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    return render_template('home.html')

@app.route('/login')
def login():
    session['current_user'] = json.dumps(User(is_authenticated=True).to_dict())
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('current_user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=8888)
