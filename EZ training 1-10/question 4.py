'''Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8
PM and will run until midnight (12 AM) i.e., for 4 hours. He also needs to travel to the
party venue within this time which takes him P minutes. The contest comprises
of N problems that are arranged in order of difficulty, with problem 1 being the
simplest and problem N being the most difficult. Max is aware that he will require 5*i
minutes to solve the ith problem.
Your task is help Max find and return an integer value, representing the number of
problems Max can solve and reach the party venue within the given time frame of 4
hours.
Note: Max will leave his home at exactly 8 PM to reach the party venue.
Input Format:
input1: An integer value N, representing the total number of problems.
input2: An integer value P, Representing the time to travel in minutes from his home
to the party venue.'''

'''  60 min
5*i
1st ques==>581=5==>'''
N=int(input())
P=int(input())
problem_solved=0
time_period=240-P
for i in range (1,N+1):
    if(time_period>0 and time_period>5*i):
        time_period-=5*i
        problem_solved=problem_solved+1
print(problem_solved)
