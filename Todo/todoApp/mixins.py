from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .models import Todo
from django.http import Http404

user = Todo.user

class UserRequiredMixin(object):
    @classmethod
    def as_view(self, *args, **kwargs):
        view = super(UserRequiredMixin, self).as_view(*args, **kwargs)
        return UserRequiredMixin(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(UserRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404

class LoginRequiredMixin(object):
    @classmethod
    def as_view(self, *args, **kwargs):
        view = super(LoginRequiredMixin, self).as_view(*args, **kwargs)
        return login_required(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


