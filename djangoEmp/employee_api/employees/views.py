from django.http import JsonResponse


def employee_list(request):
    # Populate the employees list with dictionaries
    employees = [
        {"name": "BHOOMIKA SINGH", "id": "EMP001", "address": "Delhi"},
        {"name": "VERTIKA VERMA", "id": "EMP002", "address": "Gurgaon"},
        {"name": "YAMINI TOMAR", "id": "EMP003", "address": "Noida"},
        {"name": "SAKSHI SRIVASTAVA", "id": "EMP004", "address": "Faridabad"},
    ]

    return JsonResponse({"employees": employees})
