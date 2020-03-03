import os
import urllib.request
import xlrd
headers = {
    "Cookie": "UM_distinctid=16685e0279d3e0-06f34603dfa898-36664c08-1fa400-16685e0279e133; bdshare_firstime=1539844405694; gsScrollPos-1702681410=; CNZZDATA1254092508=1744643453-1539842703-%7C1539929860; _d_id=0ba0365838c8f6569af46a1e638d05",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
}
path = "D://images/"
if not os.path.exists(path):
    os.mkdir(path)
data = xlrd.open_workbook("0201.xlsx")
table = data.sheet_by_name("Sheet0")
allx = table.nrows
namex = table.row_values(0)
i = 0
while i <= allx:
    if namex[i] == "作业图片":
        setx = i
        break
    i = i + 1
t = 1
while t < 100:
    name = table.cell_value(t, 0)
    src = table.cell_value(t, setx)
    t = t + 1
    print(name)
    print(src)
    urllib.request.urlretrieve(src, path + name + ".jpg")
    print("-------- downloading ---------")
    print("------ download done -------")
