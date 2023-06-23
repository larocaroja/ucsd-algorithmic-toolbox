def range_sum_queries(array, ranges):
    ret = []
    len_array = len(array)
    
    for range_ in ranges:
        l = range_[0]
        r = range_[1]
        assert l<r, f"the second element of range should be greater than the first one, but got (l, r) = ({l, r})"
        assert r <= len_array and l>=0, f"the range element out of range."

        ret.append(sum(array[l:r]))
    
    return ret
