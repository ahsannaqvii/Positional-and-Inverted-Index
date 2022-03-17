#FILE IMPORTS                                                           ----19K1475
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from collections import defaultdict

class PositionalIndex:
    #Class Variables
    fileText=" "
    stopWords=[]
    positional_Index={}

    #-------------------------------------------------Function designed to read stopwords.txt file -------------------------------#
    def ReadStopWords(self):                            

        f=open("/home/syedahsan127/Documents/University/SixthSemester/IR/A1/stopword.txt","r" )
        stopWords=f.read()
        stopWords=stopWords.split("\n")

    #-------------------------------------------------Function designed to Read all 448files file by file and process it accordingly---------------------#
    def ReadData(self,docID):                           
        
        fileData = open("/home/syedahsan127/Documents/University/SixthSemester/IR/A1/Abstracts/"+ str(docID) +".txt", "r" , errors="ignore")
        self.fileText=fileData.read()
                                                            
    #--------------------------------------------Remove all the punctuations from text file 1.txt ---------------------------#                                                                                                      
    def RemovePuncs(self):

        self.fileText=self.fileText.lower()
        punctuations_marks = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in self.fileText:
            if char not  in punctuations_marks:
                continue
            else:
                self.fileText=self.fileText.replace(char," ")      

    #-----------------------------------------------------Removing all the stop words from the fileText---------------------------#
    def StopWordsRemoval(self):

        stopWordsList=stopwords.words('english')
        custom_sw_list =stopWordsList
        Tokens = word_tokenize(self.fileText)
        self.fileText=[word for word in Tokens if not word in custom_sw_list]
        


    #--------------------------------------------------Stemming of words in files--------------------------------------------------#    
    def PorterStemmer(self):

        stemmer = PorterStemmer()
        stemmedTokens=[]
        for tokens in self.fileText:
            stemWord=stemmer.stem(tokens)
            stemmedTokens.append(stemWord)
            
        self.fileText=stemmedTokens

    #-------------------------------------------Function designed to form a dictionary in the form : { Term : DocID : { Positions } }---------#
    def Dictionary(self,docID):
        temp_dict={}
        Position=0
        for word in self.fileText:
            key=word
            temp_dict.setdefault(key,[])
            temp_dict[key].append(Position)
            Position+=1
        for x in temp_dict:
            
            if self.positional_Index.get(x):
                self.positional_Index[x][docID]=temp_dict.get(x)
            else:
                key=x
                self.positional_Index.setdefault(key,[])
                self.positional_Index[key]={}
                self.positional_Index[x][docID]=temp_dict.get(x)

    #-----------------------------------Performed Intersection of Lists to retrieve the common positions and then show results.-------------------#
    def Postings_List_Retrieval(self,Query):
        print(Query)

        Query=Query.lower()
        result=[]
        #Tokenizing Query
        Tokens = word_tokenize(Query)
        print(Tokens)
        #Stemming Query

        stemmer = PorterStemmer()
        stemmedTokens=[]
        for tokens in Tokens:

            stemWord=stemmer.stem(tokens)
            stemmedTokens.append(stemWord)

        #Extracting the skip position    
        Query=stemmedTokens
        Query[2]=re.sub("/","",Query[2])
        skipMarker=int(Query[2])
   
        word1=self.positional_Index.get(Query[0])
        word2=self.positional_Index.get(Query[1])

        #Finding common DOCIDs and their respective positions list.
        intersect=set(word1).intersection(set(word2))
      
   
        for i in intersect: 

            positionListW1=self.positional_Index[Query[0]][i] #this returns position list of Query1 word
            positionListW2=self.positional_Index[Query[1]][i]   #this returns position list Query2 word
    
            PositionListLength1=len(positionListW1)
            PositionListLength2=len(positionListW2)
            count1=0

            while count1!=PositionListLength1:
                count2=0
                while count2!=PositionListLength2:
                    if (abs(positionListW1[count1] - positionListW2[count2])==skipMarker):
                       
                        result.append(i)
                    count2=count2+1
                count1=count1+1

        unique=[]
        for word in result:
            if word not in unique:
                unique.append(word)
        data=unique
        return data
    #-----------------------------------------------Function made for Flask--------------------------------------------#
    def Retrieve_File_Content(self,data):                       
        content=[]
        
        for i in (data):
            print(i)
            fileExt = open("/home/syedahsan127/Documents/University/SixthSemester/IR/A1/Abstracts/"+ str(i) +".txt", "r", errors="ignore")
            ff=fileExt.read()
            content.append(ff)

        return content
        





