from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Note


# Create your views here.



# IMPLEMENTERA PUT OCH DELETE
# PUT /api/notes/<id>/
# DELETE /api/notes/<id>/


#PUT ska hitta rätt note via id (tips loopa och jämför index) uppdatera title eller content eller båda och returnera den uppdaterade noten

#DELETE hitta rätt note via id, ta bort note, returnera ett simple meddelande till user


@csrf_exempt
def create_note(request):
    if request.method == "GET":
        notes = Note.objects.all()


        data = []

        for note in notes:
            data.append({
                "id": note.id,
                "title": note.title,
                "content": note.content,
            })

            return JsonResponse(data, safe=False)

    elif request.method == "POST":
        body = json.loads(request.body)

        note = Note.objects.create(
            title=body.get("title"),
            content=body.get("content"),
        )

        return JsonResponse({
            "id": note.id,
            "title": note.title,
            "content": note.content,
        }, status=201)
    
    return JsonResponse({"error": "Method not allowed"}, status=405)

