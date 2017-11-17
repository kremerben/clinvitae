from django.test import TestCase
from rest_framework.test import APIRequestFactory

from genomic_variants.models import Gene, GenomicVariant
from genomic_variants.serializers import GeneNameSerializer, GenomicVariantsSerializer

factory = APIRequestFactory()


class GeneNameSerializerTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.gene = Gene.objects.create(name='gene 1')

    def test_gene_suggest_serializer(self):
        serializer = GeneNameSerializer(self.gene)
        self.assertEqual(serializer.data['id'], self.gene.id)
        self.assertEqual(serializer.data['name'], self.gene.name)


class GenomicVariantsSerializerTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.gene = Gene.objects.create(name='gene 1')
        cls.gv = GenomicVariant.objects.create(gene=cls.gene)

    def test_gene_suggest_serializer(self):
        serializer = GenomicVariantsSerializer(self.gv)
        self.assertEqual(serializer.data['id'], self.gv.id)
        self.assertEqual(serializer.data['nucleotide_change'], self.gv.nucleotide_change)
        self.assertEqual(serializer.data['gene'], self.gene.id)
