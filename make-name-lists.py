# Importing
import pandas
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Testing

# Ensure the names were alive
# THIS IS A VISUAL TEST - IT CANNOT FAIL - please look at manual output
def testAlign(firstNames, lastNames, andrewids, dates, eVerify):
    print("Testing name alignment...")
    print(firstNames[13200])
    print(lastNames[13200])
    print(andrewids[13200])
    print(dates[13200])
    print(eVerify[13200])
    print("Done testing")

# Get input

# Sort into arrays: each person has a unique identifier,
# and there are 3 arrays

#Set up file to export to - it's a .js we'll export in our script
f = open('getLists.js', 'w')

waltFile = "walt-data.xlsx"

info = pandas.read_excel(waltFile, skiprows = [0,1])
names = info["Legal Name"].tolist();
firstNames = [];
lastNames = [];
people = [];

andrewids = info["Andrew ID"].tolist();
dates = info["Continuous Service Date"].tolist();
eVerify = info["E-verify Initiate Date"].tolist();
            
for x in xrange(0, len(names)):
    if ',' in names[x]:
        lastNames.append(names[x].split(',')[0].strip());
        firstNames.append(names[x].split(',')[1].strip());
    else:
        #In some rarer cases, no firstname is listed. Ignore that. 
        lastNames.append(names[x].strip())
        firstNames.append(" ")
## This is arguably a good place to cleanDates() so that the seconds don't show

for person in xrange (0, len(firstNames)):
    people.append([andrewids[person],lastNames[person],firstNames[person], eVerify[person], dates[person]])
    f.write( andrewids[person] + ', '
             ##+ lastNames[person].encode('utf-8') + ', '
             ##+  firstNames[person].encode('utf-8')
             )


print(firstNames[0:100])
print(len(firstNames))
print(len(dates)) #Continuous Service Date is formatted as a timestamp
print(len(eVerify)) #E-verification date is also formatted as a timestamp
print(len(lastNames))
print(type(dates[1]))
for myint in xrange(0, 100):
    print people[myint]

##sortedFirstNames = firstNames.sort();
##sortedLastNames = lastNames.sort();
##sortedAndrewIDs = andrewids.sort();

## Then write each of these arrays to a .js file that our script.js file
## can acccess

##f.write("var firstNames = " + firstNames);
##f.write("var lastNames = " + lastNames);
##f.write("var andrewids = " + andrewids);

testAlign(firstNames, lastNames, andrewids, dates, eVerify)

f.close()
