from typing import Generator
from sqlalchemy.orm import Session
import database as _database
import models 
import schemas 

def _add_tables():
    _database.Base.metadata.create_all(bind=_database.engine)

def get_db() -> Generator[Session, None, None]:
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_contact(contact: schemas.CreateContact, db: Session) -> models.Contact:
    db_contact = models.Contact(**contact.model_dump())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_all_contacts(db: Session) -> list[schemas.Contact]:
    contacts = db.query(models.Contact).all()
    return [schemas.Contact.model_validate(c, from_attributes=True) for c in contacts]

def get_contact(contact_id:int, db: Session) -> list[schemas.Contact]:
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    return contact

def delete_contact(contact:models.Contact, db: Session):
    db.delete(contact)
    db.commit()

def update_contact( contact_data:schemas.UpdateContact, contact: models.Contact, db: Session):
    
    update_data = contact_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(contact, field, value)
    
    db.commit()
    db.refresh(contact)

    return schemas.Contact.model_validate(contact)


