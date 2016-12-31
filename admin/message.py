import pickle

PklFile =  open('message.pkl', 'rb')
DicName, DicId, DicWriter = pickle.load(PklFile)
# DicName:   Name   -> ID
# DicId:     ID     -> Name, Writer, FileZip, FileMobi, TimeZip
# DicWriter: Writer -> IDs
PklFile.close()
