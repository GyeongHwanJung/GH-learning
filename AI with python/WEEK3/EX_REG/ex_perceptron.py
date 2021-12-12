# ---------------------------------------------------
# 퍼셉트론과 AND, NAND, OR, XOR  구현
# ---------------------------------------------------
def AND_gate(x1, x2):
    w1=0.5
    w2=0.5
    b=-0.7
    result = x1*w1 + x2*w2 + b
    if result <= 0:
        return 0
    else:
        return 1

def NAND_gate(x1, x2):
    w1=-0.5
    w2=-0.5
    b=0.7
    result = x1*w1 + x2*w2 + b
    if result <= 0:
        return 0
    else:
        return 1

def OR_gate(x1, x2):
    w1=0.6
    w2=0.6
    b=-0.5
    result = x1*w1 + x2*w2 + b
    if result <= 0:
        return 0
    else:
        return 1

def XOR_gate(x1, x2):
    s1 = NAND_gate(x1, x2)
    s2 = OR_gate(x1, x2)
    y = AND_gate(s1, s2)
    return y

# 기능 구현 ----------------------------------------------
print("\n-------AND--------")
for x1 in [0,1]:
    for x2 in [0, 1]:
        print(f"AND [{x1}, {x2}] = {AND_gate(x1, x2)}")

print("\n-------NAND--------")
for x1 in [0,1]:
    for x2 in [0, 1]:
        print(f"NAND [{x1}, {x2}] = {NAND_gate(x1, x2)}")

print("\n-------OR--------")
[print(f"OR [{x1},  {x2}] = {OR_gate(x1, x2)}") for x1 in [0,1] for x2 in [0, 1] ]

print("\n-------XOR--------")
[print(f"XOR [{x1}, {x2}] = {XOR_gate(x1, x2)}") for x1 in [0,1] for x2 in [0, 1] ]