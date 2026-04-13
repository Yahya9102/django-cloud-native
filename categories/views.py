from django.shortcuts import render
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Category

# Create your views here.

@csrf_exempt
def create_category(request):
    if request.method == "GET":
        
        categories = Category.objects.all()

        data = []

        for category in categories:
            data.append({
                "id": category.id,
                "name": category.name
                
            })
            return JsonResponse(data, safe=False)
        

    elif request.method == "POST":
        body = json.loads(request.body)

        name = body.get("name")

        if not name:
            return JsonResponse(
                {"error": "category name is required"},
                status=400
            )
        

        try:
            category = Category.objects.create(name=name)
        except Category.DoesNotExist:
            return JsonResponse(
                {"error": "category not found"},
                status=404
            )    


        return JsonResponse({
                "id": category.id,
                "name": category.name
                 },
                status=201
            )    

    return JsonResponse({"error": "Method not allowed"}, status=405)

