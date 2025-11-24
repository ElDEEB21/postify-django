from django.db import models
import base64


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.BinaryField(blank=True, null=True)
    avatar_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_avatar_data_url(self):
        if self.avatar and self.avatar_type:
            base64_data = base64.b64encode(self.avatar).decode('utf-8')
            return f"data:{self.avatar_type};base64,{base64_data}"
        return None
