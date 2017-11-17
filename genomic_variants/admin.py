from django.contrib import admin

from genomic_variants.models import GenomicVariant, Gene


class GeneAdmin(admin.ModelAdmin):
    pass


admin.site.register(Gene, GeneAdmin)


class GenomicVariantAdmin(admin.ModelAdmin):
    list_display = ('gene', 'nucleotide_change', 'protein_change', 'alias',
                    'transcripts', 'region', 'reported_classification',
                    'inferred_classification', 'url', 'last_evaluated',
                    'last_updated',)
    list_filter = ('gene', 'nucleotide_change', 'protein_change',
                   'reported_classification', 'last_evaluated', 'last_updated',)


admin.site.register(GenomicVariant, GenomicVariantAdmin)
