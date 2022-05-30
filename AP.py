#Arithmetic progression
#print the first n terms of an AP
a=int(input("Enter the first term: "))
n=int(input("Enter the number of terms: "))
d=int(input("Enter the common difference: "))
for i in range(1,n+1):
    n_term=int(a+(i-1)*d)
print(n_term)

#print the sum of terms in AP
SumOfnTerms=(n_term/2)+(2*a+(i-1)*d)
print(SumOfnTerms)
