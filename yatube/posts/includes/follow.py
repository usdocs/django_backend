from django.contrib.auth.decorators import login_required

from ..models import Follow


@login_required
def follow(request, author):
    return Follow.objects.filter(author=author, user=request.user).exists()
