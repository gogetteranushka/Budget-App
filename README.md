# Budget-App

Complete the _Category_ class. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called _ledger_ that is a list.
The class should also contain the following methods:

➣A _deposit_ method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.

➣A _withdraw_ method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.

➣A _get_balance_ method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.

➣A _transfer_ method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.

A _check_funds_ method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.

When the budget object is printed it should display:

➣A title line of 30 characters where the name of the category is centered in a line of * characters.

➣A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.

➣A line displaying the category total.


Here is an example usage:


<img width="326" alt="image" src="https://github.com/gogetteranushka/Budget-App/assets/109903993/032a8feb-dba3-4fbb-9ed7-a2ebdac045ec">

And here is an example of the output:

<img width="281" alt="image" src="https://github.com/gogetteranushka/Budget-App/assets/109903993/348bb61d-5a66-4966-9f54-4679ca791314">

Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

<img width="187" alt="image" src="https://github.com/gogetteranushka/Budget-App/assets/109903993/eaada347-39af-4ebf-b86f-85f7abc44f11">



