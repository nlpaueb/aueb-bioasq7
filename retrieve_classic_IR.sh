#!/usr/bin/env bash

python3.6 \
/home/kstam/aueb/Index/home/DATA/Biomedical/document_ranking/bioasq_data/document_retrieval/queries2galago.py \
/home/kstam/aueb/Data/sample.json \
/home/kstam/aueb/Data/sample_galago_queries.json \
/home/kstam/aueb/Data/stopwords.pkl

cd /home/kstam/aueb/Index/home/DATA/Biomedical/document_ranking/bioasq_data/document_retrieval/galago-3.10-bin/bin

/home/kstam/aueb/Index/home/DATA/Biomedical/document_ranking/bioasq_data/document_retrieval/galago-3.10-bin/bin/galago \
batch-search \
--index=pubmed_only_abstract_galago_index \
--verbose=False \
--requested=2000 \
--scorer=bm25 \
--defaultTextPart=postings.krovetz \
--mode=threaded \
/home/kstam/aueb/Data/sample_galago_queries.json \
> /home/kstam/aueb/Data/sample_bm25_retrieval.txt

# This will create the .pkl files
python3.6 \
/home/kstam/aueb/generate_bioasq_data.py \
/home/kstam/aueb/Data/sample.json \
/home/kstam/aueb/Data/sample_bm25_retrieval.txt \
sample \
2017

#/home/kstam/aueb/Data/sample_galago_queries.json \


# This will create the .pkl files
python3.6 \
/home/kstam/aueb/Models/extract_submition_w2v_jpdrmm.py \
/home/kstam/aueb/Data/sample.json \
./bioasq_bm25_top100.sample.pkl \
./bioasq_bm25_docset_top100.sample.pkl \
/home/kstam/aueb/Outputs/sample_output/


