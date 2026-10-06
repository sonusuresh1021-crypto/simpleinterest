def simple_interest(principal,rate,time):
    si=(principal*rate*time)/100
    return si
if __name__ == "__main__":
    p=1000
    r=2
    t=2

    print("Simple interest:"(simple_interest(principal,rate,time)))