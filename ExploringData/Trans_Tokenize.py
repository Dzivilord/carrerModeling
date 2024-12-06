from nltk.corpus import stopwords
from deep_translator import GoogleTranslator
import time
import pandas as pd
import nltk
import re
import string
from concurrent.futures import ThreadPoolExecutor
import numpy as np

def translate_batch(text_list):
    """
    Translates a list of texts from Vietnamese to English using GoogleTranslator.
    
    Args:
    text_list (list): List of strings to translate.
    
    Returns:
    list: List of translated texts.
    """
    try:
        # Translate the batch of texts
        translated = GoogleTranslator(source='vi', target='en').translate_batch(text_list)
        return translated
    except Exception as e:
        print(f"Error translating batch: {e}")
        return [None] * len(text_list)  # Return a list of None if an error occurs
    
processed_rows = 0  # Theo dõi số lượng dòng đã xử lý
total_rows = 0      # Tổng số dòng trong DataFrame

def process_column(df, column_name):
    """
    Xử lý một cột cụ thể trong DataFrame: tiền xử lý và dịch thuật.

    Args:
    df (pd.DataFrame): DataFrame đầu vào.
    column_name (str): Tên cột cần xử lý.

    Returns:
    pd.DataFrame: DataFrame với cột đã được xử lý.
    """
    # Tiền xử lý dữ liệu
    cleaned_texts = df[column_name].astype(str).apply(lambda x: re.sub(r'\s*,\s*', ', ', x.replace('_', ' '))).tolist()

    # Dịch toàn bộ danh sách văn bản
    translated_texts = translate_batch(cleaned_texts)

    # Gán lại kết quả đã dịch vào cột
    df[column_name] = translated_texts

    global processed_rows  # Theo dõi tiến độ xử lý
    processed_rows += len(df)
    print(f"Đã xử lý xong {processed_rows} trên tổng số {total_rows} dòng của cột {column_name}.")
    return df

def parallelize_column(df, column_name, num_partitions=50):
    """
    Xử lý song song một cột cụ thể trong DataFrame.

    Args:
    df (pd.DataFrame): DataFrame đầu vào.
    column_name (str): Tên cột cần xử lý.
    num_partitions (int): Số phần để chia nhỏ DataFrame.

    Returns:
    pd.DataFrame: DataFrame với cột đã được xử lý song song.
    """
    global processed_rows, total_rows
    processed_rows = 0
    total_rows = len(df)

    # Chia nhỏ DataFrame thành các phần
    partitions = np.array_split(df, num_partitions)

    results = []
    with ThreadPoolExecutor() as executor:
        for result in executor.map(lambda part: process_column(part, column_name), partitions):
            results.append(result)
    
    # Kết hợp các phần đã xử lý
    df = pd.concat(results)
    return df
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
