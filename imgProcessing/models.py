from django.db import models
from .utils import get_filtered_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
FILTER_CHOICES= (
    ('NO_FILTER', 'no filter'),
    ('COLORIZED', 'colorized'),
    ('GRAYSCALE', 'grayscale'),
    ('GAUSSIAN_BLUR', 'gaussian blur'),
    ('SHARPEN', 'sharpen'),
    ('NOISE_REDUCTION', 'noise reduction'),
    ('BILATERAL_FILTER', 'bilateral filter'),
    ('THRESHOLD', 'threshold')
)

class Upload(models.Model):
    image = models.ImageField(upload_to='images')
    filter = models.CharField(max_length=50, choices=FILTER_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        
        # open image
        pil_img = Image.open(self.image)

        cv_img = np.array(pil_img)
        img = get_filtered_image(cv_img, self.action)

        im_pil = Image.fromarray(img)

        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)