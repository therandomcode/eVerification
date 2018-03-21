from random import randint
import random
from array import array


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
  <tr>
    <td> afutterki </td>
    <td>Alfreds Futterkiste</td>
    <td>e-verified</td>
    <td>03-12-2010</td>
  </tr>
"""

end = """
</table>
</body>
</html>"""

f.write(beginning)

firstNames = ['Santina',
               'Delia',
'Freida',
'Lanie',
'Beatrice', 'Armandin',
'Tomasa',
'Susy',
'Luella',
'Samuel',
'Roland',
'Fran',
'Cornell',
'Agnus ',
'Adalberto',
'Deneen',
'Britt',
'Anabel ',
'Matt',
'Lorilee ',
'Launa',
'Rubye',
'Treasa ',
'Chia',
'Lena',
'Iris ',
'Ted ',
'Ione',
'Molly ',
'Oliver',
'Lenora',
'Marina ',
'Noah',
'Edelmira ',
'Briana',
'Imogene ',
'Josue ',
'Valeria ',
'Ilene ',
'Eloisa',
'Antoine ',
'Mae',
'Sheldon ',
'Madlyn ',
'Theron ',
'Loma ',
'Maryanna ',
'Muriel ',
'Luigi ',
'Vonnie'
              ,'Louise'
              ,'Kristina'
              ,'Noel'
              ,'Sohail'
              ,'Yeon Soo'
              ,'Hyun Hee'
              ,'RhoEun'
              , 'Clara'
              ,'Thomas'
              ,'Jean-Luc'
              ,'Chen'
              ,'WeiWei'
              ,'Mai',
              'May',
              'Maria',
              'Samantha',
              'Jenna',
              'Obi Wan',
              'Luke',
              'Anakin',
              'Leia',
              'Basil',
              'Padme']

lastNames = [
'Everett',
'Best',
'Villegas',
'Conner',
'Oconnell',
'Avila',
'James',
'Williams',
'Stuart',
'Montoya',
'Escobar',
'Sherman',
'Buckley',
'Hancock',
'Burns',
'Todd',
'Mitchell',
'Whitney'
,'Baird'
,'Knapp'
,'Flores'
,'Michael'
,'Schneider'
,'Hays'
,'Hampton'
,'Maxwell'
,'Meadows'
,'Luna'
,'Choi'
,'Matthews'
,'Munoz'
,'Stanton'
,'Beltran'
,'Mays'
,'Summers'
,'Scott'
,'Kline'
,'Cline'
,'Dorsey'
,'Jarvis'
,'Villanueva'
,'Franklin'
,'Reeves'
,'Wilkinson'
,'Salazar'
,'Cobb'
,'Mercado'
,'Knight'
,'Horne'
,'Rowland'
,'Chen'
,'Park'
,'Kim'
,'Wang'
,'Wagner'
,'Lu'
,'Winkelmatter'
,'Santos'
,'Marco'
,'Thomas'
,'Chavez'
,'Weisendanger',
'Choo',
'Purnell',
'Hillman',
'Chung',
'Tshen',
'Willis',
'Shelly',
'Siddartha',
'Winters',
'Johnson',
'Han',
'Kenobe',
'Skywalker',
'Organa']

firstnames = [];
lastnames = [];
andrewids = [];
dates = [];

for x in range(0,1600):
    firstname = random.choice(firstNames)
    lastname = random.choice(lastNames)
    andrewID = lastname[:6] + firstname[0:2]
    andrewID = checkAndrewID(andrewID, andrewids)
    day = randint(1,30)
    month = randint(1,12)
    year = randint(1980, 2017)
    date = str(month)+"-"+str(day)+"-"+str(year)
    firstnames.append(firstname)
    lastnames.append(lastname)
    andrewids.append(andrewID)
    dates.append(date)
    ev = random.choice(["-", "e-verified"])

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
