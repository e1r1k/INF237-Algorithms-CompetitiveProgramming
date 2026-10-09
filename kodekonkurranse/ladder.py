import math as m
def main():
    a, b = map(float, input().split())
    print(m.ceil(a/m.sin(b*m.pi/180)))

main()