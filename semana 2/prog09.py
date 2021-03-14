import os
from datetime import datetime

os.getcwd()

os.chdir('C:\Users\pablo\Desktop')
os.listdir()

os.mkdir('OS-Demo')
os.makedirs('OS-Demo/Sub-Dir-1')


os.rmdir('OS-Demo')
os.removedirs('OS-Demo')

os.rename('test.txt', 'demo.txt')

for dirpath, dirnames, filenames in os.walk('C:\Users\pablo\Desktop'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()


os.environ.get('HOME')
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')


os.path.basename
os.path.dirname('/tmp/test.txt')
os.path.isfile('/tmp/test.txt')
os.path.splitext('/tmp/test.txt')
