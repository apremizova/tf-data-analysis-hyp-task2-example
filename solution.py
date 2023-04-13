import pandas as pd
import numpy as np
from scipy import stats

chat_id = 370558433 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    pval = stats.ks_2samp(x,y).pvalue
    ans = True if pval < 0.08 else False
    return ans # Ваш ответ, True или False
