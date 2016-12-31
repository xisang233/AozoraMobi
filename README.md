# 简体中文

## 文件夹构造:

```D:.
├─.idea
│  └─inspectionProfiles
├─admin
│  │csvinit.py
│  │list_person_all_extended_utf8.csv
│  │message.pkl
│  └─message.py
├─mobifile
│  └─ .mobi files
├─nomobi
│  └─ .zip files(临时)
└─zipfile
   └─ .zip files
```

> admin 文件夹 主要负责文件的构建和更新
>```
>    csvinit.py   由csv文件构建字典、确认字典中每一条所指向的都存在。
>    list_person_all_extended_utf8.csv  来源:github 定期查看更新
>    message.pkl  保存字典文件
>```
> mobifile 保存转换好的.mobi文件(人工批量拖入AozoraEpub3的GUI界面)
> zipfile 保存青空格式.zip压缩包(与源站相同)

## 准备工作

### 1. 分析CSV文件

将文件`list_person_all_extended_utf8.csv`移动到admin文件夹内
csvinit.py -> PklMake()
将csv文件中的内容逐条读取并打包存入到massage.pkl，以下内容不保存：

* 著作权未消失
* 'テキストファイルURL'(第45)项为空
* 文件未保存在http://www.aozora.gr.jp/

csvinit.py -> FileCheck()
逐条检查.zip文件和.mobi文件是否存在

### 2. 人工导入mobi文件

打开AozoraEpub3.jar，配置如下：
* 表題 -> 本文内 -> “表題　→　著者名”
* 拡張子 -> .mobi
* 必须确保同文件夹内有KindleGen程序
* 出力先 -> `mobifile` 文件夹
* 変換前確認　-> 取消

一次性将所有.zip文件拖入后等待即可


## 使用指南

### 搜索

打开main.py，输入关键词，中间使用空格分开。第一个关键字为作品名，第二个关键字为作者。两个关键字不可以同时为空。
然后程序会返回找到的所有文件，每个文件前都有编号，输入想要查找文件的编号即可。如不满意可以按q键重新查找。

例如：输入‘ 夏目漱石’，结果为：
> 001 --> ('イズムの功過', '夏目漱石', '2314_ruby_2291.zip', '2314_ruby_2291.mobi', datetime.datetime(2003, 10, 28, 0, 0))
002 --> ('一夜', '夏目漱石', '1086_ruby_5742.zip', '1086_ruby_5742.mobi', datetime.datetime(2011, 12, 5, 0, 0))
003 --> ('永日小品', '夏目漱石', '758_ruby_6056.zip', '758_ruby_6056.mobi', datetime.datetime(2011, 1, 13, 0, 0))
004 --> ('岡本一平著並画『探訪画趣』序', '夏目漱石', '2669_ruby_6341.zip', '2669_ruby_6341.mobi', datetime.datetime(2003, 5, 11, 0, 0))
...
102 --> ('私の経過した学生時代', '夏目漱石', '2677_ruby_6351.zip', '2677_ruby_6351.mobi', datetime.datetime(2003, 5, 25, 0, 0))
103 --> ('私の個人主義', '夏目漱石', '772_ruby_33099.zip', '772_ruby_33099.mobi', datetime.datetime(2008, 10, 5, 0, 0))

输入 001 002，这三个文件就会出现在相同文件夹内，只需使用邮箱发送到kindle上设置的地址即可。

例2：输入`こころ 夏目漱石` (注意‘ ’为半角空格)
> Search:`こころ 夏目漱石`
> 000 --> ('こころ', '夏目漱石', '773_ruby_5968.zip', '773_ruby_5968.mobi', datetime.datetime(2010, 10, 31, 0, 0))
> Number:`0`

例3：输入`銀河`
> Search:`銀河`
> 000 --> ('銀河鉄道の夜', '宮沢賢治', '43737_ruby_19028.zip', '43737_ruby_19028.mobi', datetime.datetime(2010, 11, 1, 0, 0))
> 001 --> ('銀河の下の町', '小川未明', '52057_ruby_48086.zip', '52057_ruby_48086.mobi', datetime.datetime(2012, 7, 17, 0, 0))
> 002 --> ('銀河まつり', '吉川英治', '52441_ruby_49986.zip', '52441_ruby_49986.mobi', datetime.datetime(2013, 1, 23, 0, 0))
> Number:`000`

### 推送

手动发送邮件。

## To do list

1. 自动更新
2. 人气统计
3. 模糊查找
4. cache
5. 源站排名榜
6. 快速搜索
7. GUI

## ChangeLog

0.01 2016.12.31 可用

## 已知BUG
以下四个文件不能正确转码，经确认是AozoraEpub转换出的.epub文件无法通过KindleGen转换成.mobi导致的。
> 47196_ruby_35629.zip
> 49940_txt_57517.zip
> 49946_txt_59449.zip
> 54858_ruby_49322.zip

# 日本語


## ファイルの構造と取り組み:

```D:.
├─.idea
│  └─inspectionProfiles
├─admin
│  │csvinit.py
│  │list_person_all_extended_utf8.csv
│  │message.pkl
│  └─message.py
├─mobifile
│  └─ .mobi files
├─nomobi
│  └─ .zip files(临时)
└─zipfile
   └─ .zip files
```

