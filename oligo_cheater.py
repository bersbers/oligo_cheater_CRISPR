#!/usr/bin/env python


#read in the sequence

sequence = raw_input("Enter your sequence: ")
print "your target sequence: "+ sequence

# remove PAM sequence

trim_seq = sequence[:-3]
print "trimmed sequence: "+ trim_seq

# add TA to 5' end

oligo1 = "TA" + trim_seq 
print "oligo 1: " + oligo1


# remove GG 

trim2 = trim_seq[2:]
print trim2

# reverse trim2

rev_trim2= trim2[::-1]
print rev_trim2 


#complement

DNA = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}

for i, j in DNA.iteritems():
      rev_compl = rev_trim2.replace(i, j)
print rev_compl   

# add AAAC to the 5' end

