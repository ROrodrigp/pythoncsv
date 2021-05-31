import csv 


with open ('mpg.csv') as csvfile: 
    mpg = list(csv.DictReader(csvfile))

print(mpg[0])
print(len(mpg))
print(mpg[0].keys())


print(sum(float(d['cty']) for d in mpg) / len(mpg))
print(sum(float(d['hwy']) for d in mpg) / len(mpg))


cylinders = set(d['cyl'] for d in mpg)
print(cylinders)


CtyMpgByCyl = []
for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
print(CtyMpgByCyl)



classtypes = set(d['class'] for d in mpg)
print(classtypes)

HwyMpgByClass = []
for c in classtypes:
    summpg = 0 
    classtypecount = 0 
    for d in mpg:
        if d['class'] == c:
            summpg = summpg + float(d['hwy'])
            classtypecount += 1
    HwyMpgByClass.append((c, summpg / classtypecount))
HwyMpgByClass.sort(key = lambda x: x[1])
print(HwyMpgByClass)

