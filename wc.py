import sys
from string import punctuation

def wordfreq(fname, stripPunc, toLower) :
    wordDict = {}
    with open(fname) as f:
        ## let's just get all the words at once.
        words = f.read().split()
        for word in words :
            if stripPunc :
                word = word.strip(punctuation)
            if toLower :
                word = word.lower()
            if word in wordDict :
                wordDict[word] += 1
            else :
                wordDict[word] = 1
    return wordDict

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("Usage: wordfreq {-nostrip -noConvert -pfile=outfile} file")
        sys.exit(-1)
        fname = sys.argv[-1]
        nostrip = '-nostrip' in sys.argv
        noConvert = '-noConvert' in sys.argv
        wd = wordfreq(fname, stripPunc=nostrip, toLower=noConvert)
        pickled = False
        for arg in sys.argv:
            if arg.startswith('--pfile'):
                ofile = arg.split('=')[1]
                pickle.dump(wd, open(ofile, 'w'))
                pickled = True
        if not pickled:
            print(wd)


