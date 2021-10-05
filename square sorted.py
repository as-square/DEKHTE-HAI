# given an array sort the array based on squares

a=[-10,-3.-2,1,11,100]
ans=[]
left=0
right=len(a)-1
while(left<=right):
  if(abs(left)>abs(right)):
    left+=1
    ans.append(a[left]*a[left])
  else:
    right+=1
    ans.append(a[right]*a[right])
    
