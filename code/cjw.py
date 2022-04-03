def add_words(spr_list, word):
    
    """
    spr_list: single words list
    word: the merge words list
    """
    
    r_list = []
    for i in range(len(spr_list)-1):
        if spr_list[i]+spr_list[i+1] == word:
            spr_list[i] = word
            r_list.append(i+1)
    count = 0
    for k in r_list:
        spr_list.pop(k-count)
        count += 1
        
    return spr_list
