def Simple_interest(P, R, T):
    SI = (P * R * T) / 100
    return SI


if __name__ == "__main__":
    P = int(input("Enter principal amount: "))
    R = float(input("Enter rate of interest: "))
    T = float(input("Enter time: "))

    SI = Simple_interest(P, R, T)
    print("Simple Interest =", SI)