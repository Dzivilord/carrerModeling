# Trans_Tokenize_DeepTranslator.py
from deep_translator import GoogleTranslator
import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

def translate_text_deep(text, index=None):
    """
    Dịch một đoạn văn bản từ tiếng Việt sang tiếng Anh sử dụng deep_translator.
    
    Args:
        text (str): Chuỗi văn bản cần dịch.
        index (int, optional): Chỉ số của dòng trong DataFrame.
    
    Returns:
        tuple: (index, translated_text)
    """
    try:
        translated = GoogleTranslator(source='vi', target='en').translate(text)
        return (index, translated)
    except Exception as e:
        print(f"Lỗi khi dịch văn bản ở dòng {index}: {e}")
        return (index, None)

def translate_dataframe_column_deep(df, column_name, num_workers=5):
    """
    Dịch một cột cụ thể trong DataFrame từ tiếng Việt sang tiếng Anh sử dụng deep_translator.
    
    Args:
        df (pd.DataFrame): DataFrame đầu vào.
        column_name (str): Tên cột cần dịch.
        num_workers (int): Số luồng để thực hiện dịch song song.
    
    Returns:
        pd.DataFrame: DataFrame mới với cột đã được dịch.
    """
    df_translated = df.copy()
    texts = df_translated[column_name].astype(str).fillna('').tolist()
    total = len(texts)
    translated_texts = [None] * total  # Khởi tạo danh sách với giá trị None

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        # Tạo mapping từ future đến chỉ số dòng
        future_to_index = {executor.submit(translate_text_deep, text, idx): idx for idx, text in enumerate(texts)}
        
        for future in as_completed(future_to_index):
            idx = future_to_index[future]
            try:
                index, translated = future.result()
                translated_texts[index] = translated
                if translated is not None:
                    print(f"Đã dịch dòng {index + 1}/{total}")
                else:
                    print(f"Dòng {index + 1}/{total} không thể dịch.")
            except Exception as e:
                print(f"Lỗi khi xử lý dòng {idx}: {e}")
                translated_texts[idx] = None
    
    df_translated[column_name] = translated_texts
    return df_translated
