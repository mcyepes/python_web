import sys

def get_pairs(list_,n):
    sorted_list = sorted(list_)
    reversed_list =sorted(list_,reverse=True)
    valid_pairs = set()
    for a in sorted_list:
        for b in reversed_list:
            if a+b == n:
                if a<=b:
                    valid_pairs.add((a,b))
            elif a+b<n:
                break
    return valid_pairs

if __name__ == '__main__':
    list_ = [int(num) for num in sys.argv[1].split(',')]
    n = int(sys.argv[2])
    answ = get_pairs(list_, n)
    if len(answ)>0:
        print('Valid Pairs: ')
        print(answ)
    else:
        print('There are not valid pairs.')