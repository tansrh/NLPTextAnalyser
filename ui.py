import streamlit as st
from pdfminer.high_level import extract_pages, extract_text
from textblob import TextBlob
import nltk
import pandas as pd
import spacy
from spacy import displacy
from annotated_text import annotated_text
from nltk.corpus import stopwords
nltk.download('stopwords')
stpwds=stopwords.words('english')
from nltk.tokenize import word_tokenize
st.title("Text Analyser")
nlp=spacy.load("en_core_web_sm")

option = st.selectbox(
    'How would you like to be analyze the text ?',
    ('File Upload', 'Edit in screen'))
if option=='File Upload':
    file = st.file_uploader("Upload a PDF file", type="pdf")
    btn=st.button("Analyse")
    content=""
    
    if file is not None:
        
    # Read the PDF file
    #    pdf_reader = PyPDF2.PdfReader(file)
    # Extract the content
        content = ""
        txt=extract_text(file)
        content=txt
        ctxt=TextBlob(content).correct()
        ct=""
        for i in ctxt:
            ct+=i
        nlpp=txt
        ct=word_tokenize(ct)
        content=word_tokenize(content)
        tot=len(ct)
        wng=[]
        crt=[]
        
        wt=0
        for i in range(tot):
            
            if(ct[i] in stpwds):
                continue
            
            
            if(content[i]!=ct[i]):
                wt+=1
                wng.append(content[i])
                crt.append(ct[i])
            
            

    if btn:
        st.write("Total words :", tot)
        st.write("Accuracy :")
        st.write(((wt/tot))*100)
        st.write(f"Vocabulary strength : {len(crt)}")
        st.write(f"Stopwords used : {tot-len(crt)}")
        lst=[]
        for i in ct:
            if(i in crt):
                lst.append((f" {i} ", '-'))
            else:
                lst.append(f" {i} ")
        st.write("Corrected text :")
        annotated_text(lst)
        
        df = pd.DataFrame({'Wrongly spelled inputs' : wng, 'Probable correct form' : crt})    
        st.table(df)
        doc=nlp(nlpp)
        if(len(doc.ents)>0):
            ll=[]
            for x in doc.ents:
                ll.append(x.text)
                
            dd=pd.DataFrame({"Named Entites Recognized" : ll})
            st.table(dd)
    
        
        
        
else:
    txt = st.text_area(
    "Write the Text to be analyzed")
    btn=st.button("Analyse")
    content = ""
    
    content=txt
    ctxt=TextBlob(content).correct()
    ct=""
    for i in ctxt:
        ct+=i
    nlpp=txt
    ct=word_tokenize(ct)
    content=word_tokenize(content)
   
    tot=len(ct)
    
    wng=[]
    crt=[]
    wt=0
    for i in range(tot):
        
        if(ct[i] in stpwds):
                continue
            
        if(content[i]!=ct[i]):
            wt+=1
            wng.append(content[i])
            crt.append(ct[i])
        
        
        
        
        
    if(btn):
        st.write("Total words :", tot)
        st.write("Accuracy :")
        st.write(((wt/tot))*100)
        st.write(f"Vocabulary strength : {len(crt)}")
        st.write(f"Stopwords used : {tot-len(crt)}")
        lst=[]
        for i in ct:
            if(i in crt):
                lst.append((f" {i} ", '-'))
            else:
                lst.append(f" {i} ")
        st.write("Corrected text :")
        annotated_text(lst)
        doc=nlp(nlpp)
        
            
        df = pd.DataFrame({'Wrongly spelled inputs' : wng, 'Probable correct form' : crt})    
        st.table(df)
        
        if(len(doc.ents)>0):
            
            ll=[]
            for x in doc.ents:
                ll.append(x.text)
                
            dd=pd.DataFrame({"Named Entites Recognized" : ll})
            st.table(dd)
        
        
        
    
    


