'''
import random
def num_choice():
    low_num=int(input("Enter a low number: "))
    high_num=int(input("Enter a high number: "))
    comp_num=random.randit(low_num,high_num)
    return comp_num
def guess():
    print("I am thinking of a number...")
    num_guess=int(input("What number am i thinking of?"))
    return num_guess
def correct(comp_num,num_guess):
   '''
   