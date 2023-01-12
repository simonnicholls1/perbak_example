from models import ItemModel


class ItemDataService:

    def __init__(self):
        pass

    def get_items(self):
        list_items = [ItemModel(1, 'Test1'), ItemModel(2, 'Test2')]
        return list_items
