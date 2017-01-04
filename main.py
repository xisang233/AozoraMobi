import libsearch
import libranking
import shutil

def Move(Id):
    Name, Writer, FileZip, FileMobi = libsearch.DicId[Id][:4]
    shutil.copy('./mobifile/' + FileMobi, Writer + ' ' + Name + '.mobi')
    return Writer + ' ' + Name + '.mobi'

while True:
    move = input('s-search, r-ranking:')
    if move == 's':
        Result = libsearch.find()
    elif move == 'r':
        Result = libranking.ranking()
        
    i = 0
    for Id in Result:
        print('%03d -->' %i, libsearch.DicId[Id])
        i += 1
    Numbers = input('Number:')
    Numbers = Numbers.replace(' ', ' ')
    if ' ' not in Numbers:
        Move(Result[int(Numbers)])
    else:
        Numbers = Numbers.split(' ')
        for Id in Numbers:
            Move(Result[int(Id)])

