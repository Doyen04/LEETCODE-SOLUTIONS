nums = [1,2,3,3,4,2,5,6,7,7,6,5,9]

unique = list(set(nums))

intersect  = list(filter(lambda x : nums.count(x) > 1,unique))
unique.extend( intersect)
print(f"f = {len(unique)}", unique)
