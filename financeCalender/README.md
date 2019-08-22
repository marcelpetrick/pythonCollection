# finance calender (calculator)

Test program to take certain types of recurring transactions and apply them to a forecast of your financial situation.

Output will represent the "current day", "current budget", "applied transactions".

Output can be processed with tools like LibreOffice or your favorite chart-maker.

## example input
entry1 = TransactionItem("consumed food", "daily", -5, "0001-01-01") # starting from today; every day 5 kuan loss<br>
entry2 = TransactionItem("salary", "monthly", +666, "0001-01-02") # test for the second of the month<br>
entry3 = TransactionItem("birthday", "yearly", +123, "0001-09-05")<br>
entry0 = TransactionItem("current state", "once", 1000, "2019-08-24")<br>

## example output
---------------------------------------<br>
0 : date= 2019-08-22 cash= -5 triggers= consumed food;<br>
1 : date= 2019-08-23 cash= -10 triggers= consumed food;<br>
2 : date= 2019-08-24 cash= 985 triggers= current state;consumed food;<br>
3 : date= 2019-08-25 cash= 980 triggers= consumed food;<br>
4 : date= 2019-08-26 cash= 975 triggers= consumed food;<br>
5 : date= 2019-08-27 cash= 970 triggers= consumed food;<br>
6 : date= 2019-08-28 cash= 965 triggers= consumed food;<br>
7 : date= 2019-08-29 cash= 960 triggers= consumed food;<br>
8 : date= 2019-08-30 cash= 955 triggers= consumed food;<br>
9 : date= 2019-08-31 cash= 950 triggers= consumed food;<br>
10 : date= 2019-09-01 cash= 945 triggers= consumed food;<br>
11 : date= 2019-09-02 cash= 1606 triggers= consumed food;salary;<br>
12 : date= 2019-09-03 cash= 1601 triggers= consumed food;<br>
13 : date= 2019-09-04 cash= 1596 triggers= consumed food;<br>
14 : date= 2019-09-05 cash= 1714 triggers= consumed food;birthday;<br>
15 : date= 2019-09-06 cash= 1709 triggers= consumed food;<br>
16 : date= 2019-09-07 cash= 1704 triggers= consumed food;<br>
17 : date= 2019-09-08 cash= 1699 triggers= consumed food;<br>
18 : date= 2019-09-09 cash= 1694 triggers= consumed food;<br>
19 : date= 2019-09-10 cash= 1689 triggers= consumed food;<br>
<br>
Process finished with exit code 0<br>

## to be done

0. Write some functionality to read from text-file.
done: 1. also print the daily change of the budget
