object and name is that obj lives in memory and each type,valuehave there identity
name is attaach to any obj

ass obj never copies reason is it attach name to one

mutuable = list,dict,set
inmutuable = int,float,bool,str,tuple,byte,none,frozenset

2 variable and refernces 
b =a does not copy the data , a and b is equal so its true 
mutable was done through b.append(4) and its visible through a

3 in place augementation and reassignment
mutuable list y +=[3] and both x,y reflect (1,2,3,) its true

4 the list multipication trap 0*2*2
multipy a list of mutuable obj duplicate refernces the line inner list not the itself list

output of question
hello
None
[1, 2, 3]
[1, 2, 3, 4] True
abc abcd
[1, 2, 3] True
[1, 2] False
[99, 2] [0, 1]
[[1, 2, 99], [3, 4]]
[[7, 0], [7, 0]]