def odd_character(s , my_string):
        if s == my_string:
            return 0
        else:     
            count = 0   
            for i in range(len(my_string)):
                
                if s[i] == my_string[i]:
                    count += 0
                else:
                    count += 1
            return count
n = int(input())
for i in range(n):
    s = input()
    my_string = 'codeforces'
    print(odd_character(s , my_string))

                