> admin フォルダー ファイルの組み立てと更新をすることができる
>```
>    csvinit.py   csvファイルからdicを組み立て、一つずつmobiファイルとzipファイルが存在するかを確認する
>    list_person_all_extended_utf8.csv  'http://www.aozora.gr.jp/index_pages/list_person_all_extended_utf8.zip'からダウンロードした内容、定期的に更新を確認すればよい
>    message.pkl  dicの情報を保存する
>```
> mobifile 転換されたmobiファイルを保存する(転換は自分でやる)
> zipfile .zipファイルを保存する(http://github.com/aozorabunko/aozorabunko.gitからcloneしたもの)

## 准备工作

### 1. 分析CSV文件

`list_person_all_extended_utf8.csv`をadminフォルダーに移動させる
csvinit.py -> PklMake()
csvファイルから読み取った内容を一つずつ読み取り、massage.pklに保存する。だたし、次の場合は保存しない：

* 著作権存続
* 'テキストファイルURL'(45番目)はない
* ファイルの保存先はhttp://www.aozora.gr.jp/ではない

csvinit.py -> FileCheck()
一つずつ.zipファイルと.mobiファイルが存在しているかを確認する。

### 2. .mobiファイルを導入する

guiでAozoraEpub3.jarを開き、次のように設定する：
* 表題 -> 本文内 -> “表題　→　著者名”
* 拡張子 -> .mobi
* （同じフォルダー内でのKindleGenのプログラムが必要
* 出力先 -> フォルダー `mobifile`
* 変換前確認　-> なし

設定し終わったら、.zipファイルを全部入力させ、転換するのを3時間ぐらい待てばいい
(ここでは、導入ずみのファイルを用意しておりますので、普通は導入しなくていい)

## 使用指南

### 搜索

mail.pyを開き、キーワードを入力する
打开main.py，输入关键词，中间使用空格分开。第一个关键字为作品名，第二个关键字为作者。两个关键字不可以同时为空。
然后程序会返回找到的所有文件，每个文件前都有编号，输入想要查找文件的编号即可。如不满意可以按q键重新查找。

例1：输入‘ 夏目漱石’，结果为：
> 001 --> ('イズムの功過', '夏目漱石', '2314_ruby_2291.zip', '2314_ruby_2291.mobi', datetime.datetime(2003, 10, 28, 0, 0))
002 --> ('一夜', '夏目漱石', '1086_ruby_5742.zip', '1086_ruby_5742.mobi', datetime.datetime(2011, 12, 5, 0, 0))
003 --> ('永日小品', '夏目漱石', '758_ruby_6056.zip', '758_ruby_6056.mobi', datetime.datetime(2011, 1, 13, 0, 0))
004 --> ('岡本一平著並画『探訪画趣』序', '夏目漱石', '2669_ruby_6341.zip', '2669_ruby_6341.mobi', datetime.datetime(2003, 5, 11, 0, 0))
...
102 --> ('私の経過した学生時代', '夏目漱石', '2677_ruby_6351.zip', '2677_ruby_6351.mobi', datetime.datetime(2003, 5, 25, 0, 0))
103 --> ('私の個人主義', '夏目漱石', '772_ruby_33099.zip', '772_ruby_33099.mobi', datetime.datetime(2008, 10, 5, 0, 0))

输入 001 002，这三个文件就会出现在相同文件夹内，只需使用邮箱发送到kindle上设置的地址即可。

例2：输入`こころ 夏目漱石` (注意‘ ’为半角空格)
> Search:`こころ 夏目漱石`
> 000 --> ('こころ', '夏目漱石', '773_ruby_5968.zip', '773_ruby_5968.mobi', datetime.datetime(2010, 10, 31, 0, 0))
> Number:`0`

例3：输入`銀河`
> Search:`銀河`
> 000 --> ('銀河鉄道の夜', '宮沢賢治', '43737_ruby_19028.zip', '43737_ruby_19028.mobi', datetime.datetime(2010, 11, 1, 0, 0))
> 001 --> ('銀河の下の町', '小川未明', '52057_ruby_48086.zip', '52057_ruby_48086.mobi', datetime.datetime(2012, 7, 17, 0, 0))
> 002 --> ('銀河まつり', '吉川英治', '52441_ruby_49986.zip', '52441_ruby_49986.mobi', datetime.datetime(2013, 1, 23, 0, 0))
> Number:`000`

### 推送

smtpを導入する予定だが、どうしても失敗したので、今では自分で発信しなければならない。

## To do list

1. 自動的に更新する
2. ダウンロード量の統計を取る
3. 仮名で検索する
4. 検索のcacheを作る
5. aozora.gr.jpからランキングをダウンロードし、ランキングから本を選ぶ
6. 検索のアルゴリズムには、検討する必要がある
7. GUIを作る

## ChangeLog

0.01 2016.12.31 使えるようになり、中国語と日本語のREADMEファイルの編集

## BUG

以下の四つのファイルは正確に転換することができない、原因を確認したら、AozoraEpubによって転換された.epubファイルをKindleGenで転換させるとき、エラーが発生したからです。

報告はすでに作者に提出しています：
https://github.com/hmdev/AozoraEpub3/issues/10

> 47196_ruby_35629.zip
> 49940_txt_57517.zip
> 49946_txt_59449.zip
> 54858_ruby_49322.zip
