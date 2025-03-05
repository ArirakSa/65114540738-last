from django.shortcuts import render
from .models import *

# Create your views here.

def SearchName(request):
    search_term = request.GET.get('q', '')  # รับคำค้นหาจาก URL ด้วย GET
    # หากมีคำค้นหาให้กรองคอร์สที่มีชื่อคล้ายกับคำค้นหา
    courses = Course.objects.filter(name__icontains=search_term) if search_term else Course.objects.all()  
    return render(request, 'course/search_results.html', {'courses': courses, 'search_term': search_term})  # ส่งข้อมูลไปที่ template
