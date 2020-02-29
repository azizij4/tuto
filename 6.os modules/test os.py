
#import shutil
#shutil.copytree("\\Users\\ricky\\Desktop\\batch", "\\Users\\ricky\\Desktop\\fil\\")
#myfile = os.chdir("\\Users\\ricky\\Desktop\\batch")
#for index,allfiles in enumerate(os.listdir(),start=1):
#	f_names , f_ext = os.path.splitext(allfiles)
#	f_name = os.path.splitext(allfiles)[0]
#	file_ex = os.path.splitext(allfiles)[1]
#	if file_ex == '.mp3' or file_ex == '.m4a':
#		print(index,'-',f_name, file_ex,'\n')
#	else:
#		print("no such file")
#		break





#myfile1 = os.listdir(myfile)
#for myfile2 in myfile1:
#	name ,ex = os.path.splitext(myfile2)
#	with open("\\Users\\ricky\\Desktop\\batch",'r') as batch:
#		pass

import os
import shutil
from pathlib import Path
myfile = Path("\\Users\\ricky\\Desktop\\files")
if  os.path.exists(myfile):
	if os.path.exists(myfile):
		shutil.copytree("\\Users\\ricky\\Desktop\\files", "\\Users\\ricky\\Desktop\\fiew2")
		print("sucessfully copied")
	else:
		print('file already copied or existed')	
else:
	print('path not exist')	







