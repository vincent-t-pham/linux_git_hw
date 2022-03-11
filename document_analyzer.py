string = """A few months ago, I decided to deaccession an assortment of my things by 
whatever means feasible: selling, donating, recycling, giving them away, 
losing them on the subway, or reserving a spot for them on the next Mars 
Explorer. I gathered my unwanteds and piled them in the living room. A 
fraction of what was in that jumble: seven antique glass cake stands that 
belonged to my mother; a dormitoryâ€™s worth of new sheet sets and 
blankets for a bed size that is not mine; a set of Lenox china that my 
grandmother gave to my mother, who gave it to me, and was never used; 
clothes galore; a Viking stove grate that arrived cracked, and which I 
saved because I planned to weld it into a sculpture someday, after I 
learned how to weld; several rolls of Trump toilet paper that I wrongly 
thought were amusing a few years ago. I wish I could have added my 
boyfriendâ€™s too large Le Corbusier lounger. (There are Web sites, such 
as NeverLikedItAnyway.com, that will buy your exâ€™s leavings, ranging 
from engagement rings to â€œRick and Mortyâ€ socks.)"""

count = {}
words = string.split()

for word in words:
	if word in count:
		count[word] += 1
	else:
		count[word] = 1
		
i = 0
frequent_key = []
frequent_value = []
frequent_dict = {}

myList = []


for freq in sorted(count, key=count.get, reverse=True):
	if(i<5):
		frequent_key.append(freq)
		i+=1

for key in frequent_key: 
	frequent_value.append(count[key])
	
for key in frequent_key: 
	frequent_dict[key] = count[key]
	
l = []
for k, v in frequent_dict.items():
	l.append((k,v))
	
l = sorted(l, key=lambda e: (-e[1], e[0]))
print()
for e in l:
	print(f'{e[0]}: {e[1]}')





