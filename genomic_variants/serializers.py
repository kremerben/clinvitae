from rest_framework.serializers import ModelSerializer

from genomic_variants.models import GenomicVariant, Gene


class GenomicVariantsSerializer(ModelSerializer):

    class Meta:
        model = GenomicVariant
        fields = '__all__'


class GeneNameSerializer(ModelSerializer):

    class Meta:
        model = Gene
        fields = ('id', 'name',)
