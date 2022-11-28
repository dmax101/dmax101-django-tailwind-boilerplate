from django.shortcuts import render
import requests
import pprint

from .models.errors import ErrorCode
from .models.user import Name, User

# Create your views here.


def index(request):

    base_context = {
        'company_name': 'Unilever',
        'application_name': 'Direct Factory Delivery',
        'version': '1.0.0',
        'user': None,
        'status': ErrorCode.NO_ERROR.value
    }

    context = {**base_context, **{'title': 'Login'}}

    try:
        user = requests.get('https://randomuser.me/api/').json()['results'][0]

        first_name = user['name']['first']
        last_name = user['name']['last'][0],
        email = user['email']

        pprint.pprint(user)

        user_instance = User(
            name=Name(first=first_name, last=last_name), email=email)

        context['user'] = user_instance

    except Exception as e:
        pprint.pprint(e)
        context['status'] = ErrorCode.ERROR_GENERIC.value
        context['status']['message'] = str(e)

    return render(request, 'myapp/index.html', context)
