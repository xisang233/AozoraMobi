import shutil
import pickle

PklFile =  open('./admin/message.pkl', 'rb')
DicName, DicId, DicWriter = pickle.load(PklFile)
# DicName:   Name   -> ID
# DicId:     ID     -> Name, Writer, FileZip, FileMobi, TimeZip
# DicWriter: Writer -> IDs
PklFile.close()

def SearchName(Name):
    List = []
    for Names in DicName:
        if Name in Names:
            List.append(DicName[Names])
    return List

def SearchWriter(Writer):
    List = []
    for Writers in DicWriter:
        if Writer in Writers:
            List += DicWriter[Writers]
    return List

def Search(Name = "", Writer = ""):
    if Name != '' and Writer == '':
        Result = SearchName(Name)
    elif Writer != '' and Name == '':
        Result = SearchWriter(Writer)
    else:
        ResultName = SearchName(Name)
        ResultWriter = SearchWriter(Writer)
        Result = []
        for Id in ResultName:
            if Id in ResultWriter:
                Result.append(Id)
    return Result

def Move(Id):
    Name, Writer, FileZip, FileMobi = DicId[Id][:4]
    shutil.copy('./mobifile/' + FileMobi, Writer + ' ' + Name + '.mobi')
    return Writer + ' ' + Name + '.mobi'

def find():
    FileList = []
    Input = input('Search:')
    if Input == '':
        exit()
    elif ' ' not in Input:
        Result = Search(Input)
    else:
        ListInput = Input.split(' ')
        Result = Search(ListInput[0], ListInput[1])

    i = 0
    for Id in Result:
        print('%03d -->' %i, DicId[Id])
        i += 1
    Numbers = input('Number:')
    Numbers = Numbers.replace(' ', ' ')
    if ' ' not in Numbers:
        Move(Result[int(Numbers)])
    else:
        Numbers = Numbers.split(' ')
        for Id in Numbers:
            Move(Result[int(Numbers)])
            FileList.append(Id)
    return FileList
