from sqlalchemy.orm import Session
from database import get_session
from fastapi import Depends


class BaseService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
