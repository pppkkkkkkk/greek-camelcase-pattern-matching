#User function Template for python3

class Solution:
    def camelCase(self,arr,pat):
        #code here
        
        def compare(word, pat):
            i=0 # for word
            j=0 # for pattern
            Let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            while i<len(word) and j <len(pat):
                if pat[j] == word[i]:
                    j+=1
                else:
                    if word[i] in Let:
                        return False
                i+=1
            if j == len(pat):
                return True
            return False
            
        result = []
        for word in arr:
            if compare(word,pat):
                result.append(word)
        
        return result
                
                    