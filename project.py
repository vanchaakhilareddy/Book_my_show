a = 10
Booked_seats = 0
cost_of_ticket = 0
Total_Income = 0
Row = int(input('Enter number of Rows - \n'))
Seats = int(input('Enter number of seats in a Row - \n'))
Total_seats = Row*Seats
Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]

class chart:

    @staticmethod
    def chart_maker():
        seats_chart = {}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j+1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart
    @staticmethod
    def find_percentage():
        percentage = (Booked_seats/Total_seats)*100
        return percentage
    
class_call = chart
table_of_chart = class_call.chart_maker()

while a != 0:
    
    print('1 for Show the seats \n2 for Buy a Ticket \n3 for Statistics ',
          '\n4 for Show booked Tickets User Info \n0 for Exit')
    a = int(input('Select Option - '))
    print('Cinema:')
    if a == 1:
        if Seats < 10:
            for seat in range(Seats):
                print(seat, end='  ')
            print(Seats)
        else:
            for seat in range(10):
                print(seat, end='  ')
            for seat in range(10, Seats):
                print(seat, end=' ')
            print(Seats)
        if Seats < 10:
            for num in table_of_chart.keys():
                print(int(num)+1, end='  ')
                for no in table_of_chart[num].values():
                    print(no, end='  ')
                print()
        else:
            count_num = 0
            for num in table_of_chart.keys():
                if int(list(table_of_chart.keys())[count_num]) < 9:
                    print(int(num)+1, end='  ')
                else:
                    print(int(num)+1, end=' ')
                count_key = 0
                for no in table_of_chart[num].values():
                    if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
        print('Vacant Seats = ', Total_seats - Booked_seats)
        print()

    elif a == 2:
        Row_number = int(input('Enter Row Number - \n'))
        Column_number = int(input('Enter Column Number - \n'))
        if Row_number in range(1, Row+1) and Column_number in range(1, Seats+1):
            if table_of_chart[str(Row_number-1)][str(Column_number)] == 'S':
                if Row*Seats <= 60:
                    cost_of_ticket = 10
                elif Row_number <= int(Row/2):
                    cost_of_ticket = 10
                else:
                    cost_of_ticket = 8
                print('cost_of_ticket - ', '$', cost_of_ticket)
                confirm = input('yes for booking and no for Stop booking - ')
                person_details = {}
                if confirm == 'yes':
                    person_details['Name'] = input('Enter Name - ')
                    person_details['Gender'] = input('Enter Gender - ')
                    person_details['Age'] = input('Enter Age - ')
                    person_details['Phone_No'] = input('Enter Phone number - ')
                    person_details['Ticket_prize'] = cost_of_ticket
                    table_of_chart[str(Row_number-1)][str(Column_number)] = 'B'
                    Booked_seats += 1
                    Total_Income = Total_seats * cost_of_ticket
                else:
                    continue
                Booked_ticket_Person[Row_number-1][Column_number-1] = person_details
                print('Booked Successfully')
            else:
                print('This seat already booked by some one')
        else:
            print()
            print('***  Invalid Input  ***')
        print()

    elif a == 3:
        print('Number of purchased Ticket - ', Booked_seats)
        print('Percentage - ', class_call.find_percentage())
        print('Current  Income - ', '$', cost_of_ticket)
        print('Total Income - ', '$', Total_Income)
        print()

    elif a == 4:
        Enter_row = int(input('Enter Row number - \n'))
        Enter_column = int(input('Enter Column number - \n'))
        if Enter_row in range(1, Row+1) and Enter_column in range(1, Seats+1):
            if table_of_chart[str(Enter_row-1)][str(Enter_column)] == 'B':
                person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
                print('Name - ', person['Name'])
                print('Gender - ', person['Gender'])
                print('Age - ', person['Age'])
                print('Phone number - ', person['Phone_No'])
                print('Ticket Prize - ', '$', person['Ticket_prize'])
            else:
                print()
                print('---**---  Vacant seats  ---**---')
    
        else:
            print()
            print('***  Invalid Input  ***')
        print()
    elif a == 0:
        print( "Thank You for visiting here" )
        exit()

    else:
        print()
        print('***  Invalid Input  ***')
        print()