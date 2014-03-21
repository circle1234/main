"""dasdas"""
import string                       
from urllib2 import urlopen         
def top_words(s):
    words = {}                                                             
    for line in s.readlines():          
        line = string.strip(line, " \n")    
        for word in line.split(" "): 
            try:                     
                words[word] += 1            
            except KeyError:                
                words[word] = 1             
 
            pairs = words.items()               
            pairs.sort(lambda a, b: b[1]-a[1])   
            for p in pairs[:10]:                
                print p[0], p[1]
web=raw_input("Enter a web address:")
u = urlopen(web)
top_words(u)
