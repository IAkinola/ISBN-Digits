# Hyperion Dev Application

## Section A: Code Review
### **Option 4: TypeScript Task**

Hello Student,

This is a really well written and documented solution, 
you showed a great understanding of the task and put a lot of effort into it.
The logic works great but I have a few notes.

1. For the most part your logic works there are just a few errors with when you definied
   a function and variables.<br>
On line 5, you initailized a function using __const__, this is used to define variables. Like your very first declaration on line 1, a better way to do this is:<br>
       
       
       			type caesar_cipher_function = (text: string, shift: number) => string<br>
			
					
 We describe the function with a "function type expression". And then we change the parameters<br>
			<li> __string__ should be something else to not confuse the compiler</li><br>
			<li>__shift__ should be an integer since we are using it for calculations later</li><br>
			
Finally we reference a copy of the variable and function we made in line 1 and 2 to use in our
solution. Like so:
	
          type Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
          type caesar_cipher_function = (text: string, shift: number) => string

          // Function: Caesar Cipher
          const caesar_cipher:caesar_cipher_function = (text: string, shift: number): string => {
            const alphabet: Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
          }
2. Your code is very effective and well thought out, I would like to recommend a way to make it look a little 
   cleaner while still using the logic you came up with. Starting from __while__ <br>
   
   
   
		while (i < encodedText.length) {
			// Append To String Valid Alphabet Characters
			if (alphabet.indexOf(encodedText[i]) == -1) {
				// Append To String
				text+= encodedText[i];
			}
			// Special Characters

			// Find Alphabet Index
			const alphabetIndex: number = alphabet.indexOf((encodedText[i]).toUpperCase());

			// Alphabet Index Is In Alphabet Range
			if (alphabet[alphabetIndex + shift]) {
				// Append To String
				text += alphabet[alphabetIndex + shift];        
			}
			// Alphabet Index Out Of Range (Adjust Alphabet By 26 Characters)
			else {
				// Append To String
				text += alphabet[alphabetIndex + shift - 26];
			}

		 	// Increase I
		 	i++;
		 }
		 return text;
	       	 };
 

But overrall, well done and I will like to see more of your work.

## Section B: Projects
https://github.com/IAkinola/Steam-Market-Web-Scrapper <br>
https://github.com/IAkinola/dice-app-flutter

## Section C: International Standard Book Numbers
A package used to check if the digits given is a valid ISBN digit. If it's a ISBN-10 digit it gets converted to a ISBN-13 digit.
### How to use 
_To Install the package:_ <br>

Although pip works on most OS, alternative package managers include apt, yum or dnf for Linux and Homebrew or MacPorts for macOS 

**pip install wheel<br>**
**python setup.py bdist_wheel<br>**
**python setup.py sdist<br>**
**Run main.py for main package and test_isbn.py for test case<br>**

## Section D: Loom Video Submission
