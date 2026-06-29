from sqlalchemy.orm import Session
from app.models.Person import Person
from app.schemas.Person import PersonCreate, PersonResponse

def create_person_repo(db: Session, Persons: PersonCreate):
    db_person = Person(**Persons.model_dump())

    db.add(db_person)
    db.commit()
    db.refresh(db_person)

    return db_person

def get_person_repo(db: Session):
    return db.query(Person).all()

def edit_person_repo(db: Session, person_id: int, person: PersonCreate):
    person_from_db = (
        db.query(Person)
        .filter(Person.id == person_id)
        .first()
    )

    if person_from_db is None:
        return None
    
    person_from_db.last_name = person.last_name
    person_from_db.first_name = person.first_name
    person_from_db.middle_name = person.middle_name
    person_from_db.age = person.age

    db.commit()
    db.refresh(person_from_db)

    return person_from_db


def delete_person_repo(db: Session, person_id: int):
    person = db.query(Person).filter(Person.id == person_id).first()

    if person is None:
        return None
    
    db.delete(person)
    db.commit()

    return person