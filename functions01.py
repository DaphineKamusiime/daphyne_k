def add(a,b):
    print(a+b)
    return a+b
add(2,4)
def bio(name,work,age):
    name=print("My name is ",name) 
    work=print("I am an ",work)
    age=print("I am ",age)
    biography=(name,work,age)
    return biography 
def edu(school,address):
    school=print("I go to ",school)
    address=print("It is found in ",address)
    education=(school,address)
    return education
bio("Daphyne","Aviator","20 years old")
edu("UCU","Mukono\n")
bio('Joan','Accountant','20 years old')
edu('MUBS','Nakawa')

def numbers():
    num=int(input('Enter a number'))
    number=(num)
    return number
def num_count(num):
    n=1
    while n<=num:
        print(n)
        n=n+1
def main():
    num=numbers()
    num_count(num)
main()