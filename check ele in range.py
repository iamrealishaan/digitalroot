test_list = [1, 2, 3, 4, 5]
print("The original list is: " + str(test_list))
i, j = 3, 10
res = True
for ele in test_list:
    if ele < i or ele >= j:
        res = False
        break
print(str(res))
