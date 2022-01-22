from src.parse_tree import ParseTree
from src.tree import PrintMode, TreeTraversalOrder
from src.utils.io_utils import clear_console, load_config

# function to print menu


def print_author_details():
    print("*"*47)
    print("* ST1507 DSAA: Expression Evaluator and Sorter*")
    print("*---------------------------------------------*")
    print("* Done By: Ethan (2012085) & Reshma (2011972) *")
    print("* Class  : DAAA/2B/03                         *")
    print("*"*47)
    print()

def menu():
    print("Please select your choice ('1','2','3','4'):\n"
          "1. Evaluate Expression\n"
          "2. Sort Expressions\n"
          "3. Fully Parenthesise an Expression\n"
          "4. Select Printing Mode\n"
          "5. Register a New Operator\n"
          "6. Exit")


def traversal_menu():
    print("\n\nPlease select how you want to traverse the Parse Tree ('a','b','c','d'):")
    print("\ta. Inorder (Left, Root, Right) \n\tb. Preorder (Root, Left, Right)\n\tc. Postorder (Left, Right, Root)\n\td. Go to Main Menu")


# main program
def main():
    depth_symbol, operator_mode = load_config(config_file='config.txt', default_config=['.', 1])
    t = ParseTree(depth_symbol=depth_symbol, mode=int(operator_mode))

    user_choice = ''
    while user_choice != '6':
        clear_console()
        print_author_details()
        menu()

        user_choice = input("Enter choice: ")

        # option 1
        if user_choice == '1':
            expression = input('Please enter the expression you want to evaluate:\n')
            t.read(expression)
            t.print_tree()
            print(f'Expression evaluates to:\n{t.evaluate()}')
            input('Press enter to continue...')

        # option 2
        elif user_choice == '2':
            pass

        elif user_choice == '3':
            expression = input('Enter an expression you want to fully parenthesise: \n')
            t.read(expression)
            print(t.reconstruct_expression())
            input('Press enter to continue...')

        elif user_choice == '4':
            new_print_mode = input('Enter new print mode (h/v): ')

            t.print_mode = new_print_mode

            traversal_menu()
            new_traversal_order = input('Enter new print mode (0/1/2): ')
            t.print_traversal_order = new_traversal_order

            # while traversal_mode != 'd':
            #     traversal_menu()
            #     traversal_mode = input("Select the traversal mode:")

                # if traversal_mode == 'a':  # Reverse Inorder
                #     expression = input('Please enter the expression you want to evaluate:\n')
                #     t = ParseTree(depth_symbol='.', mode=1)
                #     print("\n\nExpression Tree:")
                #     t.read(expression)
                #     t.print_tree()


                # elif traversal_mode == 'b':  # Preorder
                #     expression = input('Please enter the expression you want to evaluate:\n')
                #     t = ParseTree(depth_symbol='.', mode=1)
                #     print("\n\nExpression Tree:")
                #     t.read(expression)
                #     t.print_tree()
                #     print(f'Expression evaluates to:\n{t.evaluate()}')

                # elif traversal_mode == 'c':  # PostOrder
                #     pass

                # else:
                #     if traversal_mode == 'd':
                #         print("Switching to Main Menu...")
                #     else:
                #         print('\nError! Please enter alphabets a, b, c or d only!')

        elif user_choice == '5':
            t.register_new_operator()

        # option 4
        elif user_choice == '6':
            print("Bye, thanks for using ST1507 DSAA: Expression Evaluator and Sorter ")

        else:
            print("-"*60)
            print("\nError! Please enter a number from 1 to 3 and No alphabets!")
            print("-"*60)


if __name__ == '__main__':
    main()
