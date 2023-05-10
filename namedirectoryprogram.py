# -*- coding: utf-8 -*-
#Namedirectory.ipynb#




def menu () :

 while True:

    print()
    print('''Name Directory

    Select a number for the action you want to be performed:

    1. View full directory
    2. Add name to directory
    3. Delete name from directory
    4. Search from name on directory
    5. Sort list in alphabetical order
    ''')
    selection = input("Make selection: ")
    # this is to make the starting interface so that the user will be able to perform any of the tasks.

    if selection == "1":
      display()

    elif selection == "2":
      adding()

    elif selection == "3":
      removing()

    elif selection == "4":
      searching()

    elif selection == "5":
      sorting() 

    else :
      print("Invalid selection") 
#this is the message incase a number selection is made that does not have an action assigned 

Name_Directory = ["John", "Larry", "David", "Craig", "George"]
#this is the inital list of names in the directory 

def display() :
  print()
  print("- - NAMES - -")
  for a in Name_Directory:
    print( a)
#loop that prints each item in the list


def adding():
  item = input("Enter name to add to the directory: ")
  Name_Directory.append(item)
  print(item + " has been add to directory")
#this will add items and display a confirmation message with the name inputed


def removing():
  item = input("Enter name you wish to delete from the directory: ")
  Name_Directory.remove(item)
  print(item + " has been removed from directory")
#this will remove items that are already on the directory and display the name thta has been removed as confirmation

def searching():
  item = input("search for name: ")
  if item in Name_Directory:
   print("this name is already in directory")
  else:
   print("This name not found, please add using action 2.")
#this searches the strings in the list for the same string and confirmed or denies if it is on the list already. with a prompt to add if not currently on list 

  
def sorting():
  Name_Directory.sort()
  print(Name_Directory)
#this sorts the directory list by alphabetical order



menu()
