import csv
from datetime import datetime
import pytz

from django.core.management.base import BaseCommand

from genomic_variants.models import Gene, GenomicVariant


STD_TSV_COLS = ['Gene', 'Nucleotide Change', 'Protein Change',
                'Other Mappings', 'Alias', 'Transcripts', 'Region',
                'Reported Classification', 'Inferred Classification',
                'Source', 'Last Evaluated', 'Last Updated', 'URL',
                'Submitter Comment', 'Assembly', 'Chr', 'Genomic Start',
                'Genomic Stop', 'Ref', 'Alt', 'Accession', 'Reported Ref', 'Reported Alt']


class Command(BaseCommand):
    # run from the command line as
    # $ python3 manage.py loadtsvdata <file> <optional additional files>
    help = 'Imports a tsv file and writes GenomicVariant and Gene objects to the database'

    def add_arguments(self, parser):
        parser.add_argument('files', nargs='+')

    def import_data(self, filename):
        gene_count = 0
        genomic_variant_count = 0
        with open(filename) as f:
            reader = csv.reader(f, delimiter='\t')

            for row in reader:
                if row[0] != 'Gene':
                    gene_name = row[0]
                    gene, created = Gene.objects.get_or_create(name=gene_name)
                    if created:
                        gene_count += 1

                    if len(row) < len(STD_TSV_COLS):
                        for i in range(len(STD_TSV_COLS)-len(row)):
                            row.append('')

                    if row[10]:
                        last_evaluated = datetime.strptime(row[10], '%Y-%m-%d')
                        last_evaluated = last_evaluated.replace(tzinfo=pytz.UTC)
                    else:
                        last_evaluated = None

                    if row[11]:
                        last_updated = datetime.strptime(row[11], '%Y-%m-%d')
                        last_updated = last_updated.replace(tzinfo=pytz.UTC)
                    else:
                        last_updated = None

                    gv, created = GenomicVariant.objects.get_or_create(
                        gene=gene,
                        nucleotide_change=row[1],
                        protein_change=row[2],
                        other_mappings=row[3],
                        alias=row[4],
                        transcripts=row[5],
                        region=row[6],
                        reported_classification=row[7],
                        inferred_classification=row[8],
                        source=row[9],
                        last_evaluated=last_evaluated,
                        last_updated=last_updated,
                        url=row[12],
                        submitter_comment=row[13],
                        assembly=row[14],
                        chr=row[15],
                        genomic_start=row[16],
                        genomic_stop=row[17],
                        ref=row[18],
                        alt=row[19],
                        accession=row[20],
                        reported_ref=row[21],
                        reported_alt=row[22],
                    )
                    if created:
                        genomic_variant_count += 1
        self.stdout.write('{} Genes imported'.format(gene_count))
        self.stdout.write('{} Genomic Variants imported'.format(genomic_variant_count))

    def handle(self, *args, **options):
        files = options.get('files', [])
        for file in files:
            self.import_data(file)
