# Ben Kremer - Technical Application
## Clinvitae

Running live at: https://ben-kremer-clinvitae.herokuapp.com/

Clinvitae is a genomic variant web application that allows a user to search for
genomic variants based on a gene name and display the results in a table.

## To run this project locally
1. Clone repo
2. which python3
3. mkvirtualenv ben_kremer_clinvitae --python=<result from step 2>
4. cd ben_kremer_clinvitae
5. pip install -r requirements.txt
6. python3 manage.py migrate
7. python3 manage.py runserver






## Features
-------------
There are two components to the Clinvitae application, web UI access and API access (described below).



## Clinvitae API V1 WIKI
-------------
The Clinvitae REST API provides simple access to read data in JSON format via HTTP GET/POST requests over http(s).


#### Endpoints

| URL                      | Description        | HTTP |
|--------------------------|--------------------| ----- |
| `api/v1/variants/`       | Genomic Variant List | GET |
| `api/v1/variants/:variant_id`  | Genomic Variant Details by Variant Id | GET |
| `api/v1/gene/suggest/`  | Suggested Autocomplete search based on name argument | GET/POST |


## Genomic Variant List [GET]

#### Example: Genomic Variant List [GET]
```
https://ben-kremer-clinvitae.herokuapp.com/api/v1/variants/
```

#### Response
Paginated list of Genomic Variants, as described below


## Genomic Variant Detail [GET]

#### Response
Single Genomic Variant object with the following properties:

| Name            | Type    | Description |
|-----------------|---------|-------------|
| gene | integer |  ID of related Gene. |
| id | integer |  ID of Genomic Variant. |
| nucleotide_change | string | nucleotide change. |
| protein_change | string | protein change. |
| other_mappings | string | additional mappings. |
| alias | string | alias. |
| transcripts | string | transcripts. |
| region | string | region. |
| reported_classification | string | reported classification. |
| inferred_classification | string | inferred classification. |
| source | string | source. |
| last_evaluated | datetime | last evaluated datetime. |
| last_updated | datetime | last updated datetime. |
| url | string | html url. |
| submitter_comment | string | submitter comment. |
| assembly | string | assembly. |
| chr | string | chr. |
| genomic_start | string | genomic start. |
| genomic_stop | string | genomic stop. |
| ref | string | ref. |
| alt | string | alt. |
| accession | string | accession. |
| reported_ref | string | reported ref. |
| reported_alt | string | reported alt. |


#### Example: Genomic Variant Detail [GET]
```
https://ben-kremer-clinvitae.herokuapp.com/api/v1/variants/2/
```

```JSON Response
{
    id: 2,
    gene: 2
    nucleotide_change: "NM_000018.3:c.1182+1G>A",
    protein_change: "",
    other_mappings: "NM_000018.3:c.1182+1G>A,NG_007975.1:g.8405G>A,NC_000017.11:g.7223238G>A,NC_000017.10:g.7126557G>A,NM_000018.2:c.1182+1G>A",
    alias: "",
    transcripts: "NM_000018.3,NG_007975.1,NC_000017.11,NC_000017.10,NM_000018.2",
    region: "NM_000018.3:IVS11",
    reported_classification: "Pathogenic",
    inferred_classification: "Pathogenic",
    source: "ClinVar",
    last_evaluated: "2014-05-15T00:00:00Z",
    last_updated: "2017-09-14T00:00:00Z",
    url: "https://www.ncbi.nlm.nih.gov/clinvar/RCV000077901",
    submitter_comment: "",
    assembly: "GRCh37",
    chr: "17",
    genomic_start: "7126556",
    genomic_stop: "7126557",
    ref: "G",
    alt: "A",
    accession: "NC_000017.10",
    reported_ref: "G",
    reported_alt: "A",
}
```


## Gene Name suggests [GET]

### Request Query Parameters

| Name | Format | Description |
|------|--------|-------------|
| name | string | Retrieve Gene's beginning with this string |


#### Example: Suggested Gene names [GET]
```
https://ben-kremer-clinvitae.herokuapp.com/api/v1/gene/suggest/?name=a
```

```JSON Response
{
    results: [{
            id: "3142",
            text: "A1BG-AS1"
        },
        {
            id: "2927",
            text: "A1CF"
        },
        {
            id: "44",
            text: "AADAC"
        },
        {
            id: "2914",
            text: "AADACL2-AS1"
        },
    ],
    pagination: {
        more: true
    }
}
```


