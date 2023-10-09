from django.http import JsonResponse
from .models import Item

def item_list(request):
    # Populate the items list with dictionaries
    items = [
        {"name": "Item 1", "description": "Description for Item 1"},
        {"name": "Item 2", "description": "Description for Item 2"},
    ]

    # Return a JSON response with the items
    return JsonResponse({"items": items})
