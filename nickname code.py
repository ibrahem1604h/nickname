names=input("Enter the names of attendees separated by commas: ").split(", ")
nickname_list=[]
for name in names:
  name_parts = name.split()
  print(name_parts)

  first_name=name_parts[0] 
  last_name=name_parts[1]

  first_char_one= first_name[0]
  first_char_two= last_name[0]
  
  nickname=first_char_one + "." + first_char_two

  nickname_list.append(nickname) 
  
print("the niknames are: ")
for i in nickname_list:
  print(i)
