class Book:
    def __init__(self, title: str, author: str, year: int, id: int = None, status: str = "в наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """Преобразует объект Book в словарь для сериализации"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }