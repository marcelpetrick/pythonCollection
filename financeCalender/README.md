# finance calender (calculator)

Test program to take certain types of recurring transactions and apply them to a forecast of your financial situation.

Output will represent the "current day", "current budget", "applied transactions" and "actual change".

Output can be processed with tools like LibreOffice or your favorite chart-maker.

## example input
allowed trigger-types are: "once", "yearly", "monthly", "daily"

entry1 = TransactionItem("consumed food", "daily", -5, "0001-01-01") # starting from today; every day 5 kuan loss<br>
entry2 = TransactionItem("salary", "monthly", +666, "0001-01-02") # test for the second of the month<br>
entry3 = TransactionItem("birthday", "yearly", +123, "0001-09-05")<br>
entry0 = TransactionItem("current state", "once", 1000, "2019-08-24")<br>

## example output
---------------------------------------<br>
0 : date= 2019-08-22 budget= -5 triggers= consumed food; change= -5<br>
1 : date= 2019-08-23 budget= -10 triggers= consumed food; change= -5<br>
2 : date= 2019-08-24 budget= 985 triggers= current state;consumed food; change= 995<br>
3 : date= 2019-08-25 budget= 980 triggers= consumed food; change= -5<br>
4 : date= 2019-08-26 budget= 975 triggers= consumed food; change= -5<br>
5 : date= 2019-08-27 budget= 970 triggers= consumed food; change= -5<br>
6 : date= 2019-08-28 budget= 965 triggers= consumed food; change= -5<br>
7 : date= 2019-08-29 budget= 960 triggers= consumed food; change= -5<br>
8 : date= 2019-08-30 budget= 955 triggers= consumed food; change= -5<br>
9 : date= 2019-08-31 budget= 950 triggers= consumed food; change= -5<br>
10 : date= 2019-09-01 budget= 945 triggers= consumed food; change= -5<br>
11 : date= 2019-09-02 budget= 1606 triggers= consumed food;salary; change= 661<br>
12 : date= 2019-09-03 budget= 1601 triggers= consumed food; change= -5<br>
13 : date= 2019-09-04 budget= 1596 triggers= consumed food; change= -5<br>
14 : date= 2019-09-05 budget= 1714 triggers= consumed food;birthday; change= 118<br>
15 : date= 2019-09-06 budget= 1709 triggers= consumed food; change= -5<br>
16 : date= 2019-09-07 budget= 1704 triggers= consumed food; change= -5<br>
17 : date= 2019-09-08 budget= 1699 triggers= consumed food; change= -5<br>
18 : date= 2019-09-09 budget= 1694 triggers= consumed food; change= -5<br>
19 : date= 2019-09-10 budget= 1689 triggers= consumed food; change= -5<br>
<br>
Process finished with exit code 0<br>

## to be done

* write some functionality to read from text-file<br>
* write unit-tests
* remove the initial testing for calender- and datetime-code
* done: also print the daily change of the budget<br>
