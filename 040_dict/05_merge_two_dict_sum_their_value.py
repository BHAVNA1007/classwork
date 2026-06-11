#05_merge_two_dict_sum_their_value

d1 = {'goa': 5, 'nepal': 3, 'delhi': 8}
d2 = {'goa': 2, 'hyd': 6, 'delhi': 8 }

merged = d1.copy()

for k, v in d2.items():
    merged[k] = merged.get(k,0)+v
print(merged)    