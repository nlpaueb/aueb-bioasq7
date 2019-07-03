# aueb-bioasq7
AUEB at BioASQ 7: Document and Snippet Retrieval


**Downloading data:**

First of all you should download the indexed articles found in this link: <br>   
https://archive.org/details/AUEBBioASQ7Index <br>
and extract in the the "Index" directory <br>

Then you must download the data found in this link: <br>
https://archive.org/details/AUEB_BioASQ_7_data <br>
and extract in the "Data" directory <br>


**Steps:**

Step 1: Extract Data.zip in "Data" directory. <br>

Step 2: Extract galago.tar.gz and mongo.tar.gz in "Index" directory. <br>

Step 3: Install requirements.txt using Python's pip. (We used Python's version 3.6) <br>
        ```pip3.6 install requirements.txt``` 

Step 4: Start mongoDB (preferably in a screen session and then detach)
```./Index/mongo/mongodb/bin/mongod --dbpath ./Index/mongo/mongo_database```

Step 5: retrieve relevant documents using Galago and mongoDB.<br>
You can/should change the paths in the script according to your needs.<br>  
If you have to test you own data you should format your questions like in the **./DATA/bioasq_data/trainining7b.json** file.<br>
    ```sh retrieve_classic_IR.sh```<br>

 Your input file should have the following format: 
 ```
 {
    "questions": [
      {
        "body": "Is Hirschsprung disease a mendelian or a multifactorial disorder?", 
        "id": "55031181e9bde69634000014"
      },
      {
        "body": "What is being measured with an accelerometer in back pain patients", 
        "id": "533f9df0c45e133714000016"
      },
      ...
    ]
 }
```

Step 6: Load model and extract emitions <br>
The pretrianed weights for the models can be found in folder "PretrainedWeightsAndVectors".<br>
In the subfolder "bioasq7_bert_jpdrmm_2L_0p01_run_0" one can found the pretrained weights of JPDRMM model using Bert embeddings.<br>
In the subfolder "bioasq_jpdrmm_2L_0p01_run_0" one can found the pretrained weights of JPDRMM model using W2V embeddings.<br> 
You can run the models using the following commands:<br>

```
python extract_submition_w2v_jpdrmm.py
```
or 
```
python extract_submition_bert_jpdrmm.py
```
for W2V-JPDRMM and BERT-JPDRMM respectively. 

You should change the following paths according to your data files' paths.<br>
For W2V-JPDRMM: 
```
###########################################################
eval_path                   = './Evaluation/eval/run_eval.py'
retrieval_jar_path          = './Evaluation/dist/my_bioasq_eval_2.jar'
###########################################################
w2v_bin_path                = './Data/PretrainedWeightsAndVectors/pubmed2018_w2v_30D.bin'
idf_pickle_path             = './Data/PretrainedWeightsAndVectors/idf.pkl'
###########################################################
resume_from                 = './Data/bioasq_jpdrmm_2L_0p01_run_0/best_dev_checkpoint.pth.tar'
###########################################################
b                           = 5 # sys.argv[1]
f_in1                       = './Data/test_batch_{}/BioASQ-task7bPhaseA-testset{}'.format(b, b)
f_in2                       = './Data/test_batch_{}/bioasq7_bm25_top100/bioasq7_bm25_top100.test.pkl'.format(b)
f_in3                       = './Data/test_batch_{}/bioasq7_bm25_top100/bioasq7_bm25_docset_top100.test.pkl'.format(b)
odir                        = './Outputs/test_jpdrmm_high_batch{}/'.format(b)
###########################################################
```

For BERT-JPDRMM: 
```
###########################################################
f_in1               = './Data/test_batch_5/BioASQ-task7bPhaseA-testset5'
f_in2               = './Data/test_batch_5/bioasq7_bm25_top100/bioasq7_bm25_top100.test.pkl'
f_in3               = './Data/test_batch_5/bioasq7_bm25_top100/bioasq7_bm25_docset_top100.test.pkl'
odir                = './Outputs/test_bert_jpdrmm_high_batch5/'
###########################################################
eval_path           = './Evaluation/eval/run_eval.py'
retrieval_jar_path  = './Evaluation/dist/my_bioasq_eval_2.jar'
###########################################################
w2v_bin_path        = './Data/PretrainedWeightsAndVectors/pubmed2018_w2v_30D.bin'
idf_pickle_path     = './Data/PretrainedWeightsAndVectors/idf.pkl'
###########################################################
resume_from         = './Data/PretrainedWeightsAndVectors/bioasq7_bert_jpdrmm_2L_0p01_run_0/best_checkpoint.pth.tar'
resume_from_bert    = './Data/PretrainedWeightsAndVectorsbioasq7_bert_jpdrmm_2L_0p01_run_0/best_bert_checkpoint.pth.tar'
cache_dir           = './Data/PretrainedWeightsAndVectors/bert_cache/'
###########################################################
```

Step 7: 






