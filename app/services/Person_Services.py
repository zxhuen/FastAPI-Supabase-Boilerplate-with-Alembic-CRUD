from sqlalchemy.orm import Session
from app.repository import create_person_repo, get_person_repo, edit_person_repo, delete_person_repo
from app.schemas import PersonCreate
from fastapi import HTTPException

def add_person_services(db: Session, Create: PersonCreate):
    person = create_person_repo(db, Create)

    db.add(person)
    db.commit()
    db.refresh(person)

    return person

def list_person_services(db: Session):
    return get_person_repo(db)

def edit_person_services(db: Session, person_id: int, edit_person: PersonCreate):
    person = edit_person_repo(db, person_id, edit_person)

    if person is None:
        raise HTTPException(
            status_code=404,
            detail="no person found"
        )
    
    person.last_name = person.last_name
    person.first_name = person.first_name
    person.middle_name = person.middle_name
    person.age = person.age

    db.commit()
    db.refresh(person)

    return person

def delete_person_services(db: Session, person_id: int):
    person = delete_person_repo(db, person_id)

    if person is None:
        raise HTTPException(
            status_code=404,
            detail="no person found"
        )
    
    db.delete(person)
    db.refresh(person)

    return person
