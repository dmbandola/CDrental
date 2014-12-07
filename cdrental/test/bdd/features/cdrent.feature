Feature: CD(s) is/are checked out by a customer
        When checking out a CD, the system makes sure the details are correct and it is recorded as rented.

        Given Customer "Chen" with ID 921
        And CD with ID CD1, title "XOXO," a rental period of 2 days, and is not currently rented:
        When The clerk check out the CD with ID CD1 to customer with ID 921 on 9/21/2012
        Then CD with ID CD1 is recorded as rented
        And rental is contract printed with customer ID 921, customer name "Chen," CD ID CD1,  CD title "XOXO," 
        And rental due on 9/23/2012
