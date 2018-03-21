function myFunction() {
  // Declare variables 
  var input, filter, table, tr, td, i;
	var andrewID, name, status;
	var eStatus, yStatus, nStatus, exemptStatus, errorMessage;
	var andrewIDIndex, nameIndex, statusIndex, dateIndex;
	
	var numResults = 0;
	
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase().trim();
  table = document.getElementById("studentsTable");
  tr = table.getElementsByTagName("tr");
	
	eStatus = document.getElementById("eStatus");
	yStatus = document.getElementById("yStatus");
	nStatus = document.getElementById("nStatus");
	exemptStatus = document.getElementById("exemptStatus");
	errorMessage = document.getElementById("errorMessage");
	
	//Here's where in the table to search for each kind of element
	andrewIDIndex = 0;
	nameIndex = 1;
	statusIndex = 2;
	dateIndex = 3;
	
	eStatus.style.display = "block";

  // Loop through all table rows, and hide those who don't match the search query
	//Part 1: Search only for Andrew ID
  for (i = 0; i < tr.length; i++) {
    andrewID = tr[i].getElementsByTagName("td")[andrewIDIndex];
		name = tr[i].getElementsByTagName("td")[nameIndex];
		status = tr[i].getElementsByTagName("td")[statusIndex];
		date = tr[i].getElementsByTagName("td")[dateIndex];
    if (andrewID || name) {
			console.log(numResults);
			//If this person is on the list
			if (numResults === 0){
				console.log("Hey, no results!");
					changeDisplay("errorMessage");
				} else if (numResults > 1) {
					yStatus.style.display = "none";
					nStatus.style.display = "none";
					exemptStatus.style.display = "none";
				}
			
			var year = String(date.innerHTML);
				year = parseInt(year.substring(year.length - 4));
				if (year < 1986){status.innerHTML = "exempt";}
			
      if ((andrewID.innerHTML.toUpperCase().indexOf(filter) > -1) || (name.innerHTML.toUpperCase().indexOf(filter) > -1))  {
				numResults++;
        tr[i].style.display = "";  	

				if (status.innerHTML.toUpperCase() == "E-VERIFIED"){
				//display only yStatus
					if (numResults === 1) {
						changeDisplay("yStatus");
					} else {
						yStatus.style.display = "none";
						nStatus.style.display = "none";
						exemptStatus.style.display = "none";
					}
			}
			else if (status.innerHTML.toUpperCase() == "-"){
				//display only yStatus
				if (numResults === 1) {
						changeDisplay("nStatus");
					} else {
						yStatus.style.display = "none";
						nStatus.style.display = "none";
						exemptStatus.style.display = "none";
					}
      } 
			else if (status.innerHTML.toUpperCase() == "EXEMPT"){
				//display only yStatus
				if (numResults === 1) {
						changeDisplay("exemptStatus");
					} else {
						yStatus.style.display = "none";
						nStatus.style.display = "none";
						exemptStatus.style.display = "none";
					}
			}
			}
			
			else {
        tr[i].style.display = "none";
      }
    } 
  }
}

function changeDisplay(displayMessage){
	errorMessage.style.display = "none";
	yStatus.style.display = "none";
	nStatus.style.display = "none";
	exemptStatus.style.display = "none";
	if (displayMessage == "errorMessage"){errorMessage.style.display = "block";}
	if (displayMessage == "yStatus"){yStatus.style.display = "";}
	if (displayMessage == "nStatus"){nStatus.style.display = "";}
	if (displayMessage == "exemptStatus"){exemptStatus.style.display = "";}
}