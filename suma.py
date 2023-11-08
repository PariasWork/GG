def suma(na,nb,nc,nd):
    if na+nb>1000:
        return na+nb
    elif na+nb<1000 and na+nb+nc>1000:
        return na+nb+nc
    else:
        return na+nb+nc+nd

result= suma(379,767,478,532)

print(result)