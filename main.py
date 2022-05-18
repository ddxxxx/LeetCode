import os


filepath = '.\\'


def dfs(path):
    filenames = os.listdir(path)
    #print(filenames)
    for filename in filenames:
        d = os.path.join(path,filename)
        #print(d)
        if os.path.isdir(d):
            dfs(d)
            continue
        if d.find('test.txt') != -1:
            with open(d,'r') as f:
                filedata = f.read()
            filedata = filedata.replace(" dsm"," vendor_dsm")
            with open(d,'w') as f:
                f.write(filedata)

dfs(filepath)
