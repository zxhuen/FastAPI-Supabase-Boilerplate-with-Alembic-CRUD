from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.Person import PersonCreate, PersonResponse
from app.services.Person_Services import add_preson_services, list_person_services, edit_person_services


router = APIRouter(prefix="/Person", tags=["Person"])

@router.post("/", response_model=PersonResponse)
def add_person(person: PersonCreate, db: Session = Depends(get_db)):
    return add_preson_services(db, person)

@router.get("/", response_model= list[PersonResponse])
def get_person(db: Session = Depends(get_db)):
    return list_person_services(db)

@router.put("/{person_id}", response_model=PersonResponse)
def edit_person(person_id: int, person: PersonCreate, db: Session = Depends(get_db)):
    persons = edit_person_services(db, person_id, person)

    if persons is None:
        raise HTTPException(
            status_code=404,
            detail="no person found"
        )   
    
    return persons