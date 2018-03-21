# Importing
import pandas

# Testing

# Ensure the names were alive
# THIS IS A VISUAL TEST - IT CANNOT FAIL - please look at manual output
def testAlign(firstNames, lastNames, andrewids):
    print("Testing name alignment...")
    print(firstNames[13200])
    print (lastNames[13200])
    print (andrewids[13200])
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
            
for x in xrange(0, len(names)):
    #print names[x].split(',')[0]
    if ',' in names[x]:
        lastNames.append(names[x].split(',')[0].strip() );
        firstNames.append(names[x].split(',')[1].strip() );
    else:
        lastNames.append(names[x].strip() )
        firstNames.append(" ")
andrewids = info["Andrew ID"].tolist();
dates = info["Continuous Service Date"].tolist();
eVerify = info["E-verify Initiate Date"].tolist();

print(firstNames[0:100]);
##
##sortedFirstNames = firstNames.sort();
##sortedLastNames = lastNames.sort();
##sortedAndrewIDs = andrewids.sort();

##f.write("var firstNames = " + firstNames);
##f.write("var lastNames = " + lastNames);
##f.write("var andrewids = " + andrewids);

f.close()
