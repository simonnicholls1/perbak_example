from core.data_services.models.ItemModel import Item


class ItemDataService:

    def __init__(self):
        pass

    def get_items(self):
        list_items = [Item(1, 'Test1'), Item(2, 'Test2')]
        return list_items
