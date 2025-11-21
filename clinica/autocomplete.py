from dal import autocomplete
from .models import Paciente

class PacienteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Paciente.objects.all()

        if self.q:
            qs = qs.filter(nome__icontains=self.q)

        return qs
