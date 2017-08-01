
import os, re, csv
from datetime import datetime

# 不處理的檔案
ExFile = ['filename.csv', 'DirFunc.py']

# 要處理的資料夾路徑
FileDirPath = []
# 印出用的
sizeLevel = ("B", "kB" , "MB", "GB", "TB")

def main():
    # 取得當前路徑
    fpath = os.path.abspath(__file__)    
    L1 = re.match("","")
    for L1 in re.finditer("[/\\\]", fpath): pass
    fpath = fpath[:L1.regs[0][0]]
    FileDirPath.append(fpath)

    i = 0
    while(i <= len(FileDirPath)-1 ):
        GetOneDirFile(FileDirPath[i])
        i += 1

    print("Done")

def GetOneDirFile(fpath):

    # 取得所有檔名
    dirs = os.listdir(fpath)
    # 開檔案
    # with open('filename.csv', 'w') as Mycsv: # 新檔案寫入模式
    with open('filename.csv', 'a' , encoding = "utf-8") as Mycsv:  # 舊檔案增加模式 append mode
        # 拿筆
        MyPen = csv.writer(Mycsv , delimiter='\t' )
        # 先空一行壓壓驚
        MyPen.writerow([])
        # 寫時間
        MyPen.writerow(["Time : " + str(datetime.now())])
        MyPen.writerow(["Directory : " + fpath])

        for names in dirs:
            # 全檔名
            tempFullPath = fpath + os.sep + names

            # 跳過列表的檔案
            if names in ExFile: continue

            # 若遇到資料夾 就加入下次分析的資料夾清單中 但是這次不列表
            if os.path.isdir(tempFullPath):
                FileDirPath.append(tempFullPath)
                continue

            temp = names.split(".")
            # 若遇到沒有主檔名的檔案 印出(None)
            if temp[0] == "": temp[0] = "(None)"

            # 處理副檔名
            i = 1
            subfilename = ""
            while( i < len(temp) ):
                subfilename += "." + temp[i]
                i += 1

            fsize = translateSize(os.path.getsize(tempFullPath))
            # 印出主檔名 副檔名 檔案大小
            MyPen.writerow(["",temp[0], subfilename, fsize[0], sizeLevel[fsize[1]] ])

        # 隨手關檔好習慣
        Mycsv.flush()
        Mycsv.close()

def translateSize(fsize, lv = 0):
    # lv 0 -> Byte
    # lv 1 -> kB
    # lv 2 -> MB
    # lv 3 -> GB
    # lv 4 -> TB
    if fsize < 1024: return (fsize , lv)
    else: return translateSize(int(fsize/1024) , lv+1)

if __name__ == '__main__':
    main()
