# Restaurant Management processes

     Video Demo:  <https://youtu.be/v_lBkvcFi10>

     Overall Description:
        The project represents the restaurants managements processes in its most basic and simplifed version,
        these processes include reserve the table and assign the right tables to customers depending of the customer
        group number, then present the restaurant menu to the customer so they can choose thier favorite food,
        then take the orders from the customers, then get the check prepared to be presented then paid by the user,
        that check must include the ordered food prices list, the service, and the taxes,
        the service and the taxes depend on the type of the table, the number of the customer group, and total
        amount of money to be paid before applying them.

    Detailed Description:
        The project contains some essential files, the first of them named "project" it contains the main part
        of the project code and contain the main() trigger, and many function to deliver the desired solutin,
        as mentioned before the project is built as a number of code blocks, each block has its won task and
        functionality, these blocks represent the tasks to be performed.

        The first task is to make taple reservation, first print out the welcoming message to user "Welcome to
        La Dolce Vita restaurant ❤️❤️❤️❤️❤️❤️❤️" then prompt for the user asking how many persons are there
        to be in the reservation, the let the user chooses his suitable table depnding on the how many persons
        are there, there are mainly three types of tables "small", "regular", and "large",
        the small tables are to be assigned to maxmuim  two persons group, the regular tables are to be assigned
        to customers groups in range three to six persons, then if the customers group is seven persons or more
        the will be assigned a large table.

        After assigning the table, the time to present the menu and take the customers orders comes,
        in the project, the menu is presented as by a CSV file named "menu" which include all the avilable food
        and drinks accompanied by the price of each, so after taking the order, print out a styled table of
        the orders summary, the tabulate module is used to perform that task.

        The system then calculate the ckeck to be paid but before that the system add more 10% as mandatory taxes
        and the service cost which depend of the table type and the customer number as abovementioned,
        after adding the taxes and service, print out the totall amount to paid by the customer.

    Project Test:
        inculded in the project folder a file named "test_project", this file uses the pytest module to test
        the project performance and breaking points, by testing all possible scenarios it turned out that
        the project is performing as expcted, as known testing is a very important aspect of best practices.

    Notes:
    - the project can be further improved and that's what I'm going to do


