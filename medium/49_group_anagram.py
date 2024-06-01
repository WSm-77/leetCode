class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        #########################
        #   helper functions    #
        #########################

        def listOfLetters(word: str) ->  list:
            my_list = [0 for _ in range(26)]

            for char in word:
                my_list[ord(char) - ord('a')] += 1
            
            return my_list
        
        #############################
        #   body of the function    #
        #############################

        groups = []
        result = []

        for word in strs:
            list_of_letters = listOfLetters(word)
            does_match_any_group = False
            for i in range(len(groups)):
                if list_of_letters == groups[i]:
                    does_match_any_group = True
                    result[i].append(word)
                    break
                    
            if not does_match_any_group:
                groups.append(list_of_letters)
                result.append([word])
        
        return result
                

                
if __name__ == "__main__":
    test = Solution()
    words = ["eat","tea","tan","ate","nat","bat"]
    print(test.groupAnagrams(words))