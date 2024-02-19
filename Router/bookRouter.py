from fastapi import APIRouter,HTTPException, Depends
from connection.connection import session
from schema.book_schema import BookSchema
from model.book import book_model
from sqlalchemy.orm import Session




book = APIRouter()

                            ###***CRUD TABLE book***###
                     

@book.post("/api/Create_book", tags=["CrudBook"])
def create_book(data_book: BookSchema):
    existing_book = session.query(book_model).filter_by(id=data_book.id).first()
    if existing_book:
        session.commit()
        raise HTTPException(status_code=400, detail=f"User {data_book.id} aleready exists")
    new_book = book_model(id = data_book.id, title=data_book.title, authors=data_book.authors, language=data_book.language, subject=data_book.subject, 
                          pages=data_book.pages, extension=data_book.extension, size=data_book.size, summary=data_book.summary)
    
    session.add(new_book)
    session.commit()
    #session.refresh(new_user)   
    return new_book

@book.get("/api/read_book_by_id/{book_id}", tags=["CrudBook"])
def get_book(id: int):
    book = session.query(book_model).get(id)
    if not book:
        raise HTTPException(404,f"Book {id} not found")
    return book


@book.get("/api/books", tags=["Books"])
def get_all_books():
    # Obtenemos todos los libros de la base de datos utilizando la sesión
    books = session.query(book_model).all()
    # Convertimos los objetos BookModel a diccionarios manualmente
    books_data = []
    for book in books:
        book_dict = {
            "id": book.id,
            "title": book.title,
            "authors": book.authors,
            "language": book.language,
            "subject": book.subject,
            "pages": book.pages,
            "extension": book.extension,
            "size": book.size,
            "summary": book.summary
        }
        books_data.append(book_dict)
    return books_data


@book.put("/api/update_book/{book_id}", tags=["CrudBook"])
def update_book(data_update: BookSchema , book_id: int):
    db_book = session.query(book_model).filter(book_model.id == book_id).first()
    if db_book:
        # Actualiza los atributos del usuario con los valores proporcionados en usuario_actualizado
        for key, value in data_update.dict().items():
            setattr(db_book, key, value)
        session.commit()
        session.refresh(db_book)
        return {"message": "book updated successfully"}
    session.commit()
    raise HTTPException(404, f"Id {book_id} not found")

@book.delete("/api/delete_book/{book_id}", tags=["CrudBook"])
def delete_book(book_id: int):
    db_book = session.query(book_model).filter(book_model.id == book_id).first()

    if db_book:
        session.delete(db_book)
        session.commit()
        return {"message": "Book deleted successfully"}
    session.commit()
    raise HTTPException(404, f"id {book_id} not found")
