from types import new_class

import pytest
from app import library
from  app import  book


library1=library.Library()

def test_add_book():
    b=book.Book("abc","avi")
    len1=len(library1.books)
    library1.add_book(b)
    assert len(library1.books)==len1+1


def test_add_user():
    len1=len(library1.users)
    library1.add_user("rut")
    assert len(library1.users)==len1+1


def test_check_out_book():
    b = book.Book("abc", "avi")
    print()
    print(b.is_checked_out)
    library1.checked_out_books("rut",b)
    print(b.is_checked_out)
    assert b.is_checked_out==True


def test_return_book():
    b = book.Book("abc", "avi")
    print()
    print(b.is_checked_out)
    library1.return_book("rut",b)
    print(b.is_checked_out)
    assert b.is_checked_out==False


def test_search_books():
    assert library1.search_books("ssss")==[]




