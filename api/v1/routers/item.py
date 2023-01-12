from fastapi import status, HTTPException, Depends, APIRouter
from core.services.item_serivce import ItemService
from core.data_services.item_data_service import ItemDataService

router = APIRouter(
    prefix='/item',
    tags=['Item']
)


item_service = ItemService(ItemDataService())

@router.get("/item")
def get_items():

    items = item_service.get_all_items()

    if items is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Items not found")
    return items

@router.get("/item/{id}")
def get_items_by_id(id):

    item = item_service.get_items_by_id(id)

    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item not found with id {0}".format(id))
    return item