"""
Example script for PyCon Talk
This is a very simple context free grammar.
Each terminal node's vocabulary has been described as lists.

Here's the rules if you're interested:
S        -> interjection headline ellipses pics
headline -> rapper ellipses predicate
ellipses -> ellipsis|empty string

"""

from random import choice

interjections = ["OH SNAP!", "MTO WORLD EXCLUSIVE:", "BLING BLING!", "YIKES!", "BREAKING NEWS!", "TOO CUTE!"]

rappers = ["LIL WAYNE", "KENDRICK LAMAR", "KIRKO BANGZ", "RAPPER PROBLEM", "DRAKE", "KANYE WEST", \
               "NICKI MINAJ", "JIM JONES", "RICK ROSS", "LIL KIM", "IGGY AZALEA", "KIM KARDASHIAN"]

predicates = ["PUTS JUMPOFF ON BLAST ON TWITTER", "BUYS A NEW BUGATTI", "IN TROUBLE WITH THE IRS", "FOUND ON THE BEACH" ]

pics = ["(PICS INSIDE)","AND WE GOT PICS", "(PICS)", "YOU WON'T BELIEVE THE PICS!", "AND WE GOT A VIDEO!"]

ellipses = ["...", "!!!", "...", "", "", "" "", "", ""] # padded empty strings to reduce likelihood

def getHeadline():
    return " ".join( [choice(rappers), choice(ellipses), choice(predicates)] )

print choice(interjections), getHeadline(), choice(ellipses), choice(pics)
