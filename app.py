from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Person(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  dob = db.Column(db.String(120), unique=True, nullable=False)

  def __init__(self, title, content):
    self.name = title
    self.dob = content

db.create_all()

@app.route('/person/<id>', methods=['GET'])
def get_names(id):
  item = Person.query.get(id)
  del item.__dict__['_sa_instance_state']
  return jsonify(item.__dict__)

@app.route('/people', methods=['GET'])
def get_items():
  items = []
  for item in db.session.query(Person).all():
    del item.__dict__['_sa_instance_state']
    items.append(item.__dict__)
  return jsonify(items)

@app.route('/person', methods=['POST'])
def create_item():
  body = request.get_json()
  db.session.add(Person(body['name'], body['dob']))
  db.session.commit()
  return "Person created"

@app.route('/person/<id>', methods=['PUT'])
def update_item(id):
  body = request.get_json()
  db.session.query(Person).filter_by(id=id).update(
    dict(name=body['name'], dob=body['dob']))
  db.session.commit()
  return "Person updated"

@app.route('/person/<id>', methods=['DELETE'])
def delete_item(id):
  db.session.query(Person).filter_by(id=id).delete()
  db.session.commit()
  return "Person deleted"