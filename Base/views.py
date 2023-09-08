from django.shortcuts import render
from .models import Instrumento
from django.views.generic import ListView
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Instrumento, Comentario
from .forms import ActualizacionInstrumento, FormularioCambioPassword, FormularioEdicion, FormularioNuevoInstrumento, FormularioRegistroUsuario, FormularioComentario


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class LoginPagina(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')


class RegistroPagina(FormView):
    template_name = 'registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)


class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name = 'edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')


def password_exitoso(request):
    return render(request, 'passwordExitoso.html', {})


# GUITARRA

class GuitarraLista(LoginRequiredMixin, ListView):
    context_object_name = 'guitarras'
    queryset = Instrumento.objects.filter(instrumento__startswith='guitarra')
    template_name = 'listaGuitarras.html'
    login_url = '/login/'


class GuitarraDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'guitarra'
    template_name = 'guitarraDetalle.html'


class GuitarraUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('guitarras')
    context_object_name = 'guitarra'
    template_name = 'guitarraEdicion.html'


class GuitarraDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('guitarras')
    context_object_name = 'guitarra'
    template_name = 'guitarraBorrado.html'

# BAJO


class BajoLista(LoginRequiredMixin, ListView):
    context_object_name = 'bajos'
    queryset = Instrumento.objects.filter(instrumento__startswith='bajo')
    template_name = 'listaBajos.html'


class BajoDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'bajo'
    template_name = 'bajoDetalle.html'


class BajoUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('bajos')
    context_object_name = 'bajo'
    template_name = 'bajoEdicion.html'


class BajoDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('bajos')
    context_object_name = 'bajo'
    template_name = 'bajoBorrado.html'

# PEDAL


class PedalLista(LoginRequiredMixin, ListView):
    context_object_name = 'pedales'
    queryset = Instrumento.objects.filter(instrumento__startswith='pedal')
    template_name = 'listaPedales.html'


class PedalDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'pedal'
    template_name = 'pedalDetalle.html'


class PedalUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('pedales')
    context_object_name = 'pedal'
    template_name = 'pedalEdicion.html'


class PedalDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('pedales')
    context_object_name = 'pedal'
    template_name = 'pedalBorrado.html'

# AMPLIFICADOR


class AmplificadorLista(LoginRequiredMixin, ListView):
    context_object_name = 'amplificadores'
    queryset = Instrumento.objects.filter(
        instrumento__startswith='amplificador')
    template_name = 'listaAmplificadores.html'


class AmplificadorDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'amplificador'
    template_name = 'amplificadorDetalle.html'


class AmplificadorUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('amplificadores')
    context_object_name = 'amplificador'
    template_name = 'amplificadorEdicion.html'


class AmplificadorDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('amplificadores')
    context_object_name = 'amplificador'
    template_name = 'amplificadorBorrado.html'

# TECLADO


class TecladoLista(LoginRequiredMixin, ListView):
    context_object_name = 'teclados'
    queryset = Instrumento.objects.filter(instrumento__startswith='teclado')
    template_name = 'listaTeclados.html'


class TecladoDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'teclado'
    template_name = 'tecladoDetalle.html'


class TecladoUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('teclados')
    context_object_name = 'teclado'
    template_name = 'tecladoEdicion.html'


class TecladoDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('teclados')
    context_object_name = 'teclado'
    template_name = 'tecladoBorrado.html'

# BATERIA


class BateriaLista(LoginRequiredMixin, ListView):
    context_object_name = 'baterias'
    queryset = Instrumento.objects.filter(instrumento__startswith='bateria')
    template_name = 'listaBaterias.html'


class BateriaDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'bateria'
    template_name = 'bateriaDetalle.html'


class BateriaUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('baterias')
    context_object_name = 'bateria'
    template_name = 'bateriaEdicion.html'


class BateriaDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('baterias')
    context_object_name = 'bateria'
    template_name = 'bateriaBorrado.html'


# OTRO

class OtroLista(LoginRequiredMixin, ListView):
    context_object_name = 'otros'
    queryset = Instrumento.objects.filter(instrumento__startswith='otro')
    template_name = 'listaOtros.html'


class OtroDetalle(LoginRequiredMixin, DetailView):
    model = Instrumento
    context_object_name = 'otro'
    template_name = 'otroDetalle.html'


class OtroUpdate(LoginRequiredMixin, UpdateView):
    model = Instrumento
    form_class = ActualizacionInstrumento
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'otroEdicion.html'


class OtroDelete(LoginRequiredMixin, DeleteView):
    model = Instrumento
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'otroBorrado.html'

# CREACION INSTRUMENTO


class InstrumentoCreacion(LoginRequiredMixin, CreateView):
    model = Instrumento
    form_class = FormularioNuevoInstrumento
    success_url = reverse_lazy('home')
    template_name = 'instrumentoCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InstrumentoCreacion, self).form_valid(form)


class InstrumentoBusqueda(ListView):
    model = Instrumento

    def get(self, request, *args, **kwargs):
        tipo = request.GET.get('tipo')
        if tipo:
            tipo = tipo.lower()  # Convertimos en minúsculas
            if tipo in 'guitarras':
                return redirect('guitarras')
            elif tipo in 'bajos':
                return redirect('bajos')
            elif tipo in 'pedales':
                return redirect('pedales')
            elif tipo in 'amplificadores':
                return redirect('amplificadores')
            elif tipo in 'teclados':
                return redirect('teclados')
            elif tipo in 'baterias':
                return redirect('baterias')
            elif tipo in 'otros':
                return redirect('otros')

            # Faltaría agregar los otros if para los otros instrumentos que necesitemos
        else:
            return redirect('home')


class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI


def about(request):
    return render(request, 'acercaDeMi.html', {})