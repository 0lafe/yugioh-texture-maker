# YuGiOh Infamy Card texture maker for payday 2

This is a python script for generating texture files for payday 2

# Use

Call `python main.py` to run the program

A complete zip file of the mod will be generated in the `/outputs` directory

# Arguments

There are a few arguments you can pass to the function to change what cards you get

The format for passing arguements is `key=value` with no spaces
If you want to pass a string with spaces the syntax is `key="value with spaces"`

Generally all [these fields are valid](https://db.ygoprodeck.com/api-guide/), and you can mix and match them together

If you supply an invalid query, the program should terminate and print the error sent back from the API. Generally this means you spelled something wrong, used contradictory inputs, or formatted the input incorrectly

# Examples

`python main.py format=goat` will download the whole set of cards from GOAT format

`python main.py startdate=1/1/2002 enddate=1/1/2009` will get all all cards from 2002-2009