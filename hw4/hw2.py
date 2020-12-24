test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_test_list =[test_list[n] for n in range(1,len(test_list)) if test_list[n-1] < test_list[n]]
# for n in range(1, len(test_list)):
#     if test_list[n-1]<test_list[n]:
#         new_test_list.append(test_list[n])
print(new_test_list)