import json
import os
from jinja2 import Template, Environment, meta
from colorama import Fore, Back, Style 


class Madlib:
  def __init__(self, filename):
    '''Loads the madlib with entered title and sets the key value pairs.'''
    self.filename = './madlibs/' +filename + ".json"
    with open( self.filename) as f:
      data = json.load(f)
      # print(data)
      self.template = data["template"]
      self.jinjaTemplate = Template(self.template)
      self.originalStory = data["originalStory"]
      self.prompts = data["prompts"]
      self.stories = data["stories"]

  def printOriginalStory(self):
    '''Prints the original story in green.'''
    print(Fore.GREEN + self.jinjaTemplate.render(self.originalStory))
    print(Style.RESET_ALL) 

  def play(self):
    '''Prompt user for each blanked out word in the madlib.'''
    userStory = {}
    #Loop through each key stored in the prompts dictionary
    #and add that key as the key in the dictionary userStory
    #and add the value stored at that key into the dictionary userStory
    for key in self.prompts:
      response = input("Enter " + self.prompts[key] + ": ")
      if response.upper() == "EX":
        break
      userStory[key] = response
    #print(self.jinjaTemplate.render(userStory))
    return userStory

  def printStory(self, story):
    '''Print the story (in yellow) to the terminal'''
    print(Fore.YELLOW + self.jinjaTemplate.render(story))
    print(Style.RESET_ALL) 

  def saveStory(self, story, storyName):
    '''Set the story name as the key, and the story as the value, and save.'''
    self.stories[storyName] = story
    self._saveToFile()

  def _saveToFile(self):
    '''Save the template, original story, prompts, and user stories in JSON format.'''
    with open(self.filename, 'w') as f:
      data = {
        "template": self.template,
        "originalStory": self.originalStory,
        "prompts": self.prompts,
        "stories": self.stories
      }
      json.dump(data, f, indent=4)

  def printNumStories(self):
    '''Print the number of stories for that particular madlib.'''
    print(len(self.stories.keys()))

  def printStoryNames(self):
    '''Print the names of each story for that particular madlib.'''
    storyNames = self.stories.keys()
    for key in storyNames:
      print(key)

  def printUserStory(self, storyName): 
    '''Print the user created story in yellow.''' 
    print(Fore.YELLOW + self.jinjaTemplate.render(self.stories[storyName])) 
    print(Style.RESET_ALL)      
    

  @classmethod
  def createMadlib(cls):
    '''Prompt user to enter a a madlib template.'''
    template = input("\nType your story with double curly braces around each variable name (e.g. {{Name}} is going to {{country}}.) \
      \n\nDo not include spaces in your variable names.\nDo not hit enter until your story is complete.\n \
      \nEach variable name must be unique (e.g. name1, name2, verb1, verb2)\n\n")
    env = Environment()
    ast = env.parse(template)
    variables = list(meta.find_undeclared_variables(ast))
    print(variables)
    print()

    #Prompt user to enter the value that each blank has in the original story.
    originalStory = {}
    for var in variables:
      value = input("What is the value of {{" + var + "}} in your original story?")
      originalStory[var] = value
    print(originalStory)
    print()

    #Prompt user to enter the type of variable (e.g. noun, verb, type of food, etc.) 
    #that matches with each blank in the madlib. These will be used as the prompts.
    prompts = {}
    for var in variables:
      prompt = input("What is the description of {{" + var + "}} (e.g. a noun, your best friend's name)?")
      prompts[var] = prompt
    print(prompts)
    print()

    #The user created madlib will be stored in a JSON format.
    madlib = {"template": template,
              "originalStory": originalStory,
              "prompts": prompts,
              "stories": {}
    }

    #Prompt the user for a title for the madlib; this will be used as the key to find it.
    madlibName = input("What do you want to name this madlib?")
    filename = './madlibs/' + madlibName + ".json"

    with open(filename, 'w') as f:
      json.dump(madlib, f, indent=4)

    print("madlib saved successfully")



  @classmethod
  def printMadlibTitles(cls):
    '''This will print all titles of existing madlibs.'''
    filenames = os.listdir('./madlibs')
    filenames = [f[:-5] for f in filenames if ".json" in f]
    for f in filenames:
      print(" - " + f)






  
