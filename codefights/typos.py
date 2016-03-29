def num_typos(str, k, n=1):
    if str == "" or n > k: return 0
    
    num = 0
    for start in range(len(str) - 1):
        if str[start] != str[start+1]:
            num += 1 + num_typos(str[:start], k, n+1) + num_typos(str[start+1:], k, n+1)
            
    return num

def num_typos_for_domain(domain, k):
    sub_parts = domain.split(".")
    
    num = 0
    for sp in sub_parts:
        num += num_typos(sp, k)
        
    return num
    

def typosquatting(n, domain):
    if num_typos_for_domain(domain, 1000) <= n: return -1 #cheating
    if n == 0: return 0
    
    k = 0
    count = 1
    while count <= n:
        num = num_typos_for_domain(domain, count)
        if num <= n:
            k = count
        count += 1
    return k