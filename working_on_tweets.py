import nltk
import re
import train_extracting
import test_operation
path_traindata='training_final'
path_testdata_in='test_tweets'
path_testdata_out='test_prediction'
(politics,sports)=train_extracting.train_extract(path_traindata)
#Function for processing of the tweets
def process_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','',tweet)	
    tweet = re.sub('@[^\s]+','',tweet)    
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = tweet.strip()
    tweet = tweet.rstrip('\'"')
    tweet = tweet.lstrip('\'"')
    return tweet

word_taken_training=[]
filtered_tweets=[]
#Pre-processing of tweets
for (word,label) in politics+sports:
    str1=process_tweet(word)
    word_taken_training=[i.lower() for i in str1.split() if len(i)>=2]
    filtered_tweets.append((word_taken_training,label))
    
#Functions used for Feature Extraction
def extract_words(tweets):
    all_wrds=[]
    for (word,label) in tweets:
      all_wrds.extend(word)
      return all_wrds

def feature(wordlist):
    feature_extracted = nltk.FreqDist(wordlist).keys()
    return feature_extracted
#Feature Extraction
wrd_features= feature(extract_words(filtered_tweets))

def extract_features(docs):
    feature_dict={}
    set(docs)
    for word in wrd_features:
     feature_dict["consists(%s)" % word] = (word in docs)
    return feature_dict  
#Training of the dataset. 
train_set= nltk.classify.apply_features(extract_features, filtered_tweets)
classifier= nltk.NaiveBayesClassifier.train(train_set)

#extration of the test data set
(test_tweets,test_ids)=test_operation.test_extract(path_testdata_in)
prediction=[]

#Testing and classification on the test_data_set
for i in range(0,len(test_tweets)):
    prediction.append(str(classifier.classify(extract_features(test_tweets[i]))))
        
total_predictions=test_operation.test_predict(path_testdata_out,prediction,test_ids)
print "Total no of tweets processed in the test data= " + str(total_predictions)
#END OF THE PROGRAM
print "END OF PROGRAM"
