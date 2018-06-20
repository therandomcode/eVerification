# Importing
import pandas
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

#Set up file to export to - it's a .js we'll export in our script
f = open('getLists.js', 'w')
f.close()

waltFile = "walt-data.xlsx"

info = pandas.read_excel(waltFile, skiprows = [0,1])
names = info["Legal Name"].tolist();
firstNames = [];
lastNames = [];
people = [];
andrewids = info["Andrew ID"].tolist();
dates = info["Continuous Service Date"].tolist();
eVerify = info["E-verify Initiate Date"].tolist();

def testAlign(firstNames, lastNames, andrewids, dates, eVerify):
    print("Testing name alignment...")
    print(firstNames[13200])
    print(lastNames[13200])
    print(andrewids[13200])
    print(dates[13200])
    print(eVerify[13200])
    print("Done testing")
    return

def cleanNameData(names, firstnames, lastnames):          
    for x in xrange(0, len(names)):
        if ',' in names[x]:
            lastNames.append(names[x].split(',')[0].strip());
            firstNames.append(names[x].split(',')[1].strip());
        else:
            #In some rarer cases, no firstname is listed. Ignore that. 
            lastNames.append(names[x].strip())
            firstNames.append(" ")
    ## This is arguably a good place to cleanDates() so that the seconds don't show
    return

def makeJavascriptLists(firstNames, lastNames, andrewids):
    for person in xrange (0, len(firstNames)):
        people.append([andrewids[person],lastNames[person],firstNames[person], eVerify[person], dates[person]])
        f = open('getLists.js', 'a')
        f.write( '[' + andrewids[person] + ', '
                 + lastNames[person] + ', '
                 +  firstNames[person] + '], '
                 )
        f.close()
    return
        


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
## can access

##f.write("var firstNames = " + firstNames);
##f.write("var lastNames = " + lastNames);
##f.write("var andrewids = " + andrewids);

testAlign(firstNames, lastNames, andrewids, dates, everify)
cleanNameData(names, firstnames, lastnames)
makeJavascriptLists(firstNames, lastNames, andrewids)
