from carts.models import Cart


def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    # else:
    #     return Cart.objects.filter(session_key=request.session.session_key)