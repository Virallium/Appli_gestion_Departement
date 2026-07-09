from django.http import JsonResponse
from django.db import connection

def supabase_health_check(request):
    try:
        # On force Django à faire une vraie requête SQL rapide sur Supabase
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
        return JsonResponse({"status": "OK", "database": "connected"}, status=200)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)