from django.db import models


class Gene(models.Model):

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class GenomicVariant(models.Model):

    gene = models.ForeignKey(Gene, blank=True)
    nucleotide_change = models.TextField(blank=True)
    protein_change = models.TextField(blank=True)
    other_mappings = models.TextField(blank=True)
    
    alias = models.TextField(blank=True)
    transcripts = models.TextField(blank=True)
    region = models.TextField(blank=True)

    reported_classification = models.TextField(blank=True)
    inferred_classification = models.TextField(blank=True)
    source = models.TextField(blank=True)
    last_evaluated = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)

    url = models.URLField(max_length=255, blank=True)
    submitter_comment = models.TextField(blank=True)
    assembly = models.TextField(blank=True)
    chr = models.TextField(blank=True)
    genomic_start = models.TextField(blank=True)
    genomic_stop = models.TextField(blank=True)
    ref = models.TextField(blank=True)
    alt = models.TextField(blank=True)
    accession = models.TextField(blank=True)
    reported_ref = models.TextField(blank=True)
    reported_alt = models.TextField(blank=True)

    def __str__(self):
        return '{} - {}'.format(self.gene, self.nucleotide_change)
