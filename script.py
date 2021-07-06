# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:49:15 2021

@author: My Lenovo
"""

from goldman_emma_raw import goldman_docs
from henson_matthew_raw import henson_docs
from wu_tingfang_raw import wu_docs
# import sklearn modules here:
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Setting up the combined list of friends' writing samples
friends_docs = goldman_docs + henson_docs + wu_docs
# Setting up labels for your three friends
friends_labels = [1] * 154 + [2] * 141 + [3] * 166


# Print out a document from each friend:




mystery_postcard = """
My friend,
From the 10th of July to the 13th, a fierce storm raged, clouds of
freeing spray broke over the ship, incasing her in a coat of icy mail,
and the tempest forced all of the ice out of the lower end of the
channel and beyond as far as the eye could see, but the _Roosevelt_
still remained surrounded by ice.
Hope to see you soon.
"""

# Create bow_vectorizer:
from goldman_emma_raw import goldman_docs
from henson_matthew_raw import henson_docs
from wu_tingfang_raw import wu_docs
# import sklearn modules here:
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Setting up the combined list of friends' writing samples
friends_docs = goldman_docs + henson_docs + wu_docs
# Setting up labels for your three friends
friends_labels = [1] * 154 + [2] * 141 + [3] * 166

# Print out a document from each friend:




mystery_postcard = """
Project Gutenberg eBooks require no special apps to read, just the regular Web browsers or eBook readers that are included with computers and mobile devices. There have been reports of sites that charge fees for custom apps, or for the same eBooks that are freely available from Project Gutenberg. Some of the apps might have worthwhile features, but none are required to enjoy Project Gutenberg eBooks.
"""

# Create bow_vectorizer:
bow_vectorizer = CountVectorizer()
# Define friends_vectors:
friends_vectors = bow_vectorizer.fit_transform(friends_docs)
# Define mystery_vector: 
mystery_vector = bow_vectorizer.transform([mystery_postcard])

# Define friends_classifier:
goldman_docs[7]
henson_docs[40]
wu_docs[28]
friends_classifier = MultinomialNB()
# Train the classifier:
friends_classifier.fit(friends_vectors, friends_labels)
# Change predictions:
predictions = friends_classifier.predict(mystery_vector)


mystery_friend = predictions[0] if predictions[0] else "someone else"

# Uncomment the print statement:
print("The postcard was from {}!".format(mystery_friend))
# Define friends_vectors:

# Define mystery_vector: 


# Define friends_classifier:

# Train the classifier:

# Change predictions:


# Uncomment the print statement:
#print("The postcard was from {}!".format(mystery_friend))