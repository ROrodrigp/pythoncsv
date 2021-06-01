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

