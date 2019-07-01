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
    ```sh retrieve_classic_IR.sh``` 

Step 6: 


Step 7: 






