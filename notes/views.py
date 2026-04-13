from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Note
from categories.models import Category


# Create your views here.



# IMPLEMENTERA PUT OCH DELETE
# PUT /api/notes/<id>/
# DELETE /api/notes/<id>/


#PUT ska hitta rätt note via id (tips loopa och jämför index) uppdatera title eller content eller båda och returnera den uppdaterade noten

#DELETE hitta rätt note via id, ta bort note, returnera ett simple meddelande till user


@csrf_exempt
def create_note(request):
    if request.method == "GET":
        notes = Note.objects.select_related("category").all()

        data = []

        for note in notes:
            data.append({
                "id": note.id,
                "title": note.title,
                "content": note.content,
                "category": {
                    "id": note.category.id,
                    "name": note.category.name
                }
            })
            return JsonResponse(data, safe=False)

    elif request.method == "POST":
        body = json.loads(request.body)

        category_id = body.get("category_id")

        if not category_id:
            return JsonResponse(
                {"error": "category id is required"},
                status=400
            )
        
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return JsonResponse(
                {"error": "category not found"},
                status=404
            )    



        note = Note.objects.create(
            title=body.get("title"),
            content=body.get("content"),
            category=category
        )

        return JsonResponse({
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "category": {
                    "id": note.category.id,
                    "name": note.category.name
                }
        }, status=201)
    
    return JsonResponse({"error": "Method not allowed"}, status=405)

