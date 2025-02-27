from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class CreatePostUserRateThrottle(UserRateThrottle):
    scope = 'create_post_user'


class CreatePostAnonRateThrottle(AnonRateThrottle):
    scope = 'create_post_anon'

class ListPostsUserRateThrottle(UserRateThrottle):
    scope = 'list_posts_user'


class ListPostsAnonRateThrottle(AnonRateThrottle):
     scope = 'list_posts_anon'




from rest_framework.throttling import BaseThrottle
from django.core.cache import cache

class BlogRateThrottle(BaseThrottle):
    def allow_request(self, request, view):
        if request.user.is_authenticated:
            user_id = f'user_{request.user.id}'
            max_requests = 5
        else:
            user_id = f"anon_{request.META.get('REMOTE_ADDR')}"
            max_requests = 1
        
        #path =  /api/v1/posts/1
        path = request.path

        cache_key = f'throttle_{user_id}_{path}'

        hit_count = cache.get(cache_key, 0)

        if hit_count > max_requests:
            return False
        else:
            cache.set(cache_key,hit_count + 1, timeout = 60)
            return True


# class MyView(ModelViewSet):
#     throttle_classes = [RandomRateThrottle]