"""
Example script for PyCon Talk
This is a very simple context free grammar, using NLTK
"""

import nltk

headline_grammar = nltk.parse_cfg("""
S -> Int HL ELL PICS
Int -> "OH SNAP!" | "MTO WORLD EXCLUSIVE:" | "BLING BLING!" | "YIKES!" | "BREAKING NEWS!" | "TOO CUTE!"
HL -> Rapper Pred
Rapper -> "LIL WAYNE" | "KENDRICK LAMAR" | "KIRKO BANGZ" | "RAPPER PROBLEM" | "DRAKE" | "KANYE WEST" | "NICKI MINAJ" | "JIM JONES" | "RICK ROSS" | "LIL KIM" | "IGGY AZALEA" | "KIM KARDASHIAN"
Pred -> "PUTS JUMPOFF ON BLAST ON TWITTER" | "BUYS A NEW BUGATTI" | "IN TROUBLE WITH THE IRS" | "FOUND ON THE BEACH" 
ELL -> "..." | "!!!"
PICS -> "(PICS INSIDE)" | "AND WE GOT PICS" | "(PICS)" | "YOU WON'T BELIEVE THE PICS!" | "AND WE GOT A VIDEO!"
""")

