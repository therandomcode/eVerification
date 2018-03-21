from random import randint
import random
from array import array
import pandas as pd

def checkAndrewID(andrewid, andrewids):
    if andrewid in andrewids:
        andrewid = andrewid + str(randint(0,9))
        andrewid = checkAndrewID(andrewid, andrewids)
    return andrewid.lower()


f = open('index-large-table.html', 'w')
beginning = """
<html>
<head>
    <link rel="stylesheet" type="text/css" href="style.css">
    <script type="text/javascript" src="script.js"></script>
</head>
<body>
<div id = "header">
	<!--<p><a href = "new page">Report a problem <a/> </p>-->
	<h3>e-verification@CMU </h3> 
</div>

<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for Andrew ID or name..">

    <div id = eStatus>
        <div id = yStatus>
            <h2 id = yMessage> This person has been e-verified. </h2>
        </div>
        <div id = nStatus> 
            <h2 id = nMessage> This person has not been e-verified. </h2>
        </div>
        <div id = exemptStatus> 
            <h2 id = nMessage> This person is exempt from e-verification because they joined the university before 1984. </h2>
        </div>
    </div>

<div id = errorMessage>
	<h2> Sorry, no results for that! Try searching the <a href = "directory.cmu.edu"> CMU directory</a> to make sure they really exist. </h2> 
</div>



<!-- IRL load this data from .csv -->
<table id="studentsTable">
  <tr class="header">
		
		<th style = "width: 25%;">Andrew ID</th>
    <th style = "width: 25%;">Name</th>
    <th style = "width: 25%;">e-verification status</th>
		<th style = "width: 25%;">Date enrolled</th>

  </tr>
"""

end = """
</table>
</body>
</html>"""


file1 = "walt-data.xlsx"
df1 = pd.read_excel(file1, skiprows=[0,1])

f.write(beginning)


firstnames = df1["Preferred Name"].tolist();
lastnames = df1["Legal Name"].tolist();
andrewids = df1["Andrew ID"].tolist();
dates = df1["Continuous Service Date"].tolist();
eVerify = df1["E-verify Initiate Date"].tolist();

def dateToString(date):
    if date == False:
        return "-"
    else:
        return str(date.to_pydatetime())

dates = list(map((lambda x: dateToString(x)), dates))

def getEV(date):
    if date == True:
        return "e-Verified"
    else:
        return "-"

eVerify = list(map((lambda x: getEV(x)), eVerify))

#This needs to go 
for x in range(0,len(firstnames)):
##    lastname = lastnames[x].encode('UTF8')
##    firstname = firstnames[x].encode('UTF8')
##    andrewID = andrewids[x].encode('UTF8')

    lastname = lastnames[x]
    firstname = firstnames[x]
    andrewID = andrewids[x]
    
    date = dates[x]
    ev = eVerify[x]
    tableRow = ("<tr><td>"
                + str(andrewID.strip())
                + "</td>"
                + "<td>"
                + str(firstname.strip())
                + " "
                + str(lastname.strip())
                + "</td>"
                + "<td>"
                + str(ev)
                + "</td>"
                + "<td>"
                + str(date.strip())
                + "</td></tr>")

    f.write(tableRow)

f.write(end)

f.close()

