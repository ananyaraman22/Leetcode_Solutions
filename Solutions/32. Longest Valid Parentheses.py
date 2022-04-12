# Here is the PYTHON solution:

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        i_stack=[]
        longestL=0
        i_stack.append(-1)
        if(len(s)<=1):     #if string is empty or having single character
            return 0
        for i in range(len(s)):
            if(s[i]=='('):          #if we encounter ( in string then simply append it's index in i_stack
                i_stack.append(i)
            else:
                i_stack.pop()        # else means that we must have encountered a ) bracket so simply pop index from i_stack
                if(len(i_stack)==0):    #now if len(i_index)==0 then simply append the current index
                    i_stack.append(i)
                else:
                    longestL=max(longestL,i-i_stack[-1])           #else if after popping after encountering a ) bracket if the i_stack has not 
                                                                   #become empty then simply find the length 
        return longestL
