from dal import autocomplete

from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import FormView, DetailView

from rest_framework import generics

from genomic_variants.forms import GeneNameForm
from genomic_variants.models import GenomicVariant, Gene
from genomic_variants.serializers import GenomicVariantsSerializer


GV_FIELDNAMES = ['Gene', 'Nucleotide Change', 'Protein Change', 'Other Mappings',
                 'Alias', 'Transcripts', 'Region', 'Reported Classification',
                 'Inferred Classification', 'Source', 'Last Evaluated',
                 'Last Updated', 'URL', 'Submitter Comment', 'Assembly', 'Chr',
                 'Genomic Start', 'Genomic Stop', 'Ref', 'Alt', 'Accession',
                 'Reported Ref', 'Reported Alt']


class IndexView(FormView):
    template_name = 'home.html'
    form_class = GeneNameForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        qs = self.get_queryset()

        genomic_variants_table_info = []
        for gv in qs:
            gvinfo = {'id': gv.pk,
                      GV_FIELDNAMES[0]: gv.gene,
                      GV_FIELDNAMES[1]: gv.nucleotide_change,
                      GV_FIELDNAMES[2]: gv.protein_change,
                      GV_FIELDNAMES[7]: gv.reported_classification,
                      GV_FIELDNAMES[10]: gv.last_evaluated,
                      GV_FIELDNAMES[11]: gv.last_updated,
                      }
            genomic_variants_table_info.append(gvinfo)

        context['genomic_variants_table_info'] = genomic_variants_table_info
        context['genomic_variants_headers'] = GV_FIELDNAMES
        return context

    def get_queryset(self):
        qs = GenomicVariant.objects.all()
        name = self.request.GET.get('name', None)
        if name:
            return qs.filter(gene__name__iexact=name)
        return qs.none()

    def post(self, request, *args, **kwargs):
        if 'name' in request.POST:
            return redirect(self.get_success_url())
        return super(IndexView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        """Url for successful form submit"""
        url = reverse('index')
        search_name_id = self.request.POST.get('name', None)
        if search_name_id:
            search_string = Gene.objects.get(id=search_name_id)
            return '{}?{}'.format(url, urlencode({'name': search_string})) if search_string else url
        return url


class GenomicVariantsDetailView(DetailView):
    template_name = 'detail.html'
    model = GenomicVariant


################
#  APIs


class GenomicVariantsMixin(object):
    queryset = GenomicVariant.objects.all()
    serializer_class = GenomicVariantsSerializer


class GenomicVariantsAPIListView(GenomicVariantsMixin, generics.ListAPIView):

    def get_queryset(self):
        qs = GenomicVariant.objects.all()
        name = self.request.GET.get('name', None)
        if name:
            qs = qs.filter(gene__name__iexact=name)
        return qs


class GenomicVariantsAPIDetailView(GenomicVariantsMixin, generics.RetrieveAPIView):
    lookup_field = 'pk'


class GeneSuggestAPIView(autocomplete.Select2QuerySetView):
    """ View to facilitate auto-completion of Gene names """

    def get_queryset(self):
        qs = Gene.objects.all().order_by('name')
        if self.q:
            return qs.filter(name__istartswith=self.q)
        return qs.none()
