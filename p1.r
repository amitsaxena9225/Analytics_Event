import re

text_to_search ='''

#abcdefghijklmnopqurtuvwxyz  \n
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
amitsaxena09.1992@gmail.com
amit*saxena@centurylink.com
amitsaxena25@outlook.com
amitsaxena9225@gmail.com
amit-saxena25@gmail.com

100.12.123.1
12.123.11.12.1
111.23.132.4
123/1121/34/1

25/09/1992
25-09-92
25.09.92
025/90/1992
25/sep/1992
25.sep.1992
'''
sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'[\w \d *.-]+@[\w .-]+')
#pattern = re.compile(r'\d{1,3}[./]\d{1,4}[./]\d{1,3}[./]\d{1}')
#pattern = re.compile(r'\d{2}[/]\w{3}[/]\d{4}')
matches = pattern.findall(text_to_search)
print (matches)
