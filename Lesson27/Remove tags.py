# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(string):
    i = 0
    list = []
    start = 0
    stop = 0
    startflag = 0
    left = 0
    over = 0
    current = ""
    while i < len(string):
        current = string[i]
        if string[i] == '<':
            stop = i
            over = 1
            left = 1
            startflag = 0
        if string[i] == '>' and left == 1:
            startflag = 1
            left = 0
        if string[i] == ' ' and left != 1:
            startflag = 1
            over = 1
            stop = i
        if over == 1:
            if string[start:stop] != '':
                list.append(string[start:stop])
            over = 0
            start = -1
        if startflag == 1:
            if string[i] != ' ' and string[i] != '>' and string[i] != '<':
                startflag = 0
                start = i
        i += 1
    if string[start:] != '' and string[-1] != '>' and string[-1] != ' ':
        list.append(string[start:])
    return list

                
            

print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']