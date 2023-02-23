#new_book = Book(id=1, title="Harry Potter", author="J.K. Rowling", rating=9.3)
    #db.create_all()
    #db.session.add(new_book)
    #db.session.commit()
    #----------READ ALL RECORDS
    # all_books = db.session.query(Book).all()
    #----------READ A PARTICULAR RECORD BY QUERY
    # book = Book.query.filter_by(title="Harry Potter").first()
    #----------UPDATE A PARTICULAR RECORD BY QUERY
    # book_to_update = Book.query.filter_by(title="Harry Potter").first()
    # book_to_update.title = "Harry Potter and the Chamber of Secrets"
    # db.session.commit()
    #----------UPDATE A RECORD BY PRIMARY KEY
    # book_id = 1
    # book_to_update = Book.query.get(book_id)
    # book_to_update.title = "Harry Potter and the Goblet of Fire"
    # db.session.commit()
    #----------DELETE A PARTICULAR RECORD BY PRIMARY KEY
    # book_id = 1
    # book_to_delete = Book.query.get(book_id)
    # db.session.delete(book_to_delete)
    # db.session.commit()