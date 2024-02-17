from app.views import *
import os
from django.views.decorators.csrf import csrf_exempt
from core.settings import BASE_DIR
from config import DOMAIN

def get_file(request, path):
    file = open(os.path.join(BASE_DIR, f'files/{path}'), 'rb')
    return FileResponse(file)

def get_image(request, file_name, folder='images'):
    file = open(os.path.join(BASE_DIR, f'files/{folder}/{file_name}'), 'rb')
    return FileResponse(file)

@csrf_exempt
def upload_image(request, folder=''):
    if request.method == 'POST':
        print(request.FILES, request.POST)
        uploaded_file = request.FILES['file']
        # print(uploaded_file.__dict__)
        upload_dir = f'files/{folder}'
        os.makedirs(upload_dir, exist_ok=True)
        # Create a unique filename for the uploaded file (you can customize this)
        file_format = str(uploaded_file.name).split('.')[-1]
        file_name = generate_random_file_name() + '.' + file_format
        file_path = os.path.join(upload_dir, file_name)
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        return JsonResponse({'secure_url': f'{DOMAIN}/files/{folder}/{file_name}'})

    return HttpResponse('')
