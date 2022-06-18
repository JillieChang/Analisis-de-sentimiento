
import re
from nltk import TweetTokenizer
from nltk.stem import SnowballStemmer


class Preprocessor:

    _stemmer = SnowballStemmer('spanish')
    _tokenizer = TweetTokenizer().tokenize

    def __init__(self, twitter_features=None, stemming=False):
        self._twitter_features = twitter_features
        self._stemming = stemming

    def preprocess(self, message):
        if self._stemming:
            message = ' '.join(self._stemmer.stem(w) for w in self._tokenizer(message))
        return message
 
    def process_twitter_features(message, twitter_features):
        if twitter_features == Preprocessor.REMOVE:
            # remove mentions, hashtags and urls
            message = re.sub(r'((?<=\s)|(?<=\A))(@|#)\S+', '', message)
            message = re.sub(r'\b(https?:\S+)\b', '', message, flags=re.IGNORECASE)
        elif twitter_features == Preprocessor.NORMALIZE:
            # normalize mentions, hashtags and urls
            message = re.sub(r'((?<=\s)|(?<=\A))@\S+', Preprocessor.MENTION, message)
            message = re.sub(r'((?<=\s)|(?<=\A))#\S+', Preprocessor.HASHTAG, message)
            message = re.sub(r'\b(https?:\S+)\b', Preprocessor.URL, message, flags=re.IGNORECASE)
        return message
 
    def __str__(self):
        return "Preprocessor([twitter_features={0}, stemming={1}])".format(self._twitter_features, self._stemming)

    def __repr__(self):
        return "Preprocessor([twitter_features={0}, stemming={1}])".format(self._twitter_features, self._stemming)
   #NOTA: ESTE CODIGO ES UNA ADAPTACIÓN DE CARLES,V (2018). ANÁLISIS DE SENTIMIENTOS EN TWITTER