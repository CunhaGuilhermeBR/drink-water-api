from django.test import TestCase
from users.views.users_views import save, read, delete, read_id
from users.views.entrys_views import drink_water
from django.http import JsonResponse
from users.models import User
import json

class UserViewsTestCase(TestCase):
    def test_drink_water(self):
        user = User.objects.create(name="João", weight="70", daily_goal=(float(70) * 35))
        data = {"user_id": user.id, "quantity": 500}
        request = self.client.post("/drink_water", json.dumps(data), content_type="application/json")
        response = drink_water(request)
        
        entry = DailyEntry.objects.get(user=user, date=date.today())
        
        self.assertEqual(entry.daily_quantity, 500)
        self.assertFalse(entry.achieve_goal)
        self.assertEqual(entry.remaining_quantity, user.daily_goal - entry.daily_quantity)
        
        self.assertEqual(response.status_code, JsonResponse({"message": "Daily quantity and goal updated successfully"}).status_code)



    def test_save_user(self):
        data = {"name": "João", "weight": "70"}
        request = self.client.post("/", json.dumps(data), content_type="application/json")
        response = save(request)
        self.assertEqual(response.status_code, JsonResponse({"message": "User created successfully", "user": [{'id': 3, 'name': 'João', 'weight': '70.0', 'daily_goal': 2450.0}]}).status_code)
    
    def test_read_users(self):
        request = self.client.get("/")
        response = read(request)
        self.assertEqual(response.status_code, JsonResponse({"users": [{'id': 1, 'name': 'Jose', 'weight': '80.0', 'daily_goal': 2800.0, 'entries': []}, {'id': 2, 'name': 'Maria', 'weight': '60.0', 'daily_goal': 2100.0, 'entries': []}]}).status_code)
    
    def test_read_user_by_id(self):
        user_id = 1
        request = self.client.get(f"/{user_id}")
        response = read_id(request, id=user_id)
        self.assertEqual(response.status_code, JsonResponse({"user": {'id': user_id, 'name': 'Maria', 'weight': '60.0', 'daily_goal': 2100.0}, "entrys": []}).status_code)

    def test_delete_user(self):
        user_id = 1  
        request = self.client.delete(f"/{user_id}")
        response = delete(request, id=user_id)
        self.assertEqual(response.status_code, JsonResponse({"message": "User deleted successfully"}).status_code)
    
    