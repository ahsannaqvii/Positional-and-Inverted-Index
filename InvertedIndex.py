#File handling mechanism
from sre_constants import IN
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class InvertedIndex:
    fileText=" "
    stopWords=[]
    inverted_index={}
   
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

    #-------------------------------------------------------------- #Function responsible to create DOCID PAIRS----------------------#
    def Dictionary(self,docID):                                        
        unique=[]

        for word in self.fileText:
            if word not in unique:
                unique.append(word)
        self.fileText=unique
        self.fileText.sort()

        for term in (self.fileText):
            if term in self.inverted_index:
                self.inverted_index[term].add(docID)

            else:
                self.inverted_index[term]={docID}  
        return self.inverted_index

    #-----------------------------------------------------QUERY PROCESSING----------------------------------------------------x
    def QueryProcessing(self,Query):    

        print("User query is : " , Query)
        excluded=["AND" , "or" , "and", "OR" , "not" , "NOT"]
        operations=[]     
        Tokens = word_tokenize(Query)
        
        for word in Tokens:  #Save the ops(AND / OR) for future use in Posting list retrieval function.
            if word in excluded:
                operations.append(word)
                
        Query=Query.lower()  #Lowercase the query if not                                           

        stemmer = PorterStemmer() #Stem the Query and Tokenize                                   
        stemmedTokens=[]
        for tokens in Tokens:
            stemWord=stemmer.stem(tokens)
            stemmedTokens.append(stemWord)    
        Query=stemmedTokens

        QueryTerms=[]#Select Query terms to retrieve posting List                                                     
        for term in Query:
            if term not in excluded:
                QueryTerms.append(term)
        return QueryTerms,operations

    #------------------------------------------------------Retrieve all Posting alls for Query Terms---------------------------------x
    def Posting_Lists_Retrieval(self,QueryTerms):

        count=len(QueryTerms)
        PostingList=[]
        for i in range(count):
            PostingList.append(self.inverted_index[QueryTerms[i]])
        return PostingList

    #------------------------------------------------------------Intersect or Union or Not common lists.---------------------------------#
    def Posting_Lists_Intersect(self,PostingList,Operations):               
        count=len(PostingList)
        print(count)
        if(count ==1 ):
            return sorted(PostingList[0])  
        else:
            result=set(PostingList[0])
            k=1
            while count > 1 :
                s1=set(PostingList[k])
                if(Operations[k-1]=="AND" or Operations[k-1]=="and"):
                    result=result.intersection(s1)
                    k=k+1
                    count=count-1 
                elif(Operations[k-1]=="OR"):
                    result=result.union(s1)
                    k=k+1
                    count=count-1

            return sorted(result)
       
    #---------------------------------------------------------------------- #Function made for Flask-----------------------------------
    def Retrieve_File_Content(self,data):                                      
        content=[]   
        for i in (data):
            print(i)
            fileExt = open("/home/syedahsan127/Documents/University/SixthSemester/IR/A1/Abstracts/"+ str(i) +".txt", "r", errors="ignore")
            ff=fileExt.read()
            content.append(ff)

        return content




    






