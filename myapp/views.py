# views.py
from django.shortcuts import render, redirect
from django.conf import settings
import os
from .forms import ImageUploadForm
from .models import UploadedImage
import subprocess

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()

            # Path to the original image
            original_image_path = uploaded_image.image.path

            # Run YOLOv9 detect.py script
            detect_script_path = os.path.join(settings.BASE_DIR, 'myapp', 'yolov9', 'detect.py')
            weights_path = os.path.join(settings.BASE_DIR, 'myapp', 'yolov9', 'best.pt')
            source_image_path = original_image_path

            command = [
                'python', detect_script_path,
                '--conf', '0.1',
                '--weights', weights_path,
                '--source', source_image_path
            ]

            subprocess.run(command, check=True)

            resized_image_dir = os.path.join(settings.MEDIA_ROOT, 'resized_images')
            os.makedirs(resized_image_dir, exist_ok=True)


            resized_image_path = os.path.join(resized_image_dir, os.path.basename(original_image_path))
            uploaded_image.processed_image.name = resized_image_path
            



           
            # Read translated text from file and save it to the model
            text_files_subdir = 'text_files'
            translated_text_path = os.path.join(resized_image_dir, text_files_subdir, 'translated_text.txt')
            if os.path.exists(translated_text_path):
                with open(translated_text_path, 'r') as f:
                    translated_text = f.read()
                uploaded_image.license_plate_text = translated_text

            uploaded_image.save()

            return redirect('display_image')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def display_image(request):
    resized_images_path = os.path.join(settings.MEDIA_ROOT, 'resized_images')
    latest_image = None
    translated_text = ""

    if os.path.exists(resized_images_path):
        # Get list of files in resized_images folder
        images = sorted(
            os.listdir(resized_images_path), 
            key=lambda x: os.path.getctime(os.path.join(resized_images_path, x)), 
            reverse=True
        )
        if images:
            latest_image = os.path.join('resized_images', images[0])  # Store relative path

    # Get the latest uploaded image from the database
    uploaded_image = UploadedImage.objects.order_by('-id').first()
    if uploaded_image:
        translated_text = uploaded_image.license_plate_text

    return render(request, 'display_image.html', {
        'latest_image': latest_image,
        'translated_text': translated_text,
        'MEDIA_URL': settings.MEDIA_URL
    })



def view_parking_spaces(request):
    # Fetch all uploaded images from the database
    uploaded_images = UploadedImage.objects.all()
    total_parking = 20
    occupied_spaces = uploaded_images.count()
    available_spaces = total_parking - occupied_spaces
    
    return render(request, 'view_parking_spaces.html', {
        'uploaded_images': uploaded_images,
        'total_parking': total_parking,
        'occupied_spaces': occupied_spaces,
        'available_spaces': available_spaces
    })


def teams(request):
    # Logic to retrieve and display team information
    return render(request, 'teams.html', {
        # Add context variables if needed
    })


# # myapp/views.py
# from django.shortcuts import render, redirect
# from django.conf import settings
# import os
# from .forms import ImageUploadForm
# from .models import UploadedImage
# import subprocess

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_image = form.save()

#             # Path to the original image
#             original_image_path = uploaded_image.image.path

#             # Run YOLOv9 detect.py script
#             detect_script_path = os.path.join(settings.BASE_DIR, 'myapp', 'yolov9', 'detect.py')
#             weights_path = os.path.join(settings.BASE_DIR, 'myapp', 'yolov9', 'best.pt')
#             source_image_path = original_image_path

#             command = [
#                 'python', detect_script_path,
#                 '--conf', '0.1',
#                 '--weights', weights_path,
#                 '--source', source_image_path
#             ]

#             subprocess.run(command, check=True)

#             resized_image_dir = os.path.join(settings.MEDIA_ROOT, 'resized_images')
#             os.makedirs(resized_image_dir, exist_ok=True)

#             resized_image_path = os.path.join(resized_image_dir, os.path.basename(original_image_path))
#             uploaded_image.processed_image.name = resized_image_path

#             # Read translated text from file and save it to the model
#             text_files_subdir = 'text_files'
#             translated_text_path = os.path.join(resized_image_dir, text_files_subdir, 'translated_text.txt')
#             if os.path.exists(translated_text_path):
#                 with open(translated_text_path, 'r') as f:
#                     translated_text = f.read()
#                 uploaded_image.license_plate_text = translated_text

#             uploaded_image.save()

#             return redirect('display_image')
#     else:
#         form = ImageUploadForm()
#     return render(request, 'upload_image.html', {'form': form})

# def display_image(request):
#     resized_images_path = os.path.join(settings.MEDIA_ROOT, 'resized_images')
#     latest_image = None
#     translated_text = ""

#     if os.path.exists(resized_images_path):
#         # Get list of files in resized_images folder
#         images = sorted(
#             os.listdir(resized_images_path), 
#             key=lambda x: os.path.getctime(os.path.join(resized_images_path, x)), 
#             reverse=True
#         )
#         if images:
#             latest_image = os.path.join('resized_images', images[0])  # Store relative path

#     # Get the latest uploaded image from the database
#     uploaded_image = UploadedImage.objects.order_by('-id').first()
#     if uploaded_image:
#         translated_text = uploaded_image.license_plate_text

#     return render(request, 'display_image.html', {
#         'latest_image': latest_image,
#         'translated_text': translated_text,
#         'MEDIA_URL': settings.MEDIA_URL
#     })

# def view_parking_spaces(request):
#     return render(request, 'view_parking_spaces.html')

# def teams(request):
#     return render(request, 'teams.html')
