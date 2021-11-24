from api_client import DevWeekAPIClient


data = [
    {"author_name": "Constance Adkins", "title": "Angel Of Earth", "page_count": 173, "price": 7.92},
    {"author_name": "Syed Lowry", "title": "Butcher Of The Land", "page_count": 190, "price": 6.69},
    {"author_name": "Clara Macleod", "title": "Priests Of The World", "page_count": 101, "price": 5.43},
    {"author_name": "Alima Crouch", "title": "Robots Of Utopia", "page_count": 160, "price": 9.74},
    {"author_name": "Andreea Steadman", "title": "Men And Spies", "page_count": 131, "price": 8.95},
    {"author_name": "Constance Adkins", "title": "Serpents And Heroes", "page_count": 149, "price": 3.98},
    {"author_name": "Jon-Paul East", "title": "Love Of Tomorrow", "page_count": 185, "price": 4.0},
    {"author_name": "Clara Macleod", "title": "Argument Of The End", "page_count": 153, "price": 8.5},
    {"author_name": "Andreea Steadman", "title": "Weep For My Past", "page_count": 188, "price": 8.93},
    {"author_name": "Constance Adkins", "title": "Vanish In The Mines", "page_count": 189, "price": 8.01},
]

client = DevWeekAPIClient()

print(client.get_books().to_string())
print()

client.provision_database(data)

print(client.get_books().to_string())


