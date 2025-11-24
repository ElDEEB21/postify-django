from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    excerpt = models.TextField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    cover_image = models.BinaryField(blank=True, null=True)
    cover_image_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_cover_image_data_url(self):
        if self.cover_image and self.cover_image_type:
            import base64
            base64_data = base64.b64encode(self.cover_image).decode('utf-8')
            return f"data:{self.cover_image_type};base64,{base64_data}"
        return None
