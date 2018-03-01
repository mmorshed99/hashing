#Given a string, 
#find the length of the longest substring without repeating characters.
#
#Example:
#
#The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
#
#For "bbbbb" the longest substring is "b", with the length of 1
#
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        total = 0
        A_list = list(A)
        i = 0
        my_dict = {}
        curr_len = 0
        while(i < len(A_list)):
            try:
                location = my_dict[A_list[i]]
                #if curr_len > total:
                #    total = curr_len
                curr_len = 0
                i = location + 1
                my_dict = {}
            except:
                my_dict[A_list[i]] = i
                curr_len += 1
                if curr_len > total:
                    total = curr_len
                i += 1
        return total
