#!/usr/bin/env bash



python3.6 queries2galago.py \
./DATA/bioasq_data/trainining7b.json \
./bioasq7b_all_galago_queries.json

./Index/galago-3.10-bin/bin/galago \
batch-search \
--index=pubmed_only_abstract_galago_index \
--verbose=False \
--requested=2000 \
--scorer=bm25 \
--defaultTextPart=postings.krovetz \
--mode=threaded \
./bioasq7b_all_galago_queries.json \
> ./bioasq7b_bm25_retrieval.all.txt

python3.6 /home/dpappas/generate_bioasq_data.py trainining7b.json bioasq7b_bm25_retrieval.all.txt all 2016




