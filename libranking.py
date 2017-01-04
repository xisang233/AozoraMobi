import pickle

with open(r'admin\ranking_2016.pkl', 'rb') as f:
    rhtml, rtxt = pickle.load(f)

def ranking():
    Range = input('range?(eg.1-20):')
    if '-' not in Range:
        return
    else:
        start, end = Range.split('-')
        start = int(start)
        end = int(end)
        Result = []
        for each in rtxt[start-1 : end]:
            Result.append(each[4])
        return Result
