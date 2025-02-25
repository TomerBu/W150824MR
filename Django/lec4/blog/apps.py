from django.apps import AppConfig

# settings for our blog app
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
 
    # post_save
    def perform_add_user_to_users_group(sender, instance, created, **kwargs):
        # the import is nested inside the function
        from django.contrib.auth.models import Group, User

        if not created:
            return
        group, _ = Group.objects.get_or_create(name='users')
        instance.groups.add(group)
        instance.save()
        print(f'User {instance.username} added to group {group.name}')