from django.contrib.auth.permissions import Permission # type: ignore

class CanCreatePost(Permission):
    name = 'Can create post'
    codename = 'can_create_post'

class CanEditPost(Permission):
    name = 'Can edit post'
    codename = 'can_edit_post'
