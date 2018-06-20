/* ------------------ TESTING CODE ------------------------------------------------------------------------------------ */

console.log("Testing the new algorithms...");

var test_first_name_list = ['Abby', 'Bianca', 'Connie', 'Maria', 'Maria',
'Maria', 'Marielle', 'Percy', 'Jack', 'James', 'John', 'Zendaya'];
var test_last_name_list = ['Smith', 'Smith', 'Smith', 'Smith', 'Smith',
'Smith', 'Smith', 'Smith', 'Smith', 'Smith', 'Smith', 'Smith'];
var test_first_name = "Bianca";

console.log("Testing with the following variables and list:");
console.log(test_first_name, test_first_name_list);

var test_results = makeListOfResults(test_first_name, null, null, test_first_name_list, null, null);

console.log("...printing results");
console.log(test_results);


/* ----------------- END TEST CODE ------------------------------------------------------------------------------------ */

/* ----------------- START TO DO LIST -----------------------

- Get and PARSE LIST of many data entries
- BINARY SORT data entries dynamically from outputted file (set this on a timer or smtn)
---> Find out if this can be done via python instead
- Make a way to display entries from an ARRAY into a TABLE
- Make a way to redisplay entries
- Ensure that search actually triggers a change in state

----------------- END TO DO LIST ------------------------- */

//function sortDataEntries(){
	/* Fill with binary search*/
//	return list[];
//}


/*Must be recieved from input via document.getElementByID */
var firstName, lastName, andrewID;
var sortedFirstNames, sortedLastNames, sortedAndrewIDs;

/*If there is a match, this finds the index of the match */
/*If there is no match, returns -1*/
function binarySearch(minIndex, maxIndex, list, searchTerm){
	while (minIndex <= maxIndex){
		currentIndex = (minIndex + maxIndex)/2 |0;
		currentElement = list[currentIndex];

		if (currentElement < searchTerm){
			minIndex = currentIndex + 1;
		}
		else if (currentElement > searchTerm){
			maxIndex = currentIndex - 1;
		}
		else {
			return currentIndex;
		}
	}
	return -1;
}

function getListOfMatches(searchTerm, myList){
	var minIndex = 0;
	var maxIndex = myList.length-1;
	var listOfMatches = [];
	var foundIndex = binarySearch(minIndex, maxIndex, myList);
	if (foundIndex != -1){
		listOfMatches.push(foundIndex);
		/* We found a match, check for other matches
		(e.g. other people with the same last name) */
		var searchIndex = foundIndex+1;
		while (myList[searchIndex] === searchTerm){
			listOfMatches.push(searchIndex);
			searchIndex++;
		}
		searchIndex = foundIndex-1;
		while (myList[searchIndex] === searchTerm){
			listOfMatches.push(searchIndex);
			searchIndex--;
		}
	} else if (foundIndex === -1) {
		return -1;
	}
	return listOfMatches;
}

function makeListOfResults(firstName, lastName, andrewID, sortedFirstNames, sortedLastNames, sortedAndrewIDs){
	var matches = [];
	if (andrewID != null && sortedAndrewIDs != null) {
		matches = getListOfMatches(andrewID, sortedAndrewIDs);
	}
	else if (lastName != null && firstName != null && sortedLastNames != null && sortedFirstNames != null) {
		var firstMatches = getListOfMatches(lastName, sortedLastNames);
		var matches = getListOfMatches(firstName, firstMatches);
	}
	else if (lastName != null && sortedLastNames != null) {
		matches = getListOfMatches(lastName, sortedLastNames);
	}
	else if (firstName != null && sortedFirstNames != null) {
		matches = getListOfMatches(firstName, sortedFirstNames);
	}
	else {
		matches = -1;
	}
	return matches;o
}

function myFunction(){
	console.log("Starting function from input...")
	firstName = null;
	lastName = null;
	andrewID = null;
	sortedLastNames = null;
	sortedAndrewIDs = null;
	sortedFirstNames = null;

	var firstName = document.getElementById("firstNameInput").value;
	var lastName = document.getElementById("lastNameInput").value;
	var andrewID = document.getElementById("andrewIDInput").value;

	console.log(firstName, lastName, andrewID);
	var results = makeListOfResults(firstName, lastName, andrewID, test_first_name_list, sortedLastNames, sortedAndrewIDs);

	console.log(results);
	console.log("...ending function from input");

}
