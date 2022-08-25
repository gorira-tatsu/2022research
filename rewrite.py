import os
import shutil
import glob
import re

file_path = ''
file_author = ''
file_join = []

os.system(f'mkdir {file_author}')

for i,j in enumerate(glob.glob(file_path + '/*/*/*')):
    shutil.copyfile(j, f'{file_author}/{i}.txt')

os.system(f'nkf -w --overwrite {file_author}/*')

for i in glob.glob(f'{file_author}/*'):
    with open(i) as f:
        s = f.read()
        s = re.sub('《.*?》', '', s)
        s = re.sub('［.*?］', '', s)
        s = re.sub('｜', '', s)
        s = re.sub('[「-」]', '', s)
        s = s.split()

        for i in range(2):
            try:
                del s[0:s.index('-------------------------------------------------------')+1]
            except ValueError:
                break

        try:
            del s[s.index([s for s in s if '底本' in s][0]):]
        except IndexError:
            pass

        s = ''.join(s)
        file_join.append(s)

with open(f'{file_author}_texts.txt','w') as f:
    f.write(''.join(file_join))

os.system(f'rm -r {file_author}')
