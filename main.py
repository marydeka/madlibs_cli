from madlib import Madlib
import json
from jinja2 import Template



def main():
  state = "initial"
  madlib = None
  story = None

  while True:
    print("Current Menu:\n")
    if state == "initial":
      print("LM: Load Madlib")
      print("CNM: Create New Madlib")
    elif state == "loaded":
      print("POS: Print Original Story")
      print("PM: Play Madlib")
      print("CM: Close Madlib")
    elif state == "played":
      print("POS: Print Original Story")
      print("PYS: Print Your Story")
      print("SS: Save Story")
      print("CM: Close Madlib")
      print("PST: Print Story Titles")
      print("GNS: Get Number of Stories")
      print("PSS: Print a Saved Story")
    print("EX: Exit Program")
    print("\n=================================")

    command = input("Enter a command: ").upper()

    if command == "LM":
      print("Filenames (madlib titles) to choose from are: ")
      Madlib.printMadlibTitles()
      filename = input("Enter a filename: ")
      try: 
        madlib = Madlib(str(filename))
        state = "loaded"
        print("You have loaded the madlib: " + str(filename))
        print("\n")
      except:
          print("Not a valid filename. Returning to the main menu.")
          
    elif command == "CNM":
      Madlib.createMadlib()

    elif command == "POS":
      madlib.printOriginalStory()
      print("\n")

    elif command == "PM":
      story = madlib.play()
      state = "played"
      print("\n")

    elif command == "PYS":
      madlib.printStory(story)
      print("\n")

    elif command == "SS":
      storyName = input("Enter a name for your story:")
      madlib.saveStory(story, storyName)
      print("Story saved successfully\n")

    elif command == "PMT":
      print("Madlib titles (filenames to choose from) are: ")
      Madlib.printMadlibTitles()

    elif command == "PSS":
      print("The stories you can print are: ")
      madlib.printStoryNames()
      story = input("Enter the name of the story you want to see: ")
      madlib.printUserStory(story)

    elif command == "PST":
      madlib.printStoryNames()

    elif command == "GNS":
      madlib.printNumStories()

    elif command == "CM":
      madlib = None
      state = "initial"

    elif command == "EX":
      break
    else:
      print("Invalid command. Please try again.\n")

    

if __name__== "__main__":
  main()
  