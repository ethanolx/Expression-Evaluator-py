from src.parse_tree import ParseTree
from src.tree import PrintMode, TreeTraversalOrder
from src.utils.io_utils import clear_console, load_config

# function to print menu


def print_author_details():
    print("*"*48)
    print("* ST1507 DSAA: Expression Evaluator and Sorter *")
    print("*----------------------------------------------*")
    print("* Done By: Ethan (2012085) & Reshma (2011972)  *")
    print("* Class  : DAAA/2B/03                          *")
    print("*"*48)
    print()


def menu():
    print("Please select your choice [1/2/3/4/5/6]:\n"
          "1. Evaluate Expression\n"
          "2. Sort Expressions\n"
          "3. Fully Parenthesise an Expression\n"
          "4. Select Printing Mode\n"
          "5. Register a New Operator\n"
          "6. Exit")


# main program
def main():
    depth_symbol, operator_mode = load_config(config_file='config.txt', default_config=['.', 1])
    t = ParseTree(depth_symbol=depth_symbol, mode=int(operator_mode))

    user_choice = ''
    while user_choice != '6':
        try:
            clear_console()
            print_author_details()
            menu()

            user_choice = input("Enter choice: ")

            if user_choice == '1':
                expression = input('Please enter the expression you want to evaluate:\n')
                t.read(expression)
                t.print_tree()
                print(f'Expression evaluates to:\n{t.evaluate()}')

            elif user_choice == '2':
                pass

            elif user_choice == '3':
                expression = input('Enter an expression you want to fully parenthesise: \n')
                t.read(expression)
                print('Expression fully parenthesised:', t.reconstruct_expression())

            elif user_choice == '4':
                t.change_print_mode()

            elif user_choice == '5':
                t.register_new_operator()

            elif user_choice == '6':
                print("Bye, thanks for using ST1507 DSAA: Expression Evaluator and Sorter ")

        except Exception as e:
            print(str(e))

        finally:
            input('Press Enter to continue...')


if __name__ == '__main__':
    main()
