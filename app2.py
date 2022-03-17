from operator import truediv
from flask import Flask, render_template, url_for, request
import  InvertedIndex 
from re import search
from PositionalIndex import PositionalIndex
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
   
    return render_template("index.html")

@app.route('/result',methods=['POST', 'GET'])
def result():
    data=[]
    content=[]
    heading="BING! RESULTS"
    output = request.form.to_dict()
    print(output)

    if "/" in output["name"]:
        dec=True
    else:
        dec=False
    if(dec==False):
            
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

    elif(dec==True):
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

       

    return render_template('index.html',data=data , heading=heading ,content=content )
    




if __name__ == "__main__":
    app.run(debug=True)