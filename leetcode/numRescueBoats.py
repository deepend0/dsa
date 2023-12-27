from typing import List
from math import ceil

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        
        boats = []
        
        len_peop = len(people)
        remaining = len_peop
        #print("people", people)
        while remaining:
            #print("remaining", remaining)
            #print("boats", boats)
            new_boats = int(ceil(remaining/2))
            for i in range (new_boats):
                boats.append(limit - people[len_peop - remaining])
                remaining -= 1
                      
            j = 0
            for i in range(remaining):
                while j < remaining:
                    if boats[-1 * (i+1)] >= people[len_peop - remaining + j]:
                        break
                    j += 1
                
                if j < remaining:
                    boats[-1 * (i+1)] -= people[len_peop - remaining + j]
                    del people[len_peop - remaining + j]
                    remaining -= 1
                    len_peop -= 1
                else:
                    break
                    
        return len(boats)
        
        
s = Solution()

class Solution {
    // TC : O(nlogn)
    // SC : O(1)
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int end = people.length-1;
        int start =0;
        int boatCount =0;
        while(end>=start){
            if(people[end]==limit){
                end--;
                boatCount++;
            } else if(people[end]+ people[start] <=limit){
                start++;
                end--;
                boatCount++;
            } else {
                end--;
                boatCount++;
            }
        }
        return boatCount; 
    }
}
print(s.numRescueBoats([1,2], 3))
print(s.numRescueBoats([3,2,2,1], 3))
print(s.numRescueBoats([3,5,3,4], 5))
print(s.numRescueBoats([7,6,4,4,4,3, 3, 1], 7))
