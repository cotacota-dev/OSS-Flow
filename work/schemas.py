from pydantic import BaseModel, Field
import datetime
from typing import Union

# ユーザ登録時に必要な型
class OssApplicationCreate(BaseModel):
    name_of_applicant: str 
    pc_id :str
    name_of_oss :str
    version_of_oss : str
    application_date : datetime.datetime
    approval :bool
    approval_date : Union[datetime.datetime, None] = Field(default=None)
    
# ユーザ作成時に受け取る型
class OssApplication(OssApplicationCreate):
    application_id: int

    class Config:
        orm_mode = True