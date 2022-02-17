class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        dict = {}
        output = []
        
        for domain in cpdomains:
            arr = domain.split(' ')
            addr = arr[1]
            while addr:
                if addr not in dict:
                    dict[addr] = 0
                dict[addr] += int(arr[0])
                addr = ".".join(addr.split('.')[1:])
            
        for key, value in dict.items():
            output.append(str(value) + " " + key)
        return output