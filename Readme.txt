#Pairwise-Sequence-Alignment

##Problem Statement
Positional and Inverted indexing are different implementations of Boolean Model to resolve boolean queries.These indexing methods produce rankless documents but provides basis to models like Bi-Word indexes , Wild-card queries.

<p>
  <a href="https://www.linkedin.com/in/ahsannaqvii/" rel="nofollow noreferrer">
 	![rr](https://i.stack.imgur.com/gVE0j.png)

    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
  </a> &nbsp; 
  <a href="https://github.com/[removed]" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
  </a>
</p>


























#Steps to Execute the FLASK UI

In the Positional and Inverted Index files : 
1) Enter the Abstract folder path which contain all the files.
2) Enter the path for StopWords.txt file.

--If successful , Positional and Inverted indexes will be  made

To show the Indexes and Document on Flask UI:

1)Create a virtual env
2)Activate the venv by : source .env/bin/activate
3)export FLASK_ENVIRONMENT=development
4)export FLASK_APP=app2.py
5)FLASK_DEBUG=1 flask run


NOTE : YOU CANNOT RUN THE PositionalIndex.py and InvertedIndex.py without setting up the Flask config . 
If you wish to run the PositionalIndex.py without FLASK UI : 
copy the following into the __main__ of PositionalIndex.py file :

 PosIndex=PositionalIndex()
 PosIndex.ReadStopWords()
 for docID in range(1,448): 
            PosIndex.ReadData(docID)
            PosIndex.RemovePuncs()
            PosIndex.StopWordsRemoval()
            PosIndex.PorterStemmer()
            PosIndex.Dictionary(docID)
        

        data=PosIndex.Postings_List_Retrieval(output["name"])
        print(data)
       
        content=PosIndex.Retrieve_File_Content(data)
        print(content)
        
If you wish to run the InvertedIndex.py without FLASK UI : 
copy the following into the __main__ of InvertedIndex.py file :
InvertedIndex1=InvertedIndex.InvertedIndex()
        InvertedIndex1.ReadStopWords()
        
        for docID in range(1,448): 
            InvertedIndex1.ReadData(docID)
            InvertedIndex1.RemovePuncs()
            InvertedIndex1.StopWordsRemoval()
            InvertedIndex1.PorterStemmer()
            II=InvertedIndex1.Dictionary(docID)

        QT,ops=InvertedIndex1.QueryProcessing(output["name"])


        PL=InvertedIndex1.Posting_Lists_Retrieval(QT)

        data=InvertedIndex1.Posting_Lists_Intersect(PL,ops)  #This contains all the common DOCIDS;
        # count=str(len(data))
       
        content=InvertedIndex1.Retrieve_File_Content(data)
![rr](https://user-images.githubusercontent.com/29493186/158867974-29ba3044-16f1-4f71-887d-6a8eacf0ce13.png)


