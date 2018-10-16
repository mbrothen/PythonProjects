#! python3
# extracts phone and email addresses from text in clipboard and outputs them to the clipboard and print command
# Skils: pyperclip, regular expressions

import pyperclip, re
text = str(pyperclip.paste()) #grab clipboard text
matches = []
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))? #optional areacode, 3 digits w/w/0 parenthesis
	(\s|-|\.)? 	#optional seperator space - or .
	(\d{3}) 		#first three numbers
	(\s|-|\.) 	#optional seperator
	(\d{4})     	#final 4 numebrs
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	#extension
	)''', re.VERBOSE)

emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+ 	#username, only vaide characters
	@ 					#@ symbol
	[a-zA-Z0-9.-]+ 		#url address
	(\.[a-zA-Z]{2,4}) 	#tld, 2-4 char, allows country codes, restricts newer extensions
	)''', re.VERBOSE)

# us regex to seach copied text
for groups in phoneRegex.findall(text):
	# build phone numbers in any format. 
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	print(groups[0])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

# Copy Results to clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('\n'.join(matches))
	print('Copied to Clipboad:')
else:
	print('No phone numnbers or email addresses found')
