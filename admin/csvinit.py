import csv
import pickle
import datetime
import os
import shutil

def PklMake():
    DicName = {}
    DicWriter = {}
    DicId = {}

    JumpCpr = 0
    JumpZip = 0
    JumpNoAozora = 0
    CountSuc = 0

    with open('list_person_all_extended_utf8.csv', encoding = 'utf-8') as csvfile:
        read = csv.reader(csvfile)
        for book in read:
            book_id = book[0]
            book_name = book[1] + book[4]

            cpr_flag = book[10]
            # 著作权情况，仅收录过期作品
            # 著作権存続フラグ。著作権のない作品だけダウンロード可能にする
            if cpr_flag == 'なし':
                book_cpr = False
            else:
                book_cpr = True
            if book_cpr:
                JumpCpr += 1
                continue
                # 若著作权未消失则跳过
                # 著作権存続の場合は飛ばす

            book_writer = book[15] + book[16]
            if 'http://www.aozora.gr.jp/' in book[45]:
                file_zip = book[45].split('/')[-1]
                if file_zip == '':
                    JumpZip += 1
                    continue
                time_zip = datetime.datetime.strptime(book[46], '%Y-%m-%d')
                file_mobi = file_zip[:-4] + '.mobi'
            else:
                JumpNoAozora += 1
                continue

            CountSuc += 1
            book_id = int(book_id)
            DicName[book_name] = book_id
            DicId[book_id] = (book_name, book_writer, file_zip, file_mobi, time_zip)
            if book_writer in DicWriter:
                DicWriter[book_writer] += [book_id]
            else:
                DicWriter[book_writer] = [book_id]

    PklFile = open('message.pkl', 'wb')
    pickle.dump((DicName, DicId, DicWriter), PklFile)
    PklFile.close()
    print('Pkl file making finished!', CountSuc, 'files successed, ', JumpCpr, 'files Copyright',
          JumpZip, 'files No file', JumpNoAozora, 'files Not in Aozora.')

def FileCheck():
    ZipList = os.listdir('../zipfile')
    MobiList = os.listdir('../mobifile')
    NoMobi = []
    NoZip  = []
    NoMobiZip = []

    with open('message.pkl', 'rb') as PklFile:
        DicId = pickle.load(PklFile)[1]
    for id in DicId:
        ZipFile = DicId[id][2]
        MobiFile = DicId[id][3]
        if ZipFile in ZipList:
            if MobiFile in MobiList:
                continue
            else:
                NoMobi.append(MobiFile)
                NoMobiZip.append(ZipFile)
        else:
            NoZip.append(ZipFile)
    return NoMobi, NoZip, NoMobiZip

PklMake()
print(FileCheck())
