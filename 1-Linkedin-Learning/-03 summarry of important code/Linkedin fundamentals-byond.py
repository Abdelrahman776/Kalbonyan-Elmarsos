#------------------------------------------------------------------------------------------------------

from pickle import TRUE


name=input("what is your name")
print("my name is  " ,name)
print(type(name))
age=13
print(type(age))
#------------------------------------------------------------------------------------------------------
#comment
#5/2 =205
#5//2=2
#5%3=2 mod
#------------------------------------------------------------------------------------------------------


a=input()
if a>2:
    print("more than 2")
elif a>0:
    print("more than zero")

else:
    print("less than zero") # there has to be identation by using tab =4 spaces

    #5==4   false
    #5!4    true

#------------------------------------------------------------------------------------------------------

    def dance(  ):
        print("Dancing , yeah")
    #dance()


    def withdraw(balance,amount ):   #parameters
        if balance>amount:
            return balance
    x=withdraw(100,80) # arguments

 #------------------------------------------------------------------------------------------------------
guests=["maria ", "Gordon","Bob"]   #[0 , 1 , 2] index of a list
print(guests[0])  #  maria

t= ["avocado", 15 ,True ]  # list can have different data types at the same list

tuple=[4 , 2 ,7] # tuple list: its items canot be changed


california_states={"bird":"bear",
                    "A":"a"
                    ,"B":"b"}      # Dictionary data type  store related information

print(california_states["bird"])   # bear

#------------------------------------------------------------------------------------------------------

for name in guests:
    print(name)

i=5
while i<100:
    i+=5

#------------------------------------------------------------------------------------------------------
# import testmodule   module is python file that has code  
# library group of code used  together
# framework group of code used  together in a certain way 


#------------------------------------------------------------------------------------------------------

infile = open("inin.txt","rt")
out = open("outp.txt","wt")
print("processing input ")
sums =0

for f in infile:
    sums+=int(f)
    print(f.rstrip() , file =out)
print("\nTotal:"+str(sums),file =out)
out.close()
print("pgtehtrgjtrjyr")
