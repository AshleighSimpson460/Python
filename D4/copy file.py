# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('c:\\Users\Ashleigh\\Desktop\\text.txt','c:\\Users\Ashleigh\\Desktop\\text_copy.txt')
shutil.copy2('c:\\Users\Ashleigh\\Desktop\\text.txt','c:\\Users\Ashleigh\\Documents\\')