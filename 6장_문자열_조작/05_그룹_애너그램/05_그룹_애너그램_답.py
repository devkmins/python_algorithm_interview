def anagram(arr):
    ans = {}
    arr.sort()
    
    for i in range(len(arr)):
        if i == 0:
            ans["".join(sorted(arr[i]))] = [arr[i]]
        else:
            if "".join(sorted(arr[i])) in ans:
                ans["".join(sorted(arr[i]))].append(arr[i])
            else:
                ans["".join(sorted(arr[i]))] = [arr[i]]
                
    return list(ans.values())
            
    
        
print(anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))