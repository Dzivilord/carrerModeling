from nltk.corpus import stopwords
from deep_translator import GoogleTranslator
import time
import pandas as pd
import nltk
import re
import string
def translate_column(text):
    """
    Translates the input text from Vietnamese to English.
    
    Args:
    text (str): The text to translate.
    
    Returns:
    str: The translated text.
    """
    try:
        # Clean the text if necessary (e.g., replacing underscores)
        cleaned_tokens = text.replace('_', ' ')
        
        # Xóa khoảng trắng thừa xung quanh dấu phẩy
        cleaned_tokens = re.sub(r'\s*,\s*', ', ', text)
        
        # Translate from Vietnamese to English
        translated = GoogleTranslator(source='vi', target='en').translate(cleaned_tokens)
        
        #print(f"{cleaned_tokens} -> {translated}")
        time.sleep(1)  # To avoid hitting rate limits
        
        return translated
    except Exception as e:
        print(f"Error translating {text}: {e}")
        return None

# Hàm xử lý và token hóa văn bản tiếng Anh
def process_tokenization_english(text):
    """
    Xử lý văn bản bằng cách loại bỏ dấu câu, số, stopwords và lấy tối đa số token quy định.
    
    Args:
    text (str): Chuỗi văn bản cần xử lý.
    max_tokens (int): Số lượng token tối đa cần lấy (mặc định là 5).
    
    Returns:
    list: Danh sách các token đã được làm sạch và giới hạn.
    """
    stop_words_english = set(stopwords.words('english'))
    
    # Kiểm tra nếu text là chuỗi
    if isinstance(text, str):
        # Loại bỏ dấu câu và ký tự đặc biệt
        text = re.sub(r'[•–—\-*]', '', text)  # Loại bỏ các ký tự không cần thiết
        text = re.sub(r'[^\w\s]', '', text)  # Loại bỏ tất cả dấu câu (bao gồm dấu phẩy)
        text = re.sub(r'\d+', '', text).lower()
        
        # Tokenize và loại bỏ stopwords
        tokens = [word for word in text.split() if word not in stop_words_english and word not in string.punctuation]
        unique_tokens = list(dict.fromkeys(tokens))
        # Giới hạn số token tối đa
        return unique_tokens
    
    return []
