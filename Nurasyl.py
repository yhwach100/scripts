reccomend=input("Какой жанр музыки вы предпочитаете?(off чтобы отключить) ")
reccomend=reccomend.lower()
while reccomend!="off":
  if reccomend=="рок":
    print("Возможно вам понравится эти исполнители:")
    print("Linkin Park")
    print("Harry Styles") 
    print("Paramore")
  elif reccomend=="джаз":
    print("Возможно вам понравится эти исполнители:")
    print("Lui Armstrong")
    print("Miles Deivis")
    print("Billy Holiday")
  elif reccomend=="поп":
    print("Возможно вам понравится эти исполнители:")
    print("Ariana Grande")  
    print("Lady Gaga")  
    print("Michael Jackson")  
  elif reccomend=="хип хоп":
    print("Возможно вам понравится эти исполнители:")
    print("Drake")
    print("Kendrick Lamar")
    print("Post Malone")
  reccomend=input("Какой жанр музыки вы предпочитаете?(off чтобы отключить) ")
print("Досвидание!")