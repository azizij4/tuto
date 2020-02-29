import os
import shutil
#shutil.copytree("\\Users\\ricky\\Desktop\\batch", "\\Users\\ricky\\Desktop\\fil\\")
os.chdir("\\Users\\ricky\\Desktop\\batch")
for index,allfiles in enumerate(os.listdir(),start=1):
	f_names , f_ext = os.path.splitext(allfiles)
	f_name = os.path.splitext(allfiles)[0]
	file_ex = os.path.splitext(allfiles)[1]
	if file_ex == '.mp3' or file_ex == '.m4a':
		print(index,'-',f_name, file_ex,'\n')
	else:
		print("no such file")
		break


