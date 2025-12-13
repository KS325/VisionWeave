
import numpy as np


ratio_dict = {
    "hakugin": np.sqrt(2), 
    "ougon": (1 + np.sqrt(5)) / 2, 
    "4:3": 4 / 3, 
    "16:9": 16 / 9, 
    "3:2": 3 / 2, 
}

def cal_size(raw_size: list, base: int, ratio):
    _, W = raw_size
    H_n = ratio2length(base, ratio)

    return [H_n, W]

def ratio2length(base, ratio):
    if (type(ratio) == int) or (type(ratio) == float):
        length = int(base * ratio)
    elif (type(ratio) == str):
        length = int(base * ratio_dict[ratio])
    return length


