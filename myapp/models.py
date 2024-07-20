from django.db import models
 
def get_image_upload_path(instance, filename):
    return f'images/{filename}'
 
def get_resized_image_upload_path(instance, filename):
    return f'resized_images/{filename}'
 
class UploadedImage(models.Model):
    image  = models.ImageField(upload_to=get_image_upload_path, default='images/default.jpg')
    processed_image = models.ImageField(upload_to=get_resized_image_upload_path,null=True, blank=True, default='resized_images/default.jpg')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    license_plate_text = models.TextField(null=True, blank=True)  # New field to store the translated text
