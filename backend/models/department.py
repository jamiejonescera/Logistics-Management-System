# from app import db
# from datetime import datetime
# import pytz

# # Set Manila timezone
# MANILA_TZ = pytz.timezone("Asia/Manila")

# class DepartmentFacility(db.Model):
#     __tablename__ = 'department_facility'

#     department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     classroom_name = db.Column(db.String(100), nullable=False, unique=True)
#     created_at = db.Column(db.DateTime, default=lambda: datetime.now(MANILA_TZ))
#     updated_at = db.Column(db.DateTime, default=lambda: datetime.now(MANILA_TZ), onupdate=lambda: datetime.now(MANILA_TZ))

#     def __repr__(self):
#         return f"<DepartmentFacility {self.classroom_name}>"

#     def to_dict(self):
#         return {
#             'department_id': self.department_id,
#             'classroom_name': self.classroom_name,
#             'created_at': self.created_at,
#             'updated_at': self.updated_at
#         }

# from app import db
# from datetime import datetime
# import pytz
# from enum import Enum

# # Set Manila timezone
# MANILA_TZ = pytz.timezone("Asia/Manila")

# # # Enum for Facility Types
# # class FacilityTypeEnum(Enum):
# #     classroom_learning = "Classroom & Learning Spaces"
# #     standard_classroom = "Standard Classroom"
# #     lecture_hall = "Lecture Hall"
# #     laboratory = "Laboratory (Science, Computer, etc.)"
# #     library = "Library"
# #     study_room = "Study Room"
# #     auditorium = "Auditorium"
# #     sports_recreation = "Sports & Recreation Facilities"
# #     gymnasium = "Gymnasium"
# #     basketball_court = "Basketball Court"
# #     football_field = "Football Field"
# #     swimming_pool = "Swimming Pool"
# #     track_field = "Track and Field Area"
# #     playground = "Playground"
# #     admin_staff = "Administrative & Staff Areas"
# #     faculty_room = "Faculty Room"
# #     principal_office = "Principal’s Office"
# #     guidance_office = "Guidance Office"
# #     conference_room = "Conference Room"
# #     reception_area = "Reception Area"
# #     specialized_rooms = "Specialized Rooms"
# #     music_room = "Music Room"
# #     art_room = "Art Room"
# #     theater_room = "Theater/Performing Arts Room"
# #     robotics_lab = "Robotics Lab"
# #     home_economics = "Home Economics Room"
# #     language_lab = "Language Lab"
# #     build = "Building"  # Added "Build" as a facility type

# class DepartmentFacility(db.Model):
#     __tablename__ = 'department_facility'

#     department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     classroom_name = db.Column(db.String(100), nullable=False, unique=True)
#     facility_type = db.Column(db.String(100), nullable=True)  # Using Enum for dropdown
#     capacity = db.Column(db.Integer, default=0, nullable=True)
#     classroom_status = db.column(db.String(100), nullable=True)

#     def __repr__(self):
#         return f"<DepartmentFacility {self.classroom_name}>"

#     def to_dict(self):
#         return {
#             'department_id': self.department_id,
#             'classroom_name': self.classroom_name,
#             'facility_type': self.facility_type.value,  # Returns readable facility name
#             'capacity': self.capacity,
#             'classroom_status': self.classroom_status
#         }

from app import db
from datetime import datetime
import pytz

# Set Manila timezone
MANILA_TZ = pytz.timezone("Asia/Manila")

class DepartmentFacility(db.Model):
    __tablename__ = 'department_facility'

    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    classroom_name = db.Column(db.String(100), nullable=False, unique=True)
    facility_type = db.Column(db.String(100), nullable=True)  # Enum can be used for predefined types
    capacity = db.Column(db.Integer, default=0, nullable=True)
    classroom_status = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<DepartmentFacility {self.classroom_name}>"

    def to_dict(self):
        return {
            'department_id': self.department_id,
            'classroom_name': self.classroom_name,
            'facility_type': self.facility_type,
            'capacity': self.capacity,
            'classroom_status': self.classroom_status
        }


# from app import db
# from datetime import datetime
# import pytz

# # Set Manila timezone
# MANILA_TZ = pytz.timezone("Asia/Manila")

# class DepartmentFacility(db.Model):
#     __tablename__ = 'department_facility'

#     department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     classroom_name = db.Column(db.String(100), nullable=False, unique=True)
#     created_at = db.Column(db.DateTime, default=lambda: datetime.now(MANILA_TZ))
#     updated_at = db.Column(db.DateTime, default=lambda: datetime.now(MANILA_TZ), onupdate=lambda: datetime.now(MANILA_TZ))

#     def __repr__(self):
#         return f"<DepartmentFacility {self.classroom_name}>"

#     def to_dict(self):
#         return {
#             'department_id': self.department_id,
#             'classroom_name': self.classroom_name,
#             'created_at': self.created_at,
#             'updated_at': self.updated_at
#         }
