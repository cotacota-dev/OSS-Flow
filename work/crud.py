from sqlalchemy.orm import Session
import models, schemas

# 申請一覧取得
def get_oss_applications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.OssApplication).offset(skip).limit(limit).all()

# ユーザ登録
def create_oss_application(db: Session, ossApplication: schemas.OssApplication):
    db_oss_application = models.OssApplication(name_of_applicant=ossApplication.name_of_applicant, pc_id=ossApplication.pc_id, name_of_oss=ossApplication.name_of_oss, version_of_oss=ossApplication.version_of_oss, application_date=ossApplication.application_date, approval=ossApplication.approval, approval_date=ossApplication.approval_date)
    db.add(db_oss_application)
    db.commit()
    db.refresh(db_oss_application)
    return db_oss_application