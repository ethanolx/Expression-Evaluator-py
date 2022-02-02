'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
from sys import argv
from src import ParseTree, clear_console, load_config
from src.exceptions import InvalidExpressionError


# Global constants
DEFAULT_CONFIG_FILE = 'config.txt'
CONFIG_FILE = argv[1] if len(argv) > 1 else DEFAULT_CONFIG_FILE


# Prints the details of the authors of this program
def print_author_details():
    print("*"*48)
    print("* ST1507 DSAA: Expression Evaluator and Sorter *")
    print("*----------------------------------------------*")
    print("* Done By: Ethan (2012085) & Reshma (2011972)  *")
    print("* Class  : DAAA/2B/03                          *")
    print("*"*48)
    print()


# Prints the available options
def menu():
    print("Please select your choice [1 - 7]:\n"
          "1. Evaluate Fully Parenthesised Expression\n"
          "2. Evaluate Any Valid Expression\n"
          "3. Sort Expressions\n"
          "4. Fully Parenthesise an Expression\n"
          "5. Select Printing Mode\n"
          "6. Register a New Operator\n"
          "7. Exit")


# Entry point into the program
def main():
    # Loads configuration,
    #   otherwise falls back to default options
    try:
        depth_symbol, operator_mode = load_config(config_file=CONFIG_FILE, default_config=['.', 1])
        t = ParseTree(depth_symbol=depth_symbol[0], mode=int(operator_mode))
    except:
        t = ParseTree()

    # Infinite loop,
    #   until user exits the program
    user_choice = ''
    while user_choice != '7':
        try:
            # Refresh the display
            clear_console()
            print_author_details()
            menu()

            # Allow user to select option
            user_choice = input("Enter choice: ").strip()

            # Evaluate an expression (1 - fully parenthesised only / 2 - any valid expression)
            #   - Parse tree will be displayed
            #   - Followed by the result of the evaluation
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

            # Evaluate and sort expressions from a specified text file
            #   - The user can choose to save the results
            elif user_choice == '3':
                t.evaluate_and_sort()

            # Fully parenthesise a non-fully parenthesised valid expression
            elif user_choice == '4':
                expression = input('Enter an expression you want to fully parenthesise: \n')
                t.read(expression)
                print('Expression fully parenthesised:', t.reconstruct_expression())

            # Allows the user to change the mode of printing
            #   - h. horizontal (employs dfs)
            #       - a. in-order
            #       - b. pre-order
            #       - c. post-order
            #   - v. vertical (employs bfs)
            elif user_choice == '5':
                t.change_print_mode()

            # Allows the user to register a custom operator
            elif user_choice == '6':
                t.register_new_operator()

            # Exits/Quits and thus terminates the program
            elif user_choice == '7':
                print("Bye, thanks for using ST1507 DSAA: Expression Evaluator and Sorter :D")

        except FileNotFoundError as e:
            # Truncates the prefix '[Errno 2]'
            print(str(e)[10:])

        except ValueError:
            print('Invalid Expression')

        except Exception as e:
            print(str(e))

        finally:
            # Pauses program before display is refreshed
            input('\nPress Enter to continue...')


main()
