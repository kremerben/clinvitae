import json

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from genomic_variants.models import GenomicVariant, Gene
from genomic_variants.views import (GenomicVariantsAPIListView,
                                    GenomicVariantsAPIDetailView, GeneSuggestAPIView)


factory = APIRequestFactory()
gv_api_list = GenomicVariantsAPIListView.as_view()
gv_api_detail = GenomicVariantsAPIDetailView.as_view()
gene_api_suggest = GeneSuggestAPIView.as_view()


class GenomicVariantsAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.gene = Gene.objects.create(name='gene 1')
        cls.gv = GenomicVariant.objects.create(gene=cls.gene)

    def test_access_to_genomic_variants_list(self):
        request = factory.get('/api/v1/variants/')
        response = gv_api_list(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_to_genomic_variants_detail(self):
        request = factory.get('/api/v1/variants/')
        response = gv_api_detail(request, pk=self.gv.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_to_gene_suggest_no_params(self):
        request = factory.get('/api/v1/gene/suggest/')
        response = gene_api_suggest(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_to_gene_suggest(self):
        request = factory.get('/api/v1/gene/suggest/', {'q': 'g'})
        response = gene_api_suggest(request)

        expected_response = {'results': [{'id': '1',
                                          'text': 'gene 1'}],
                             'pagination': {'more': False}
                             }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_response, json.loads(response.content))

    def test_access_to_gene_suggest_no_result(self):
        request = factory.get('/api/v1/gene/suggest/', {'q': 'asdf'})
        response = gene_api_suggest(request)

        expected_response = {'results': [],
                             'pagination': {'more': False}
                             }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_response, json.loads(response.content))

    def test_access_to_gene_suggest_missing_params(self):
        request = factory.get('/api/v1/gene/suggest/')
        response = gene_api_suggest(request)

        expected_response = {'results': [],
                             'pagination': {'more': False}
                             }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_response, json.loads(response.content))
