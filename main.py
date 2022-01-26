'''
   Class: DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''

from src import ParseTree, clear_console, load_config
from sys import argv

from src.exceptions import InvalidExpressionError

DEFAULT_CONFIG_FILE = 'config.txt'

CONFIG_FILE = argv[1] if len(argv) > 1 else DEFAULT_CONFIG_FILE

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
    print("Please select your choice [1 - 7]:\n"
          "1. Evaluate Fully Parenthesised Expression\n"
          "2. Evaluate Any Valid Expression\n"
          "3. Sort Expressions\n"
          "4. Fully Parenthesise an Expression\n"
          "5. Select Printing Mode\n"
          "6. Register a New Operator\n"
          "7. Exit")


# main program
def main():
    try:
        depth_symbol, operator_mode = load_config(config_file=CONFIG_FILE, default_config=['.', 1])
        t = ParseTree(depth_symbol=depth_symbol[0], mode=int(operator_mode))
    except:
        t = ParseTree()
        print('Invalid Configuration File >:(')
        input('Press Enter to continue...')

    user_choice = ''
    while user_choice != '7':
        try:
            clear_console()
            print_author_details()
            menu()

            user_choice = input("Enter choice: ")

            if user_choice in {'1', '2'}:
                expression = input('Please enter the expression you want to evaluate:\n')
                t.read(expression)
                t.build()
                if user_choice == '1' and not t.validate_fully_parenthesised():
                    raise InvalidExpressionError(f'Expression is not fully parenthesised. Did you mean \'{t.reconstruct_expression()}\'?')
                print('\nParse Tree')
                print('----------')
                t.print_tree()
                print(f'\nExpression evaluates to:')
                print(t.evaluate())

            elif user_choice == '3':
                t.evaluate_parsetree()

            elif user_choice == '4':
                expression = input('Enter an expression you want to fully parenthesise: \n')
                t.read(expression)
                print('Expression fully parenthesised:', t.reconstruct_expression())

            elif user_choice == '5':
                t.change_print_mode()

            elif user_choice == '6':
                t.register_new_operator()

            elif user_choice == '7':
                print("Bye, thanks for using ST1507 DSAA: Expression Evaluator and Sorter ")

        except FileNotFoundError as e:
            print(str(e)[10:])

        except ValueError:
            print('Invalid Expression')

        except Exception as e:
            print(str(e))

        finally:
            input('\nPress Enter to continue...')


main()
