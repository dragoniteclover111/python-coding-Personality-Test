print("Title of program: CCA Personality Test")
print()
print("Welcome! Please answer the following questions truthfully according to your own preferences and I will suggest a CCA which might be suitable for you based on your personality and your interests.")
print("Please answer the questions with numbers 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

Com1 = input("I enjoy coding and computing lessons.")
Bball1 = input("I love to stay active!")
Orchestra1 = input("I love to play musical instruments.")
Drama1 = input("I have fun when acting and performing in front of many people.")
Art1 = input("I enjoy drawing or doing art during my free time.")
Choir1 = input("I enjoy listening to music and singing")

Com2 = input("I'm good at coding and helping others solve computing problems.")
Bball2 = input("I love to play sports!")
Orchestra2 = input("I play at least one musical instrument well.")
Drama2 = input("I am not afarid of large crowds of people.")
Art2 = input("I like to be creative and can draw/paint etc very well.")
Choir2 = input("I can sing very well")

Com3 = input("I have a lot of experience and confidence in computing.")
Bball3 = input("I like to run a lot.")
Orchestra3 = input("I like to listen to classical music.")
Drama3 = input("I like to handle with props, music, lights etc backstage.")
Art3 = input("I can express myself through art.")
Choir3 = input("I confident to sing infront of crowds")

Com4 = input("I feel happy and relaxed doing computing.")
Bball4 = input("I enjoy being competitive and like to win.")
Orchestra4 = input("I feel calm and relaxed when I listen to an orchestra.")
Drama4 = input("I enjoy watching plays and dramas.")
Art4 = input("I admire drawing a lot and loved it.")
Choir4 = input("I can sing sensitively,paying attention to volume,and the style of music")

Com5 = input("I enjoy thinking about how to solve problems.")
Bball5 = input("I enjoy working in a team.")
Orchestra5 = input("I enjoy playing music for others.")
Drama5 = input("I enjoy being a part of a play.")
Art5 = input("I enjoy using colors.")
Choir5 = input ("I can tell what pitch I am using")

Com6 = input("I hope to join Infocomm Club.")
Bball6 = input("I hope to be in a Basketball team.")
Orchestra6 = input("I hope to be part of an Orchestra.")
Drama6 = input("I hope to be in Drama Club.")
Art6 = input("I hope to express myself through art even more in Art Club.")
Choir6 = input ("I hope to be able to sing better in choir")


Com_final = int(Com1) + int(Com2) + int(Com3) + int(Com4) + int(Com5) + int(Com6)
Bball_final = int(Bball1) + int(Bball2) + int(Bball3) + int(Bball4) + int(Bball5) + int(Bball6)
Orchestra_final = int(Orchestra1) + int(Orchestra2) + int(Orchestra3) + int(Orchestra4) + int(Orchestra5) + int(Orchestra6)
Drama_final = int(Drama1)+ int(Drama2)+ int(Drama3)+ int(Drama4)+ int(Drama5) + int(Drama6)
Art_final = int(Art1)+ int(Art2)+ int(Art3)+ int(Art4)+ int(Art5) + int(Art6)
Choir_final = int(Choir1)+ int(Choir2)+ int(Choir3)+ int(Choir4)+ int(Choir5) + int(Choir6)


print()

if Com_final > Bball_final and Com_final > Orchestra_final and Com_final > Drama_final and Com_final > Art_final and  Com_final > Choir_final:
  print("Based on your answers you have chosen, it's a high chance you are suitable for Infocomm club!")
if Bball_final > Com_final and Bball_final > Orchestra_final and Bball_final > Drama_final and Bball_final > Art_final and Bball_final > Choir_final:
  print("Based on your answers you have chosen, it's a high chance you are suitable for Basketball!")
if Orchestra_final > Bball_final and Orchestra_final > Com_final and Orchestra_final > Drama_final and Orchestra_final > Art_final and Orchestra_final > Choir_final:
  print("Based on your answers you have chosen, it's a high chance you are suitable for Chinese Orchestra!")
if Drama_final > Bball_final and Drama_final > Orchestra_final and Drama_final > Com_final and Drama_final > Art_final and Drama_final > Choir_final:
  print("Based on your answers you have chosen, it's a high chance you are suitable for Drama Society!")
if Art_final > Bball_final and Art_final > Orchestra_final and Art_final > Com_final and Art_final > Drama_final and Art_final > Choir_final:
  print("Based on your answers you have chosen, it's a high chance you are suitable for Art Club!")
 if Choir_final > Bball_final and Choir_final > Orchestra_final and Choir_final > Com_final and Choir_final > Drama_final and Choir_final > Art_final:
  print("Based on your answers you have chosen, it's a high chance you are suitable for choir!")
