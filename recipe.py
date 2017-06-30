import random

ingredientsDict = {'Steak Dinner': 'Potatoes,Broccoli,Steak',
               'Chicken Salad': 'Chicken,Mayonnaise,Grapes',
               'Turkey Sub': 'Turkey Slices,Rolls,Lettuce',
               'Greek Salad': 'Lettuce,Olives,Peppers,Cheese,Dressing',
               'Brownies': 'Batter,Flour,Water,Eggs',
               'Beef Stew': 'Broth,Carrots,Potatos,Beef,Salt'
              }
recipeDict = {'Steak Dinner': 'Mash Potatoes, Cook Broccoli, Grill steak',
              'Chicken Salad':'Shred Grilled Chicken, Add Mayo, Mix, Add chopped Grapes',
              'Turkey Sub': 'Cut bread roll in half, add slice turkey in center',
              'Greek Salad': 'Shred lettuce, throw olives, pepper, cheese, dressing and lettuce into bowl',
              'Brownies' : 'Mix it all into bowl',
              'Beef Stew' : 'Chop vegetable and slice the beef, throw into pot hard. Then simmer until done'
              }


def getRecipe():
    return random.choice(list(ingredientsDict.items()))

def printRecipe():
    i,j = getRecipe()
    if i not in recipeDict.keys():
        return print('You have no instructions to make',i ,'\n')
    # if instructions do not exist returns from fn
    k = recipeDict.get(i)  # gets the value at key i of second dict for instructions

    print('Recipe of the week: ',i, '\n')
    print ('Ingredients: ',j, '\n')
    print('Instructions: ',k, '\n')  #bold text

# executable code
printRecipe()
print('Enter q to quit, any other input to generate new recipe\n')
quit = input() #no do while loops in python?

while quit is not 'q': # q to quit, any other input generates new recipe
    printRecipe()
    print('Enter q to quit, any other input to generate new recipe\n')
    quit = input()
sys.quit()






