def username_generator (first_name, last_name):
  username = 0
  if len(first_name) > 3 and len(last_name) > 4:
     username = first_name[:3]+last_name[:4]
     return username
  elif len(first_name) > 3 and len(last_name) <= 4:
    username = first_name[:3]+last_name
    return username
  elif len(first_name) <= 3 and len(last_name) > 4:
    username = first_name+last_name[:4]
    return username
  else:
     return  first_name+last_name

print(username_generator ("Mimiko", "Watanabe"))


def password_generator(user_name):
   return user_name[-1:] + user_name[:-1]

print(password_generator('MimWata'))