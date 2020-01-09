import flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('Post.id'))

    post = db.relationship('Post')

    def post_name(self):
        return self.post.name


app = flask.Flask(__name__)

@app.route('/')
def index():
    comment = Comment.query.first()
    post_name = comment.post.name

    return flask.jsonify(post_name)
