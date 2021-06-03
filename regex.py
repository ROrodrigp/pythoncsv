#match() y search() busca un patrón y regresa un booleano 
import re 
text = 'This is a good day'

if re.search('good',text):
    print('Wonderful')
else:
    print('Not great bro')

#split() divide la cadena y findall() devuelve las veces que aparece el patron en la cadena 
text = "Amy works diligently. Amy gets good grades. Our student Amy is succesful."
 
print(re.split('Amy',text))
print(re.findall('Amy',text))


# Anchors specify the start and/or the end of the string that you are trying to match. The caret character ^
# means start and the dollar sign character $ means end. If you put ^ before a string, it means that the text
# the regex processor retrieves must start with the string you specify. For ending, you have to put the $
# character after the string, it means that the text Regex retrieves must end with the string you specify.

print(re.search('^Amy works',text))
print(re.search('succesful.$',text))


#                               PATTERNS AND CHARACTERS CLASSES
grades = "ACAAAABCBCBAA"
print(re.findall('B',grades))

# If we wanted to count the number of A's or B's in the list, we can't use "AB" since this is used to match
# all A's followed immediately by a B. Instead, we put the characters A and B inside square brackets
print(re.findall('[BA]',grades))
print(re.findall('BA',grades))
# Let´s built a simple regex to parse out all instances where this student receive an A followed by a B or a C
print(re.findall('[A][B-C]',grades))
print(re.findall('AC|AB',grades))
# We can use the caret with the set operator to negate our results. For instance, if we want to parse out only
# the grades which were not A's
print(re.findall('[^A]',grades))
print(re.findall('^[^A]',grades))

#                                    QUANTIFIERS
# Quantifiers are the number of times you want a pattern to be matched in order to match. The most basic
# quantifier is expressed as e{m,n}, where e is the expression or character we are matching, m is the minimum
# number of times you want it to matched, and n is the maximum number of times the item could be matched.

print(re.findall('A{2,10}',grades))
print(re.findall('A{1,1}A{1,1}',grades))

# Using this, we could find a decreasing trend in a student's grades
print(re.findall("A{1,10}B{1,10}C{1,10}",grades))


# Now, that's a bit of a hack, because we included a maximum that was just arbitrarily large. There are three
# other quantifiers that are used as short hand, an asterix * to match 0 or more times, a question mark ? to
# match one or more times, or a + plus sign to match one or more times. Lets look at a more complex example,
# and load some data scraped from wikipedia

with open("ferpa.txt","r") as file:
    # we'll read that into a variable called wiki
    wiki=file.read()
#print(wiki)

# Scanning through this document one of the things we notice is that the headers all have the words [edit]
# behind them, followed by a newline character. So if we wanted to get a list of all of the headers in this
# article we could do so using re.findall
print(re.findall("[a-zA-Z]{1,100}\[edit\]",wiki))

print(re.findall('[\w]{1,100}\[edit\]',wiki))

print(re.findall('[\w]*\[edit\]',wiki))
print(re.findall('[\w ]*\[edit\]',wiki))

for title in re.findall('[\w ]*\[edit\]',wiki):
    print(re.split('[\[]',title)[0])



#                                               GROUPS
# To group patterns together you use parentheses, which is actually
# pretty natural. Lets rewrite our findall using groups
print('\n\n\n')
print(re.findall("([\w ]*)(\[edit\])",wiki))
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.groups())


for item in re.finditer('([\w ]*)(\[edit\])',wiki):
    print(item.group(1))
