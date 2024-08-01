from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}@{os.environ['MYSQL_HOST']}/{os.environ['MYSQL_DATABASE']}"

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()
    if not Item.query.first():
        initial_items = [Item(name='Item1'), Item(name='Item2'), Item(name='Item3')]
        db.session.bulk_save_objects(initial_items)
        db.session.commit()

@app.route('/')
def index():
    return '<h1 style="text-align: center;">Hello Tango!</h1><br><div style="text-align: center;"><a href="/items">Click here</a> to view the items.</div>'

@app.route('/healthz')
def health_check():
    return jsonify([{'status': 'UP'}])

@app.route('/items')
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)