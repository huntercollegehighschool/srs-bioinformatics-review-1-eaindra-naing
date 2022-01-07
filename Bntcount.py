"""
Define a function ntcount that takes a string representing a DNA string. 

-First the function should check if it is a valid DNA strand (use the function defined in the 1st part). If it's not, return "error".

-If it is a valid DNA strand, the function returns a dictionary with the counts of each nucleotide.

For example: 
ntcount("AACTGTA") 
returns {"A": 3, "C": 1, "G": 1, "T": 2}
"""

def ntcount(dna):
  for letter in dna:
    if letter != "A" and letter != "C" and letter != "G" and letter != "T":
      return "error"
  dnaseq = {}
  for letter in dna:
    dnaseq.setdefault (letter,0)
    dnaseq [letter] += 1
  return dnaseq
  print (ntcount(dna))



"""
elif part == "B":
  from Bntcount import ntcount
  for sequence in dna:
    print(sequence, "counts:", ntcount(sequence))
"""    