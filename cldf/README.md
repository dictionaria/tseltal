<a name="ds-cldfmetadatajson"> </a>

# Dictionary Tseltal-Spanish multidialectal dictionary

**CLDF Metadata**: [cldf-metadata.json](./cldf-metadata.json)

**Sources**: [sources.bib](./sources.bib)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Polian, Gilles. 2020. Tseltal-Spanish multidialectal dictionary. Dictionaria 10. 1-8109 (Available online at https://dictionaria.clld.org/contributions/tseltal)
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Dictionary](http://cldf.clld.org/v1.0/terms.rdf#Dictionary)
[dc:creator](http://purl.org/dc/terms/creator) | Gilles Polian
[dc:identifier](http://purl.org/dc/terms/identifier) | https://dictionaria.clld.org/contributions/tseltal
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/dictionaria/tseltal
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/dictionaria/tseltal/tree/7aac043">dictionaria/tseltal v1.1-3-g7aac043</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v4.4">Glottolog v4.4</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.8.10</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | tseltal
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-entriescsv"></a>Table [entries.csv](./entries.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF EntryTable](http://cldf.clld.org/v1.0/terms.rdf#EntryTable)
[dc:extent](http://purl.org/dc/terms/extent) | 8109


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Headword](http://cldf.clld.org/v1.0/terms.rdf#headword) | `string` | 
[Part_Of_Speech](http://cldf.clld.org/v1.0/terms.rdf#partOfSpeech) | `string` | 
`Abstract_Noun` | `string` | 
`Agentive_Noun` | `string` | 
`Alternative_Form` | `string` | 
`Associated_Phrasemes` | `string` | 
`Attributive` | `string` | 
`Contains` | list of `string` (separated by ` ; `) | References [entries.csv::ID](#table-entriescsv)
`Dialectal_Distribution` | `string` | 
`Diffusive_Form` | `string` | 
`Entry_IDs` | list of `string` (separated by ` ; `) | References [entries.csv::ID](#table-entriescsv)
`Etymology` | `string` | 
`Infinitive` | `string` | 
`MarkedPossession` | `string` | 
`Morphological_Segmentation` | `string` | 
`NonPossessed_Form` | `string` | 
`Phonetic_Form` | `string` | 
`Plural` | `string` | 
`Possessed_Plural` | `string` | 
`Predictable_Dialectal_Variants` | `string` | 
`Related_Dialectal_Form` | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
`Variant_Form` | `string` | 

## <a name="table-sensescsv"></a>Table [senses.csv](./senses.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF SenseTable](http://cldf.clld.org/v1.0/terms.rdf#SenseTable)
[dc:extent](http://purl.org/dc/terms/extent) | 9616


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Entry_ID](http://cldf.clld.org/v1.0/terms.rdf#entryReference) | `string` | References [entries.csv::ID](#table-entriescsv)
`Comparison_Meaning` | `string` | 
[Concepticon_ID](http://cldf.clld.org/v1.0/terms.rdf#concepticonReference) | `string` | 
`Media_IDs` | list of `string` (separated by ` ; `) | References [media.csv::ID](#table-mediacsv)
`Related_Entries` | `string` | 
`Related_Forms_Other_Dialect` | `string` | 
`Scientific_Name` | `string` | 
`Sense_Dialect` | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
`Subspecies` | `string` | 
`Synonym` | list of `string` (separated by ` ; `) | References [entries.csv::ID](#table-entriescsv)
`Synonyms_Other_Dialect` | `string` | 

## <a name="table-examplescsv"></a>Table [examples.csv](./examples.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ExampleTable](http://cldf.clld.org/v1.0/terms.rdf#ExampleTable)
[dc:extent](http://purl.org/dc/terms/extent) | 12446


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Primary_Text](http://cldf.clld.org/v1.0/terms.rdf#primaryText) | `string` | The example text in the source language.
[Analyzed_Word](http://cldf.clld.org/v1.0/terms.rdf#analyzedWord) | list of `string` (separated by `\t`) | The sequence of words of the primary text to be aligned with glosses
[Gloss](http://cldf.clld.org/v1.0/terms.rdf#gloss) | list of `string` (separated by `\t`) | The sequence of glosses aligned with the words of the primary text
[Translated_Text](http://cldf.clld.org/v1.0/terms.rdf#translatedText) | `string` | The translation of the example text in a meta language
[Meta_Language_ID](http://cldf.clld.org/v1.0/terms.rdf#metaLanguageReference) | `string` | References the language of the translated text<br>References [languages.csv::ID](#table-languagescsv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
`Dialect` | `string` | 
`Sense_IDs` | list of `string` (separated by ` ; `) | References [senses.csv::ID](#table-sensescsv)

## <a name="table-mediacsv"></a>Table [media.csv](./media.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF MediaTable](http://cldf.clld.org/v1.0/terms.rdf#MediaTable)
[dc:extent](http://purl.org/dc/terms/extent) | 318


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Media_Type](http://cldf.clld.org/v1.0/terms.rdf#mediaType) | `string` | 
[Download_URL](http://cldf.clld.org/v1.0/terms.rdf#downloadUrl) | `anyURI` | 
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
`size` | `integer` | 

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 1


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 

