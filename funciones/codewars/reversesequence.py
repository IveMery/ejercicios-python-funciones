def reverse_seq(n):
    lista = []
    for i in range(n) :
        lista.append(n-i)
    return lista    
  
print(reverse_seq(10))    


#other solution
#def reverseseq(n):
#    return list(range(n, 0, -1))    