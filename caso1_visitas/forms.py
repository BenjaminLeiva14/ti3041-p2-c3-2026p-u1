from django import forms
from .models import Visita

class VisitaForm(forms.ModelForm):
    rut = forms.IntegerField(
        label='RUT',
        min_value=70000000,
        max_value=259999999,
        required=True,
    )
    class Meta:
        model = Visita
        fields = ['nombre', 'rut', 'motivo_visita', 'hora_entrada']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-orange-200 bg-white/80 px-3 py-2.5 text-stone-950 shadow-sm outline-none transition duration-200 placeholder:text-stone-400 hover:border-orange-300 focus:border-orange-600 focus:bg-white focus:ring-4 focus:ring-orange-100',
                'placeholder': 'Ingrese su nombre',
                'autocomplete': 'off',
            }),
            'rut': forms.NumberInput(attrs={
                'class': 'w-full rounded-xl border border-orange-200 bg-white/80 px-3 py-2.5 text-stone-950 shadow-sm outline-none transition duration-200 placeholder:text-stone-400 hover:border-orange-300 focus:border-orange-600 focus:bg-white focus:ring-4 focus:ring-orange-100',
                'placeholder': 'Ingrese su RUT',
                'min': '70000000',
                'max': '259999999',
                'step': '1',
                'inputmode': 'numeric',
            }),
            'motivo_visita': forms.Textarea(attrs={
                'class': 'min-h-28 w-full resize-y rounded-xl border border-orange-200 bg-white/80 px-3 py-2.5 text-stone-950 shadow-sm outline-none transition duration-200 placeholder:text-stone-400 hover:border-orange-300 focus:border-orange-600 focus:bg-white focus:ring-4 focus:ring-orange-100',
                'placeholder': 'Describe el motivo de la visita',
                'rows': 4,
            }),
            'hora_entrada': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'w-full rounded-xl border border-orange-200 bg-white/80 px-3 py-2.5 text-stone-950 shadow-sm outline-none transition duration-200 hover:border-orange-300 focus:border-orange-600 focus:bg-white focus:ring-4 focus:ring-orange-100',
            }),
        }