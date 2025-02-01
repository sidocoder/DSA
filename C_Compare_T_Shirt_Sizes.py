
t = int(input())
for _ in range(t):
    def compare_sizes(a: str, b: str) -> str:
        if a == b:
            return "="
    
    def get_type(size: str):
        if size[-1] == 'M':
            return ('M', 0)
        x_count = size.count('X')
        return (size[-1], x_count)
    
    type_a, x_count_a = get_type(a)
    type_b, x_count_b = get_type(b)
    
    if type_a != type_b:
        print('=')
   

    a, b = input().split()
    print(compare_sizes(a, b))

 
    