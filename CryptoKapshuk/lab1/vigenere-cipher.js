//'use strict'

function doCrypt (isDecrypt) {
	var keyStr = document.querySelector("#key").value;
	//console.log(keyStr)

	if (keyStr.length == 0) {
		alert("Please fill out field Key");
		return;
	}

	var keyArray = filterKey(keyStr);
	console.log(keyArray)
	if (keyArray.length == 0) {
		alert("Key has no letters");
		return;
	}

	if (isDecrypt) {
		for (var i = 0; i < keyArray.length; i++)
			keyArray[i] = (26 - keyArray[i]) % 26;
	}

	var textElem = document.getElementById("text");
	var result = crypt(textElem.value, keyArray)
	document.getElementById("output").value = result;
};

function crypt (input, key) {
	var output = "";
	for (var i = 0, j = 0; i < input.length; i++) {
		var c = input.charCodeAt(i);
		if (isUppercase(c)) {
			output += String.fromCharCode((c - 65 + key[j % key.length]) % 26 + 65);
			//console.log(((c - 65 + key[j % key.length]) % 26 + 65));
			j++;
		} else if (isLowercase(c)) {
			output += String.fromCharCode((c - 97 + key[j % key.length]) % 26 + 97);
			j++;
		} else {
			output += input.charAt(i);
		}
	}
	return output;
}

function filterKey (key) {
	var result = [];
	for (var i = 0; i < key.length; i++) {
		var c = key.charCodeAt(i);
		if (isLetter(c))
			result.push((c - 65) % 32);
	}
	return result;
}

function isLetter(c) {
	return isUppercase(c) || isLowercase(c);
}

function isUppercase(c) {
	return 65 <= c && c <= 90;
}

function isLowercase(c) {
	return 97 <= c && c <= 122;
}

var encrypt = document.querySelector('#encrypt')
var decrypt = document.querySelector('#decrypt')

encrypt.addEventListener('click', () => doCrypt(false))
decrypt.addEventListener('click', () => doCrypt(true))