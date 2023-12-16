import zipfile
import time

path = input('Enter path of the zipfile: ')

zipf = zipfile.ZipFile(path)

global result
result = 0
global tried
tried = 0
c = 0

if not zipf:
    print('The zip file is not protected! You can open it.')
else:
    starttime = time.time()

    wordListFile = open('wordlist.txt', 'r', errors = 'ignore')
    body = wordListFile.read().lower()
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        password = word.encode('utf-8').strip()
        c += 1
        print('Trying to decode the password {}'.format(word))

        try:
            with zipfile.ZipFile(path, 'r') as zf:
                zf.extractall(pwd = password)
                print('Success! The password is ' + word)
                endtime = time.time()
                result = 1
            break
        except: pass

duration = endtime - starttime
if result == 0:
    print('Sorry password not found. A total of ' + str(c) + 'possible combinations tried in ' + str(duration) + 'seconds. password is not of 4 characters')

else:
    print('Congratulations! Password found after trying ' + str(c) + ' combinations in ' + str(duration) + 'seconds')