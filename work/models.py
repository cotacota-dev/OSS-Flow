from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from database import Base

class OssApplication(Base):
    __tablename__ = 'oss_application'

    application_id = Column(Integer, primary_key=True, index=True)
    name_of_applicant = Column(String)
    pc_id = Column(String)
    name_of_oss = Column(String)
    version_of_oss = Column(String)
    application_date = Column(DateTime)
    approval = Column(Boolean)
    approval_date = Column(DateTime)