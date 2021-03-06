#solution found on https://codereview.stackexchange.com/questions/28167/optimizing-edit-distance-solution

def hamming(word1, word2, subst=1):
    len1, len2 = len(word1), len(word2)
    med = [[0] * (len2 + 1) for j in range(len1 + 1)]
    for j in xrange(len1 + 1):
        for k in xrange(len2 + 1):
            if min(j, k) == 0:
                med[j][k] = max(j, k) # initialization
            else:
                diag = 0 if word1[j-1] == word2[k-1] else subst
                med[j][k] = min(med[j-1][k-1] + diag, # substite or keep
                                med[j-1][k  ] + 1,    # insert
                                med[j  ][k-1] + 1)    # delete
    return med[len1][len2]

def main():
    str1 = raw_input('String 1: ')
    str2 = raw_input('String 2: ')

    distance = hamming(str1, str2)
    print distance

if __name__ == '__main__':
    main()