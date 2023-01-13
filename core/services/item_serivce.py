

class ItemService:

    def __init__(self, item_data_service):
        self.item_data_service = item_data_service

    def get_items_by_id(self, id: int):
        items = self.item_data_service.get_items()
        for item in items:
            if item.id == int(id):
                return item
        raise ValueError('Could not find item with ID: {0}'.format(id))

    def get_all_items(self):
        return self.item_data_service.get_items()