import nltk

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
sentence = [("a", "DT"),("clever", "JJ"),("fox","NN"),("was","VBP"),("jumping","VBP"),("over","IN"),("the","DT"),("wall","NN")]
grammar = "NP:{<DT>?<JJ>*<NN>}"
parser_chunking=nltk.RegexpParser(grammar)
parser_chunking.parse(sentence)
Output_chunk=parser_chunking.parse(sentence)
output = Output_chunk
output.draw()