customer=int(input("Enter the money you purchased: "))

_500_won=customer//500
customer -= _500_won*500
_100_won=customer//100
customer -= _100_won*100
_50_won=customer//50
customer -= _50_won*50
_10_won=customer//10
customer -= _10_won*10

print(_500_won,_100_won,_50_won,_10_won)



