from django.shortcuts import render, redirect
from django.conf import settings
from PIL import Image
import os
from .forms import ImageUploadForm
from .models import UploadedImage

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()

            # Path to the original image
            original_image_path = uploaded_image.image.path

            # Open the original image
            img = Image.open(original_image_path)

            # Resize the image
            img = img.resize((800, 800), Image.ANTIALIAS)  # Adjust dimensions as needed

            # Path to save the resized image
            resized_image_dir = os.path.join(settings.MEDIA_ROOT, 'resized_images')
            resized_image_path = os.path.join(resized_image_dir, os.path.basename(original_image_path))

            # Ensure the resized_images directory exists
            os.makedirs(resized_image_dir, exist_ok=True)

            # Save the resized image
            img.save(resized_image_path)

            return redirect('display_image')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def display_image(request):
    resized_images_path = os.path.join(settings.MEDIA_ROOT, 'resized_images')
    latest_image = None

    if os.path.exists(resized_images_path):
        # Get list of files in resized_images folder
        images = sorted(
            os.listdir(resized_images_path), 
            key=lambda x: os.path.getctime(os.path.join(resized_images_path, x)), 
            reverse=True
        )
        if images:
            latest_image = os.path.join('resized_images', images[0])  # Store relative path

    return render(request, 'display_image.html', {
        'latest_image': latest_image,
        'MEDIA_URL': settings.MEDIA_URL
    })
