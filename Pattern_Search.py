import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

regex= "[^A-Za-z1-9]" #Reg Ex created to find necessary pattern. Square brackets and carrot combo used to mean "does not contain" followed by all letters (upper and lower) and numbers
for i in lorem_ipsum: #Loop through lorem_ipsum string
  results = re.findall(regex, lorem_ipsum) 
print(len(results)) #print amount of non-alphanum instances of pattern found

regex = "sit[-:]amet" #regular expression pattern defined
for i in lorem_ipsum: #for loop used to iterate through lorem ipsum string
  occurrences_sit_amet = re.findall(regex, lorem_ipsum) #all patterns found put into utility variable
print(len(occurrences_sit_amet)) #amount of times pattern found using len function

regex = "sit[-:]amet"
substitution = "sit amet" #substitution pattern defined
for i in lorem_ipsum: #for loop
  replace_results = re.sub(regex, substitution, lorem_ipsum) #results of replacing pattern with defined substitution put into replace_results utility variable
  occurrance_sit_amet = re.findall(substitution, replace_results) #
print(len(occurrance_sit_amet)) #print using len function to determine number of amount of occurances

regex = "sit[-:]amet"
substitution = "sit amet"
for i in lorem_ipsum:
  replace_results = re.sub(regex, substitution, lorem_ipsum)
  occurrance_sit_amet = re.findall(substitution, replace_results)
print(len(occurrance_sit_amet))
