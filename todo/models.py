from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def get_default_user():
    # Return a default user (e.g., the first user or a specific user)
    return User.objects.first().id

class Todo(models.Model):
    """
    Represents a todo item with an owner, title, description, completion status,
    and timestamps for creation and updates.
    
    Attributes:
        owner (User): The user who owns the todo item.
        title (str): Title of the todo item.
        description (str): Detailed description of the todo item.
        completed (bool): Status indicating if the todo is completed.
        created_at (datetime): The date and time when the todo was created.
        updated (datetime): The date and time when the todo was last updated.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """Returns the title of the todo item."""
        return self.title

class Profile(models.Model):
    """
    Represents a user's profile in the application.

    Attributes:
        user (User): The user to whom this profile belongs.
        image (ImageField): The profile image of the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/', default='default_profile.jpg'
    )

    def __str__(self):
        """Returns the user's username with an appended string for profile identification."""
        return f"{self.user.username}'s profile"

def create_Profile(sender, instance, created, **kwargs):
    """
    Signal receiver that creates a Profile instance whenever a new User instance is created.

    Args:
        sender (Model): The model class that sent the signal.
        instance (User): The instance of the model that was saved.
        created (bool): A boolean indicating whether a new record was created.
        kwargs: Additional keyword arguments.
    """
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_Profile, sender=User)
