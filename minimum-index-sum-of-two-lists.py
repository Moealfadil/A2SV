class Solution:
    def findRestaurant(self, list1, list2):
        common_string=[]
        least_index=float("inf")
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    if i+j <least_index:
                        common_string.clear()
                        common_string.append(list1[i])
                        least_index=i+j
                    elif i+j == least_index:
                        common_string.append(list1[i])
        return common_string
        