# # app/db/base.py
# from app.db.session import Base
# from app.models.student_survey import StudentSurvey  # or whatever models you have

# from sqlalchemy.orm import declarative_base
# from app.models.student_survey import StudentSurvey  # Import to register it

# app/db/base.py
from app.db.base_class import Base  # ✅ Use the shared definition
from app.models.student_survey import StudentSurvey

