def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word) - 1 - i]
    return x

word = raw_input('Give a text: ')
y = reverse(word)
if y == word:
    print 'It is a Palindrome'
else:
    print 'It is NOT a Palindrome'
