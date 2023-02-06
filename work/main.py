from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models, schemas, crud
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# READ
@app.get("/oss_application", response_model=List[schemas.OssApplication])
async def read_application(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    applications = crud.get_oss_applications(db, skip=skip, limit=limit)
    return applications

#CREATE
@app.post("/oss_application", response_model=schemas.OssApplication)
async def create_application(oss_application: schemas.OssApplicationCreate, db: Session = Depends(get_db)):
    return crud.create_oss_application(db=db, ossApplication=oss_application)