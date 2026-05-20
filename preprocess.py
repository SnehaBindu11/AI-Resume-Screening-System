import re
import nltk

nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words('english'))


custom_stopwords = {

    "team",
    "project",
    "projects",
    "managed",
    "using",
    "used",
    "required",
    "preferred",
    "responsibilities"
}

stop_words.update(custom_stopwords)


def preprocess_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    tokens = word_tokenize(text)

    cleaned_tokens = []

    for word in tokens:

        if word not in stop_words and len(word) > 2:

            lemma = lemmatizer.lemmatize(word)

            cleaned_tokens.append(lemma)

    cleaned_text = " ".join(cleaned_tokens)

    return cleaned_text