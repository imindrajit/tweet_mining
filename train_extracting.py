def find_2nd(str1, substr1):
   return str1.find(substr1,str1.find(substr1)+1)


def train_extract(path_train):
 train_file = open(path_train, 'r')
 politics=[]
 sports=[]
 tweet_id=[]
 #extracting training data
 for line in train_file.readlines():
   tweet_id.append(line[:line.find(' ')])
   sec_space = find_2nd(line,' ')
   tweet_label=line[line.find(' ')+1:sec_space]
   if tweet_label.startswith('P'):
     politics.append((line[sec_space+2:-2],tweet_label))
   else:
     sports.append((line[sec_space+2:-2],tweet_label))
 train_file.close()
 return (politics,sports)
  
