1. Random access machine (RAM)
   - in O(1) time
   - load O(1) words
   - O(1) computations
   - store O(1) words 
2. Pointer machine 
   - dynamic allocated obj
   - obj has O(1) fields (words int or pointer)

3. Python model 
   1. list is array 
   2. list.append(x): table doubling O(1) time 
   3. list.sort(): O(nlogn)

4. Comparison model:
   1. used for sorting when the only ADT is `>`, `<` and `==`
   2. compare takes at least `nlgn` time (lower bound)
   3. example: insersion sort, merge sort, heap sort

5. 