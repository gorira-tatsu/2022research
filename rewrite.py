import os
import shutil
import glob
import re

file_path = ''
file_author = ''
file_join = []
name = []
make_test_data = False

os.system(f'mkdir {file_author}')

for i,j in enumerate(glob.glob(file_path + '/*/*/*')):
    shutil.copyfile(j, f'{file_author}/{i}.txt')

os.system(f'nkf -w --overwrite {file_author}/*')

def preprocessing():
    for i in glob.glob(f'{file_author}/*'):
        with open(i) as f:
            s = f.read()
            s = re.sub('《.*?》', '', s)
            s = re.sub('［.*?］', '', s)
            s = re.sub('｜', '', s)
            s = re.sub('[「-」]', '', s)
            s = s.replace('。', '')
            s = s.replace('、', '')
            s = s.split()

            name.append(s[0])

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
    

if not make_test_data:
    preprocessing()

    with open(f'{file_author}_train.txt','w') as f:
        f.write(''.join(file_join))

    os.system(f'mecab -Owakati {file_author}_train.txt -o {file_author}_train_wakati.txt')
    os.system(f'nkf -w --overwrite {file_author}_train_wakati.txt')

    os.system(f'rm {file_author}_train.txt')
    os.system(f'rm -r {file_author}')


else:
    preprocessing()

    for i,j in enumerate(file_join):
        with open(f'{file_author}/bin_{name[i]}_{i}.txt', 'w') as q:
            q.write(j)

        os.system(f'mecab -Owakati {file_author}/bin_{name[i]}_{i}.txt -o {file_author}/{name[i]}_{i}_wakati.txt')

    os.system(f'rm {file_author}/[0-9]*')
    os.system(f'rm {file_author}/bin*')

    os.system(f'nkf -w --overwrite {file_author}/*')