from .models import User


def frontusr(request):
    uesr_id = request.session.get('user_id')
    context = {}
    try:
        front_user = User.objects.get(pk=uesr_id)
        context['front_user'] = front_user
        return context
    except:
        return context