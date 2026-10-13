import sys

def Simple_interest(P, R, T):
    SI = (P * R * T) / 100
    return SI


if __name__ == "__main__":
    P = int(sys.argv[1])
    R = float(sys.argv[2])
    T = float(sys.argv[3])

    SI = Simple_interest(P, R, T)
    print("Simple Interest =", SI)