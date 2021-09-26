   
  n = int(input())
    integer_list = tuple(map(int, input().split())) #maps the input into int types since input is auto string, stores in var
    
    print (hash(integer_list)) #computes hash
    
