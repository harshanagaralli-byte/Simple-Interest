import sys

def Simple_interest(P, R, T):
    return (P*R*T)/100

P = int(sys.argv[1])
R = int(sys.argv[2])
T = int(sys.argv[3])

print(sys.argv[0])

print("Simple Interest=", Simple_interest(P,R,T))