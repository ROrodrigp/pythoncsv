import re 

def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    pattern = '[A-Z][a-z]*'
    print(re.findall(pattern,simple_string))


#The dataset file in assets/grades.txt contains a line separated list of people with their grade in a class. 
#Create a regex to generate a list of just those students who received a B in the course

def grades():
    with open ("grades.txt", "r") as file:
        grades = file.read()
    
    pattern = '[A-Z][a-z ]*\s[A-Z][a-z]*\:\sB'
    return(re.findall(pattern,grades))
    # YOUR CODE HERE
   
names()
print(grades())
print(len(grades()))