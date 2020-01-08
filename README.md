# Invite customers within 100km of our office for some food and drinks on INTERCOM. 

Problem statement: invite any customer within 100km of our Dublin office for some food and drinks on us. Write a program that will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending)

You must use the formula for calculating distance from the link : https://en.wikipedia.org/wiki/Great-circle_distance

The GPS coordinates for our Dublin office are 53.339428, -6.257664.

Customer list is customers.txt file that is found in the current directory

Pre-requisite:
git and python3 or 
git and docker

# Usage for python3.

commands to run the program:

`git clone https://github.com/Lionelkris/intrcom.git`
`python3 customers_in_range.py`

Testing:

`python3 -m unittest discover`

Output for the program is also checkedin under the file name Output.txt in this repository

# Usage for docker

If running via docker, use the below commands

`git clone https://github.com/Lionelkris/intrcom.git`
`docker build -t intercom-test .`
`docker run intercom-test`

Above comamnds will print the desired output to the terminal and also prints the result of the unittest.

The program is tested on Mac OSX and Ubuntu 18.04.
