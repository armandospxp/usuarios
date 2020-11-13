from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView, CreateView
from apps.usuarios.forms import RegistroForm
from apps.usuarios.decorator import *

PERMISO_VISTA_USER = ['administrador', '123']


class RegistroForm(CreateView):
    model = User
    template_name = "usuario/usuario_form.html"
    form_class = RegistroForm
    success_url = reverse_lazy("listar_usuario")



class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "core/login.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)



class UsuarioList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'usuario/lista_usuarios.html'
    context_object_name = 'user_list'
    paginate_by = 10



class editarUsuario(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['email', 'first_name', 'last_name']
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy("listar_usuario")


class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('listar_usuario')
    context_object_name = 'usuario_delete'

