# from app import app
# from flask import Blueprint, request
# from services.departmentServices import get_departments, get_department_by_id, create_department, update_department, delete_department

# department_bp = Blueprint('department', __name__, url_prefix='/api/department')

# # Route to get all departments
# @department_bp.route('/', methods=['GET'])
# def fetch_departments():
#     return get_departments()

# # Route to get a department by id
# @department_bp.route('/<int:id>', methods=['GET'])
# def fetch_department(id):
#     return get_department_by_id(id) 

# # Route to create a new department
# @department_bp.route('/create', methods=['POST'])
# def create_new_department():
#     data = request.json 
#     return create_department(data) 

# # Route to update an existing department
# @department_bp.route('/update/<int:id>', methods=['PUT'])
# def update_existing_department(id):
#     data = request.json
#     return update_department(id, data)

# # Route to delete a department by id
# @department_bp.route('/delete/<int:id>', methods=['DELETE'])
# def delete_existing_department(id):
#     return delete_department(id)



# from app import app
# from flask import Blueprint, request
# from services.departmentServices import (
#     get_departments, get_department_by_id, create_department, 
#     update_department, delete_department
# )

# department_bp = Blueprint('department', __name__, url_prefix='/api/department')

# # Route to get all departments
# @department_bp.route('/', methods=['GET'])
# def fetch_departments():
#     return get_departments()

# # Route to get a department by ID
# @department_bp.route('/<int:id>', methods=['GET'])
# def fetch_department(id):
#     return get_department_by_id(id)

# # Route to create a new department with facility type and capacity
# @department_bp.route('/create', methods=['POST'])
# def create_new_department():
#     data = request.json 
#     return create_department(data) 

# # Route to update an existing department
# @department_bp.route('/update/<int:id>', methods=['PUT'])
# def update_existing_department(id):
#     data = request.json
#     return update_department(id, data)

# # Route to delete a department by ID
# @department_bp.route('/delete/<int:id>', methods=['DELETE'])
# def delete_existing_department(id):
#     return delete_department(id)  

from app import app
from flask import Blueprint, request, jsonify
from services.departmentServices import (
    get_departments, get_department_by_id, create_department, 
    update_department, delete_department
)
# from models.department import FacilityTypeEnum  # Import Enum

department_bp = Blueprint('department', __name__, url_prefix='/api/department')

# Route to get all departments
@department_bp.route('/', methods=['GET'])
def fetch_departments():
    return get_departments()

# Route to get a department by ID
@department_bp.route('/<int:id>', methods=['GET'])
def fetch_department(id):
    return get_department_by_id(id)

# # Route to get all available facility types (Dropdown support)
# @department_bp.route('/facility-types', methods=['GET'])
# def fetch_facility_types():
#     facility_types = {ft.name: ft.value for ft in FacilityTypeEnum}
#     return jsonify(facility_types)

# Route to create a new department with facility type and capacity
@department_bp.route('/create', methods=['POST'])
def create_new_department():
    data = request.json  

    classroom_name = data.get("classroom_name")
    facility_type = data.get("facility_type")
    capacity = data.get("capacity", 0)

    department_data = {
        "classroom_name": classroom_name,
        "facility_type": facility_type, # Convert string to Enum
        "capacity": capacity,
        "classroom_status": "Available"
    }

    return create_department(department_data)

# # Route to update an existing department
# @department_bp.route('/update/<int:id>', methods=['PUT'])
# def update_existing_department(id):
#     data = request.json  

#     # Validate facility type
#     if "facility_type" in data and data["facility_type"] not in .__members__:
#         return jsonify({"error": "Invalid facility type"}), 400

    return update_department(id, data)

# Route to delete a department by ID
@department_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_existing_department(id):
    return delete_department(id)
