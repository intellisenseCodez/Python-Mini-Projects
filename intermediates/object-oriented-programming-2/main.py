from grade_book import *

if __name__ == "__main__":

    data = [
        {"id": 1, "name": "John Holt", "score": 45},
        {"id": 2, "name": "Shina Ranbow", "score": 50},
        {"id": 3, "name": "Kiss Daniel", "score": 38},
        {"id": 4, "name": "Wole Soyinka", "score": 83},
        {"id": 5, "name": "Naira Marley", "score": 12},
    ]

    # instance
    book1 = Grade_book("Mr Olateju", "Data Science")
    book2 = Grade_book("Mr Success", "Cyber Security")

    print(book1.results(data))
    print(book1.results(data))