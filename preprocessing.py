import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk


# Create A Function for Text Preprocessing
def text_preprocessing(text, stop_words, lemmatizer):

    # Case folding
    text = text.lower()

    # Mention and Hashtags removal
    text = re.sub(r"@[A-Za-z0-9_]+|#[A-Za-z0-9_]+", " ", text)

    # Newline removal (\n)
    text = re.sub(r"\\n", " ", text)

    # URL and Non-letter removal
    text = re.sub(r"http\S+|www.\S+|[^A-Za-z\s']", " ", text)

    # Tokenization
    tokens = word_tokenize(text)

    # Stopwords removal
    tokens = [word for word in tokens if word.lower() not in stop_words]

    # Lemmatization instead of stemming
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Combining Tokens
    processed_text = ' '.join(tokens)

    return processed_text
