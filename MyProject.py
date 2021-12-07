print('hello world')

# Une fonction qui me retourne une tache bien formée
def createTask (description) :
    Task = [1, description, False]
    return Task

# affichage d'une tache bien formée sur une ligne
# n'affiche pas encore l'état todo/done
def printTask (Task) :
    print(Task[0] + '[ ]' + description)
    return 

printTask(createTask('voici une tache'))
