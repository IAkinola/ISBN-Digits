# Hyperion Dev Application

## Section A: Code Review
### **Option 4: TypeScript Task**

Hello Student,

This is a really well written and documented solution, 
you showed a great understanding of the task and put a lot of effort into it.
The logic works great but I have a few notes.

1. I would like some of your comments to be more descriptive of what you are doing?

2. For the most part your logic works there are just a few errors with when you definied
   a function and variables.<br>
	 On line 5, you initailized a function using __const__, this is used to define variables. Like your very first declaration on line 1, a better way to do this is:<br>
           type caesar_cipher_function = (encodedText: string, shift: number) => string<br>
	We describe the function with a "function type expression". And then we change the parameters
			1. __string__ should be something else to not confuse the compiler
			2. __shift__ should be an integer since we are using it for calculations later
	Finally we reference a copy of the variable and function we made in line 1 and 2 to use in our
	solution. Like so:
	
          type Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
          type caesar_cipher_function = (encodedText: string, shift: number) => string

          // Function: Caesar Cipher
          const caesar_cipher:caesar_cipher_function = (encodedText: string, shift: number): string => {
            // Alphabet
            const alphabet: Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
          }

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
