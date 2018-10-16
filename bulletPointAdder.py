#! python3
# Adds bullet points to text in clipboard to be pasted into wikipedia

import pyperclip
text = pyperclip.paste()

#split lines, add astriks
lines = text.split('\n')
for i in range(len(lines)): 
	#loop all lines from copied text
	lines[i] = '* ' + lines[i] #add star to each string in list
text = '\n'.join(lines)
print("Modified text saved to clipboard")
pyperclip.copy(text)

