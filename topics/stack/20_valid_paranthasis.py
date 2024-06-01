class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketsSet = [('(', ')'), ('[', ']'), ('{', '}')]
        for currentbracket in s:
            if currentbracket in ['(','{','[']:
            # if currentbracket in [x[0] for x in bracketsSet]:
                stack.append(currentbracket)
            else:
                if stack == []:
                    return False
                
                openBracket = stack.pop()
                for b in bracketsSet:
                    if b[0] != openBracket:
                        continue
                    #end if
                    if currentbracket != b[1]:
                        return False
                    #end if
                #end for
            #end if
        #end for
        return True if stack == [] else False


if __name__ == "__main__":
    myObject = Solution
    s = "()"
    print(myObject.isValid(myObject, s))
    s = "()[]{}"
    print(myObject.isValid(myObject, s))
    s = "(]"
    print(myObject.isValid(myObject, s))
    s = "([{{}()}()])"
    print(myObject.isValid(myObject, s))