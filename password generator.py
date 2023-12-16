counter = 0
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
              'v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

file = open('wordlist.txt', 'w')

for i in characters:
    for j in characters:
        for k in characters:
            for l in characters:
                guess = str(i) + str(j) + str(k) + str(l)
                file.write(guess)
                file.write('\n')
                counter += 1

print('wordlist of {} passwords created'.format(counter))
