amountOfNumbers = int(input())
warehouse = []
for i in range(1, amountOfNumbers+1):
    a = int(input())
    warehouse.append(a)
Finally = []
a = 0
m = 0
while len(warehouse) > 0:
    for i in range(0, len(warehouse)):
        if warehouse[a] <= warehouse[i]:
            m = m+1
    if m == len(warehouse):
        Finally.append(warehouse.pop(a))
        a = 0
        m = 0
    else:
        a = a + 1
        m = 0
print(Finally)


