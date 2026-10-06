def Simple_interest(P, R, T):
    return (P*R*T)/100

P = int(input("Enter principal: "))
R = int(input("Enter rate: "))
T = int(input("Enter time: "))

print("Simple Interest=", Simple_interest(P,R,T))