import os
import os.path

def work(path):
	resPath = r"D:\python-project\result"
	#打开文件
	f = open(path,"r",encoding = "UTF-8-sig")
	#处理每一行数据
	while True:
		lineInfo = f.readline()
		if lineInfo.split(",")[-2][-1] != "m":
			if lineInfo.split(",")[-2][-1] != "n":
				if len(lineInfo) < 5 :
					continue
		#曹阳,32010619720506042x,F,19720506,-,210005,13770848687,025-842019149,-,cy_qing@163.com,0
		mailStr = lineInfo.split(",")[9]
		nameStr = lineInfo.split(",")[0]
		#获取邮箱的字符串 cy_qing@163.com
		print(nameStr)
		dirStrTemp = mailStr.split("@")[1].split(".")[0]
		#获取邮箱类型 126/qq/other   163
		print(dirStrTemp)
		dirStr = os.path.join(resPath,dirStrTemp)
		#获取邮箱类型对应的字符串  D:\python-project\result\163
		print(dirStr)
		'''
		#代码无问题 调试BUG 
		if not os.path.exists(dirStr):
			#不存在 创建新目录
			os.mkdir(dirStr)
			
		
		#创建文件
		fileType = dirStrTemp
		filePath = os.path.join(dirStr,fileType + ".txt")
		with open(filePath,"a") as fw:
			fw.write(mailStr + "\n")
		'''
		
def getAllDirRE(path, sp = ""):
    #得到当前目录下所有的文件
    filesList = os.listdir(path)
    #处理每一个文件
    sp += "   "
    for fileName in filesList:
        #判断是否是路径（用绝对路径）
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            #print(sp + "目录：", fileName)
            #递归调用
            getAllDirRE(fileAbsPath, sp)
        else:work(fileAbsPath)
            #print(sp + "普通文件：", fileName)
			#处理普通文件
			

getAllDirRE(r"D:\python-project\newdir")
