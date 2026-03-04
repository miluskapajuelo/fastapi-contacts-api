## write API


from fastapi import FastAPI, Depends, HTTPException
import schemas 
from sqlalchemy.orm import Session
import database as _database
import services




app = FastAPI()

@app.on_event("startup")
def startup():
    import models 
    _database.Base.metadata.create_all(bind=_database.engine)

@app.get("/")
def root():
    return {"ok": True}


@app.post("/api/contacts", response_model=schemas.Contact)
def create_contact( contact: schemas.CreateContact, db:Session = Depends(services.get_db)):
    return  services.create_contact(contact=contact, db=db)


@app.get("/api/contacts", response_model=list[schemas.Contact])
def get_contacts(db: Session = Depends(services.get_db)):
    return  services.get_all_contacts(db=db)

@app.get("/api/contacts/{contact_id}/", response_model=schemas.Contact)
def  get_contact(contact_id: int, db: Session = Depends(services.get_db)):
    return services.get_contact(contact_id=contact_id, db=db)

@app.delete("/api/contacts/{contact_id}/")
def  delete_contact(contact_id: int, db: Session = Depends(services.get_db)):
    contact = services.get_contact(contact_id=contact_id, db=db)
    if contact is None:
        raise HTTPException(status_code=404, detail="user does not exist")
    services.delete_contact(contact, db=db)
    return {"message": "successfully deleted the contact"}

@app.put("/api/contacts/{contact_id}/", response_model=schemas.Contact)
def update_contact(
    contact_id: int, 
    contact_data:schemas.UpdateContact,
    db: Session = Depends(services.get_db)):

    contact = services.get_contact(db=db, contact_id=contact_id )
    if contact is None:
        raise HTTPException(status_code=404, detail="Not found")
    
    return services.update_contact(contact_data=contact_data, contact=contact, db=db)