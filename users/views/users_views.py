from django.shortcuts import render
from django.http import JsonResponse
from ..models import User, DailyEntry
from django.forms.models import model_to_dict
import json

def save(request):
    try:
         data = json.loads(request.body.decode("utf-8"))
         name = data.get("name")
         weight = data.get("weight")
         if name is not None and weight is not None:
            user = User.objects.create(name=name, weight=weight, daily_goal=(float(weight) * 35))
            users_data = User.objects.filter(id=user.id).values() 
            return JsonResponse({"message": "User created successfully", "user": list(users_data)})
         else:
            return JsonResponse({"error": "Invalid data provided"})
    except Exception as e:
        return JsonResponse({"error": str(e)})

    
def read(request):
    users_queryset = User.objects.all().prefetch_related('dailyentry_set') 
    users_data = []

    for user in users_queryset:
        user_data = {
            "id": user.id,
            "name": user.name,
            "weight": user.weight,
            "daily_goal": user.daily_goal,
            "entries": list(user.dailyentry_set.values('id', 'daily_quantity', 'date', 'achieve_goal'))
        }
        users_data.append(user_data)

    return JsonResponse({"users": users_data})

def update(request, id):
    data = json.loads(request.body.decode("utf-8"))
    update_params = data.get("update_params") 
    
    try:
        user = User.objects.get(id=id)
        
        for field, value in update_params.items():
            setattr(user, field, value) 
        
        user.save() 
        updated_user_data = model_to_dict(user)
        return JsonResponse({"message": "User updated successfully", "user": updated_user_data })
    
    except Exception as e:
        return JsonResponse({"error": str(e)})

def delete(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete() 
        
        return JsonResponse({"message": "User deleted successfully"})
    
    except Exception as e:
        return JsonResponse({"error": str(e)})

def read_id(request, id):
    try:
        user = User.objects.get(id=id)
        user_data = model_to_dict(user)
        
        entrys_queryset = DailyEntry.objects.filter(user=user)
        entrys_data = list(entrys_queryset.values())
        
        return JsonResponse({"user": user_data, "entrys": entrys_data})
    except Exception as e:
        return JsonResponse({"error": str(e)})