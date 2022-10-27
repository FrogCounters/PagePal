import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate(r"token.json")

app = firebase_admin.initialize_app(cred)

db = firestore.client()


def insert_book(title, url, text, emotions, hate_speech, author, main_img):
    data = {
        u'title': title,
        u'url': url,
        u'text': text,
        u'emotions': emotions,
        u'hate_speech': hate_speech,
        u'date_uploaded': datetime.utcnow(),
        u'author': author,
        u'main_img': main_img
    }

    db.collection("books").document(title).set(data)


def get_book(title):
    doc_ref = db.collection("books").document(title)

    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return {}


def get_all_books():
    docs = db.collection("books").stream()   # .where(u'', u'==', True)
    return docs


def insert_user_book(title, text, emotions, hate_speech, book_id):
    data = {
        u'title': title,
        u'text': text,
        u'emotions': emotions,
        u'hate_speech': hate_speech,
        u'date_uploaded': datetime.utcnow(),
        u'book_id': book_id
    }

    db.collection("user_books").document(book_id).set(data)


def get_user_book(book_id):
    doc_ref = db.collection("user_books").document(book_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return {}


if __name__ == '__main__':
    get_book("test title")
