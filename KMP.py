def KMP(text, pattern):
    ans = [] # indexes
    lps = buildPattern(pattern)
    k = 0
    for i in range(len(text)):
        while k > 0 and pattern[k] != text[i]:
            k = lps[k-1]
        if pattern[k] == text[i]:
            k += 1
        if k == len(pattern):
            ans.append(i - len(pattern) + 1)
            k = lps[k-1]
    return ans

def buildPattern(p):
    pi = [0]*len(p)
    lenLPS = 0 # Length of Previous Longest Prefix Suffix
    for i in range(1, len(p)):
        while lenLPS > 0 and p[lenLPS] != p[i]:
            lenLPS = pi[lenLPS - 1]
        if p[lenLPS] == p[i]:
            lenLPS += 1
        pi[i] = lenLPS
    return pi

def KMP_Trace(text, pattern):
    lps = buildPattern(pattern)
    k = 0
    for i in range(len(text)):
        print(' ' * (i) + "_")
        print(text)
        print(' ' * (i-k) + pattern[:k+1])
        while k > 0 and pattern[k] != text[i]:
            k = lps[k-1]
            print(' ' * (i-k) + pattern[:k+1])
        if pattern[k] == text[i]:
            k += 1
        if k == len(pattern):
            print("Found at index :", i - len(pattern) + 1)
            k = lps[k-1]


# KMP_Trace("AABAACAADAABAABA", "AABA")
print(buildPattern("ababbabbabbababbabb"))
t = "xyztrwqxyzfg"
p = "xyz"
print(KMP(t, p))