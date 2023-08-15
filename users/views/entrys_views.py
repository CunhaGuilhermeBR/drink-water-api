from django.shortcuts import render
from django.http import JsonResponse
from ..models import DailyEntry, User
from django.forms.models import model_to_dict
import json
from datetime import datetime, date

def save_entrys(user_id):
    try:
        user = User.objects.get(pk=user_id)  
        entry = DailyEntry.objects.create(user=user, daily_quantity=quantity)
        if entry.daily_quantity >= user.daily_goal:
            entry.achieve_goal = True
            entry.reimaning_quantity = 0
        else:
            entry.remaining_quantity = user.daily_goal - entry.daily_quantity
        entry_data = DailyEntry.objects.filter(id=entry.id).values() 
        return JsonResponse({"message": "Entry created successfully", "entry": list(entry_data)})
     
    except Exception as e:
        return JsonResponse({"error": str(e)})

def drink_water(request):
    data = json.loads(request.body.decode("utf-8"))
    user_id = data.get("user_id")
    quantity = data.get("quantity")

    try:
        if user_id is not None and quantity is not None and quantity > 0:
            user = User.objects.get(pk=user_id)
            today = date.today()
            entry, created = DailyEntry.objects.get_or_create(user=user, date=today)
    
            entry.daily_quantity += quantity
            
            if entry.daily_quantity >= user.daily_goal:
                entry.achieve_goal = True
                entry.remaining_quantity = 0
            else:
                entry.remaining_quantity = user.daily_goal - entry.daily_quantity

            entry.save()

            return JsonResponse({"message": "Daily quantity and goal updated successfully"})
        else:
            return JsonResponse({"error": "Invalid data provided"})
    except DailyEntry.DoesNotExist:
        result = save_entrys(user_id, quantity)
        return result
    except Exception as e:
        return JsonResponse({"error": str(e)})
    
def read_entrys(request): 
    entrys_queryset = entry.objects.all()
    entrys_data = list(entrys_queryset.values())
    return JsonResponse({"entrys": entrys_data})

def read_id_entrys(request, id):
    try:
        entry = DailyEntry.objects.get(id=id)
        entry_data = model_to_dict(entry)
        return JsonResponse({"entry": entry_data })
    except Exception as e:
        return JsonResponse({"error": str(e)})