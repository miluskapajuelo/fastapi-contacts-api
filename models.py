import datetime as _dt
from datetime import timezone
import sqlalchemy 
import database

class Contact(database.Base):
    __tablename__ = "contacts"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(100), index=True, nullable=False)
    last_name = sqlalchemy.Column(sqlalchemy.String(100), index=True, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String(255), index=True, unique=True, nullable=False)
    phone_number = sqlalchemy.Column(sqlalchemy.String(30), index=True, unique=True, nullable=False)
    date_created = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), default=lambda: _dt.datetime.now(_dt.timezone.utc), nullable=False)

    
    