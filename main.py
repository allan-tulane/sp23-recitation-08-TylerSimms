
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('boo--k', 'b--ack'), ('kooka-bu-rra-', 'kook-yb-ir--d'), ('-eleph-ant','rele--vant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    # TODO -  implement memoization
    if (S, T) in MED:
        return MED[(S, T)]
    if (S == ""):
        return len(T)
    if (T == ""):
        return len(S)
    else:
        if (S[0] == T[0]):
            MED[(S, T)] = fast_MED(S[1:], T[1:])
        else:
            MED[(S, T)] = 1 + min(fast_MED(S, T[1:]), fast_MED(S[1:], T))
    return MED[(S, T)]


def fast_align_MED(S, T):
    return fast_align_MED_helper(S, T, MED)[1][0], fast_align_MED_helper(S, T, MED)[1][1]

def fast_align_MED_helper(S, T, MED):
    # TODO - keep track of alignment
    align_S = ""
    align_T = ""
    while len(S) != 0 or len(T) != 0:
        s = fast_MED(S,T)
        i = fast_MED(S,T[:-1])
        d = fast_MED(S[:-1],T)
        min_ed = min(s, i, d)
        
        if min_ed == s:
            align_S = S[-1] + align_S
            align_T = T[-1] + align_T       
            S = S[:-1]
            T = T[:-1]
        elif min_ed == i:
            align_S = "-" + align_S
            align_T = T[-1] + align_T
            T = T[:-1]  
        else:
            align_T = "-" + align_T
            align_S = S[-1] + align_S           
            S = S[:-1]

    align_S = S + align_S
    align_T = T + align_T
    return fast_MED(S, T), (align_S, align_T)
    

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
