#!/usr/bin/python3
def best_score(n_dict):
    return max(n_dict, key=n_dict.get) if n_dict else None
