from src.parse_tree import ParseTree

#function to print menu
def menu():
    print("\n\nPlease select your choice ('1','2','3','4'):")
    print("\t1. Evaluate expression\n\t2. Sort expressions\n\t3. Fully Parenthesise an expression\n\t4. Exit")

def traversal_menu():
    print("\n\nPlease select your choice of traversing ('a','b','c','d'):")
    print("\ta. Inorder (Left, Root, Right) \n\tb. Preorder (Root, Left, Right)\n\tc. Postorder (Left, Right, Root)\n\td. Go to Main Menu")


#main program
class Sorter:
    def __init__(self):
        self.x = 'blank'

    def main_program(self):

        print("*"*47)
        print("* ST1507 DSAA: Expression Evaluator and Sorter*")
        print("*---------------------------------------------*")
        print("* Done By: Ethan (2012085) & Reshma (2011972) *")
        print("* Class  : DAAA/2B/03                         *")
        print("*"*47)

        user_choice = 0
        while user_choice != '4':
            menu()
            user_choice = input("Enter choice: ")

            #option 1
            if user_choice == '1':

                traversal_mode = 0
                while traversal_mode != 'd':
                    traversal_menu()
                    traversal_mode = input("Select the traversal mode:")

                    if traversal_mode == 'a': #Reverse Inorder
                        expression = input('Please enter the expression you want to evaluate:\n')
                        t = ParseTree(depth_symbol='.', mode=1)
                        print("\n\nExpression Tree:")
                        t.read(expression)
                        t.build()
                        print(str(t))
                        print(f'Expression evaluates to:\n{t.evaluate(True)}')

                    elif traversal_mode == 'b': #Preorder
                        pass

                    elif traversal_mode == 'c': #PostOrder
                        pass

                    else:
                        if traversal_mode == 'd':
                            print("Switching menu...")
                        else:
                            print('\nError! Please enter alphabets a, b, c or d only!')

            # option 2
            elif user_choice == '2':
                pass

            elif user_choice == '3':
                expression = input('Please enter an expression:\n')
                t = ParseTree(depth_symbol='.', mode=1)
                print(t.reconstruct_expression())
                
            else:
                #option 4
                if user_choice == '4':
                    print("Bye, thanks for using ST1507 DSAA: Expression Evaluator and Sorter ")
                
                else:
                    print("-"*60)
                    print("\nError! Please enter a number from 1 to 3 and No alphabets!")
                    print("-"*60)


sorter = Sorter()

sorter.main_program()
