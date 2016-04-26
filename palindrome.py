def palindrome(str):
    l=len(str)
    k=l;
    str1=str[l::-1]
    print str1
    if str1==str:
        print "palindrome"
    else:
        print " not palindrome"

palindrome("ayesha")
