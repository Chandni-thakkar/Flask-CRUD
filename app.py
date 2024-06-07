from flask import Flask,request,jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
import os
from config import Config
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employees'

    emp_id = db.Column(db.Integer,primary_key=True)
    emp_name = db.Column(db.String(80),unique = True , nullable = False)
    emp_email = db.Column(db.String(120), unique =  True , nullable = False)
    emp_phone = db.Column(db.String(15),nullable=False)

    def json(self):
        return {'employee_id' : self.emp_id,
                'employee_username' :self.emp_name,
                'employee_email': self.emp_email,
                'employee_phone':  self.emp_phone
        }
with app.app_context():
    db.create_all()

#

# to create employee
@app.route('/employees',methods=['POST'])
def create_employee():
    try:
        data=request.get_json()
        new_emp=Employee(emp_name=data['emp_name'], emp_email = data['emp_email'] , emp_phone= data['emp_phone'])
        db.session.add(new_emp)
        db.session.commit()
        return make_response(jsonify({'message' :'employee created'}),201)
    except Exception as e:
        return make_response(jsonify({'message': f'error creating employee: {str(e)}'}), 500)

# get all employees
@app.route('/employees',methods=['GET'])
def get_employees():
    try:
        employees=Employee.query.all()
        return make_response(jsonify({'employees':[employee.json() for employee in employees]}),200)
    except Exception as e:
        return make_response(jsonify({'message': f'error getting employee details: {str(e)}'}), 500)

#get employee by id
@app.route('/employees/<int:id>',methods=['GET'])
def get_employees_by_id(id):
    try:
        employee = Employee.query.filter_by(emp_id=id).first()
        if employee:
            return make_response(jsonify({'employees': employee.json()}), 200)
        return make_response(jsonify({'message': 'Employee not found'}), 404)
    except Exception as e:
        print(f"Error getting employee details: {str(e)}")
        return make_response(jsonify({'message': f'error getting employee details: {str(e)}'}), 500)


#update employee details
@app.route('/employees/<int:id>',methods=['PUT'])
def update_employee(id):
    try:
        data=request.get_json()
        employee=Employee.query.filter_by(emp_id=id).first()
        if employee:
            employee.emp_name = data['emp_name']
            employee.emp_email =  data['emp_email']
            employee.emp_phone = data ['emp_phone']
            db.session.commit()
            return make_response(jsonify({'message': 'employee details updated'}),200)
        return make_response(jsonify({'message': 'employee not found'}),404)
    except Exception as e:
        return make_response(jsonify({'message': f'error updating employee details: {str(e)}'}), 500)

#delete a employee
@app.route('/employees/<int:id>',methods=['DELETE'])
def delete_employee(id):
    try:
        employee=Employee.query.filter_by(emp_id=id).first()
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return make_response(jsonify({'message': 'employee deleted'}), 200)
        return make_response(jsonify({'message': 'employee not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': f'error deleting employee details: {str(e)}'}), 500)

if __name__ == '__main__':
    app.run(debug=True)





