from django.conf.urls import url

from genomic_variants.views import (IndexView,
                                    GenomicVariantsDetailView,
                                    GenomicVariantsAPIListView,
                                    GenomicVariantsAPIDetailView,
                                    GeneSuggestAPIView,
                                    )


api_prefix = r'^api/v1/'

urlpatterns = [

    url(r'^$',
        view=IndexView.as_view(),
        name='index'),

    url(r'^variants/(?P<pk>[0-9]+)/$',
        view=GenomicVariantsDetailView.as_view(),
        name='genomic-variants-detail'),

    url(api_prefix + 'variants/$',
        view=GenomicVariantsAPIListView.as_view(),
        name='api.v1.genomic-variants-list'),

    url(api_prefix + 'variants/(?P<pk>[0-9]+)/$',
        view=GenomicVariantsAPIDetailView.as_view(),
        name='api.v1.genomic-variants-detail'),

    url(api_prefix + 'gene/suggest/$',
        view=GeneSuggestAPIView.as_view(),
        name='api.v1.gene-name-suggest'),
]
