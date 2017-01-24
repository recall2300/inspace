from django.shortcuts import render_to_response
from functools import wraps
from .models import Employee

USER_FIELDS = ['username', 'email']


def partial(func):
    @wraps(func)
    def wrapper(strategy, pipeline_index, *args, **kwargs):
        out = func(strategy=strategy, pipeline_index=pipeline_index,
                   *args, **kwargs) or {}
        if not isinstance(out, dict):
            values = strategy.partial_to_session(pipeline_index, *args,
                                                 **kwargs)
            strategy.session_set('partial_pipeline', values)
        return out

    return wrapper


def create_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    # fields = dict((name, kwargs.get(name, details.get(name)))
    #               for name in backend.setting('USER_FIELDS', USER_FIELDS))
    fields = {'username': details.get('last_name') + details.get('first_name'), 'email': details.get('email'),
              'gender': kwargs.get('response').get('gender'), 'nickname': kwargs.get('response').get('nickname'),
              'image': kwargs.get('response').get('image').get('url')}
    if not fields:
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }


@partial
def enter_user_information_at_initial_signup(backend, details, response, request, user, is_new=False, *args, **kwargs):
    if backend.name == 'google-oauth2' and is_new:
        data = backend.strategy.request_data()
        if data.get('department') is None:
            return render_to_response('registration/signup_option.html', {'details': details, })
        else:
            return {'department': data.get('department')}


def save_profile(backend, user, response, is_new, *args, **kwargs):
    if backend.name == 'google-oauth2' and is_new:
        data = backend.strategy.request_data()

        user.department = data.get('department', '')
        user.position = data.get('position', '')
        user.available_leave_day = data.get('available_leave_day', 15.0)
        user.contact = data.get('contact', '')
        user.signature_image = data.get('signature_image', '')
        user.save()

def remove_profile(backend, user, *args, **kwargs):
    print("test")
    employee = Employee.objects.get(id=user.id)
    employee.delete()

