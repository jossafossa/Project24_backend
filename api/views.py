from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'friendcircles': reverse('friendcircle-list', request=request, format=format),
        'prikmuur': reverse('prikmuur-list', request=request, format=format),
        'interests': reverse('interest-list', request=request, format=format),
    })
