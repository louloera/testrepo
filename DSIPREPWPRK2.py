def rec_dig_sum(n):
    '''
    Returns the recursive digit sum of an integer.

    Parameter
    ---------
    n: int

    Returns
    -------
    rec_dig_sum: int
       the recursive digit sum of the input n
    '''
    number = str(n)
    sum=0
    for i in number:
        sum+=int(i)

    if sum <= 9:
        return sum
    else:
        return rec_dig_sum(sum)




def distr_of_rec_digit_sums(low=0, high=1500):
    dic= {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for i in range(low, high+1):
            dic[rec_dig_sum(i)]+=1
    return dic


print (distr_of_rec_digit_sums())