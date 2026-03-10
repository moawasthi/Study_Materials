'''

Q1. Define a variable of all the labours and print the name of each labour.
Condition:-
    Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh
    labour variable should be something like this 1st_labour, 2nd_labour and so on.

Q2. Define a variable of all the labours daily wage and print the name and wage of each labour.
Condition:-
    Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh and wages are 500,400,400,300 respectively
    labour variable should be something like this 1st_labour_name,1st_labour_wage, 2nd_labour_name,
    2nd_labour_wage and so on.
    You are bound to use string formatting


Q3. I want to print this paragraph and its line number from which this paragraph is printing
    """ Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
    we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
    help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
    we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
            I have to print this paragraph as it is given here."""

    Condition:- 
    You can't use triple quote.
    Triple quote at starting is also a part of paragraph.

Q4. When do we get NameError?

Q5. Python is a high level language. What does that mean by high level?

Q6. What is compiled and Inetrpreted language, list a few?

Q7. Get all varibales address from RAM and you find if something is similar?
'''

# Q1
labour_1 = "Mahesh"
labour_2 = "Mithilesh"
labour_3 = "Ramesh"
labour_4 = "Sumesh"

print(f" labour 1 : {labour_1} \n labour 2 : {labour_2} \n labour 3 : {labour_3} \n labour 4 : {labour_4}")

labour_1 = "Mahesh"
labour_2 = "Mithilesh"
labour_3 = "Ramesh"
labour_4 = "Sumesh"
labour_1_wage = 500
labour_2_wage = 400
labour_3_wage = 400
labour_4_wage = 300

print(f" labour 1 : {labour_1} \n labour 2 : {labour_2} \n labour 3 : {labour_3} \n labour 4 : {labour_4}")

print(f" labour 1 : {labour_1} \t labour 1 wage : {labour_1_wage} \n labour 2 : {labour_2} \t labour 2 wage : {labour_2_wage} \n labour 3 : {labour_3} \t labour 3 wage : {labour_3_wage}\n labour 4 : {labour_4} \t labour 4 wage : {labour_4_wage}")


print(  """ Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that " \
"we are implemeting all the logics by ourself. The aim here is to build our \"4 BHK\" house with the\\"\\ 
    "help of 'Python programming'. We have total land is of \\100 ft * 100ft /, to colmplete the house" \ 
    "we have total 6 labours with 'different skill set like \"\\ building wall or building roof \\\\" \
            "I have to print this paragraph as it is given here.""")
