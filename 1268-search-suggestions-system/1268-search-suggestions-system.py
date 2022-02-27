class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
#         products = sorted(products)
#         i = 1
#         output = []
        
#         while i <= len(searchWord):
#             temp = []
#             for j in range(len(products)):
#                 if i > len(products[j]):
#                     continue
#                 if searchWord[:i] in products[j]:
#                     temp.append(products[j])
#                     if len(temp) >= 3: break
#             output.append(temp)
#             i += 1
        
#         return output

        sol = []
        products.sort()
        for i in range(len(searchWord)):
            temp = []
            for p in products:
                if i >= len(p):
                    continue
                if p[i] == searchWord[i]:
                    temp.append(p)
                products = temp
            sol.append(temp[:3]) 
        return sol
                    