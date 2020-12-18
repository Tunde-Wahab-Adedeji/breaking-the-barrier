import os
import builtins
#print(help(os))
from os import DirEntry,stat_result
#print(help(os.stat))
#print(help(stat_result))
c=os.getcwd()
d=os.stat(c,dir_fd=None,follow_symlinks=False)
k=stat_result(d)
#print(help(k))
print(k.st_blksize)

