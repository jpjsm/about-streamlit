import pickle

import streamlit as st
import pandas as pd
# Medusa imports
from medusa.picture import Picture
from medusa.loader import Loader
from medusa.CommonRawFormats import COMMON_RAW_FORMATS

if __name__ == "__main__":
    import pickle
    with open('/medusa/output/fotosvarias.pkl', 'rb') as infile:
        loaded_pictures = pickle.load(infile)
    
    print("Total pictures      : ", loaded_pictures.PictureCount)
    print("Duplicate groups    : ", len(loaded_pictures.Duplicate))
    duplicates_group_size_count = {}
    _max_group_size = 0
    for duplicate_group_id, pictures in loaded_pictures.Duplicate.items():
        _len = len(pictures)
        if _len not in duplicates_group_size_count:
            duplicates_group_size_count[_len] = 0
        
        duplicates_group_size_count[_len] += 1
        if _len > _max_group_size:
            _max_group_size = _len

    for i in range(_max_group_size,1,-1):
        if i in duplicates_group_size_count:
            print(f"\t{i} -> {duplicates_group_size_count[i]}")

    print("Identical groups    : ", len(loaded_pictures.Identical))
    identicals_group_size_count = {}
    _max_group_size = 0
    for duplicate_group_id, ids in loaded_pictures.Identical.items():
        _len = len(ids)
        if _len not in identicals_group_size_count:
            identicals_group_size_count[_len] = 0
        
        identicals_group_size_count[_len] += 1
        if _len > _max_group_size:
            _max_group_size = _len

    for i in range(_max_group_size,1,-1):
        if i in identicals_group_size_count:
            print(f"\t{i} -> {identicals_group_size_count[i]}")

    print("Color similar groups: ", len(loaded_pictures.ColorSimilar))
    colorsimilar_group_size_count = {}
    _max_group_size = 0
    for duplicate_group_id, ids in loaded_pictures.ColorSimilar.items():
        _len = len(ids)
        if _len not in colorsimilar_group_size_count:
            colorsimilar_group_size_count[_len] = 0
        
        colorsimilar_group_size_count[_len] += 1
        if _len > _max_group_size:
            _max_group_size = _len

    for i in range(_max_group_size,1,-1):
        if i in colorsimilar_group_size_count:
            print(f"\t{i} -> {colorsimilar_group_size_count[i]}")

