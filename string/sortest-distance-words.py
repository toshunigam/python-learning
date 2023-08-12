S = [ "my", "name", "is", "bali", "sun", "jara", "man", "manchali" ]
word1 = "my"; word2 = "man"
d1=-1
d2=-1
ans=100000
for i in range(len(S)):
    if (S[i] == word1):
        d1=i
    if (S[i] == word2):
        d2=i
    if (d1 !=-1 and d2 != -1):
        ans=min(ans, abs(d1-d2))
print(ans)