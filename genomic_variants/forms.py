from dal import autocomplete

from django import forms

from genomic_variants.models import Gene


class GeneNameForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=Gene.objects.all(),
        widget=autocomplete.ModelSelect2(url='api.v1.gene-name-suggest',
                                         attrs={
                                             'data-placeholder': 'Autocomplete...',
                                             'data-minimum-input-length': 2,
                                         })
    )

    class Meta:
        model = Gene
        fields = ('name',)

