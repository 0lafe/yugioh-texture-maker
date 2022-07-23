# YuGiOh Infamy Card texture maker for payday 2

This is a python script for generating texture files for payday 2

# Use

Call `python main.py` to run the program

.texture files will appear in /outputs, and total card count will be printed in the console

# Arguments

There are a few arguments you can pass to the function to change what cards you get. You need 500 cards to make a full infamy deck

The format for passing arguements is `key=value` with no spaces
If you want to pass a string with spaces the syntax is `key="value with spaces"`

Generally all [these fields are valid](https://db.ygoprodeck.com/api-guide/) however there are some others I added

`rng` will pick a random set of cards from the returned list. Overriding any sorting you specify

# Example

`python main.py format=goat` will download 