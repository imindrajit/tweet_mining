def test_extract(path_test_in):
 test_in = open(path_test_in, 'r')
 test_ids=[]
 test_tweets=[]
 for line in test_in.readlines():
   test_ids.append(str(line[:line.find(' ')]))
   #tweet_label=line[line.find(' ')+1:sec_space]
   test_tweets.append(str(line[line.find(' ')+1:]))
 test_in.close()           
 return (test_tweets,test_ids)

def test_predict(path_test_out,prediction,tweet_ids):
 count=0
 test_out=open(path_test_out,'w')
 for i in range(0,len(tweet_ids)):
     test_out.write(str(tweet_ids[i]+"  "+prediction[i]+"\n"))
     count=count+1
 return count     
