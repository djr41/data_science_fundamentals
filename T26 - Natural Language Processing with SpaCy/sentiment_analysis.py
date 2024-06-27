#---------- Task 26 - Natural Language Processing with spaCy ---------------------
# In this task, we develop a Python program that performs sentiment analysis
# on a dataset of Amazon product reviews.

# import the required libraries
import pandas as pd
import re
import spacy
from textblob import TextBlob
import pprint

##-- Functions to be called in the main program
# Function to process a doc object in preparation for sentiment analysis.
def process_doc(doc):
    # lemmatize and filter out stop words
    temp_list = [token.lemma_ for token in doc if not token.is_stop]   
    # joins list to make string
    temp_str = ' '.join(temp_list)                                   
    # removes any non alpha numeric characters
    temp_str = re.sub('[^a-zA-Z0-9 \n]', '', temp_str)              
    return temp_str

# Function to return a doc with TextBlob sentiment attributes from the index of the review
def review_sentiment(review_index):
     doc = nlp(review_data_cleaned[review_index])
     doc = TextBlob(process_doc(doc))
     return doc

# Function to compute the similarities between two reviews given their indexes r1 & r2
def review_similarity(r1, r2):
    doc1 = nlp(review_data_cleaned[r1])    # review 1
    doc2 = nlp(review_data_cleaned[r2])    # review 2
    similarity_score = doc1.similarity(doc2)
    return similarity_score


# load the language model
nlp = spacy.load("en_core_web_md")

# load the data set
df = pd.read_csv('amazon_product_reviews.csv',dtype='str')


##-- Pre-processing 
# select the column that contains the reviews and drop any missing values
review_data = df['reviews.text'].dropna()

# use string methods to switch to lower case and strip white space
review_data_cleaned = review_data.str.lower().str.strip()


##-- Main program 
#ask for user input of the review index and outputs sentiment analysis 
review_index=int(input('Please enter the index of the review that you with to analyse: '))

# call review_sentiment function and assign polarity and subjectivity values 
polarity = review_sentiment(review_index).sentiment.polarity
subjectivity = review_sentiment(review_index).sentiment.subjectivity

# print to screen sentiment analysis along with the original review
print(f"The below review has a polarity of {polarity:.2f} and a subjectivity of {subjectivity:.2f}\n")
pprint.pprint(f"{review_data[review_index]}")


##-- additional script to show how to call the similarity score function
r1 = review_index # index of review chosen by user
r2 = 0 # index of the review to compare similarity with

print(f"\nThe similarity between review {r1} and {r2} is {review_similarity(r1,r2):.2f}\n")