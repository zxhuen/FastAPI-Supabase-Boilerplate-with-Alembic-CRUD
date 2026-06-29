from sqlalchemy.orm import Session
from app.Repository.Person_Repo import create_person_repo, get_person_repo, edit_person_repo, delete_person_repo
from app.schemas.Person import PersonResponse, PersonCreate

def add_preson_services(db: Session, Create: PersonCreate):
    return create_person_repo(db, Create)

def list_person_services(db: Session):
    return get_person_repo(db)

def edit_person_services(db: Session, person_id: int, person: PersonCreate):
    return edit_person_repo(db, person_id, person)

def delete_person_services(db: Session, person_id: int):
    return delete_person_repo(db, person_id)
