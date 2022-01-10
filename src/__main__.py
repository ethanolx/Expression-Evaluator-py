#function to print menu
def menu():
    print("\n\nPlease select your choice ('1','2','3','4'):")
    print("\t1. Evaluate expression\n\t2. Sort expressions\n\t3. Exit")

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
        while user_choice != '3':
            menu()
            user_choice = input("Enter choice: ")

            #option 1
            if user_choice == '1':
                pass

            # option 2
            elif user_choice == '2':
                pass
        
            else:
                #option 4
                if user_choice == '3':
                    print("Bye, thanks for using ST1507 DSAA: Expression Evaluator and Sorter ")
                # if input is not 1 2 3 
                else:
                    print("-"*60)
                    print("\nError! Please enter a number from 1 to 3 and No alphabets!")
                    print("-"*60)


sorter = Sorter()

sorter.main_program()
