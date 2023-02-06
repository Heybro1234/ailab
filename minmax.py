import math
def minmax(depth,nodeindex,maxplayer,values,targetdepth):
    if depth==targetdepth:
        return values[nodeindex]
        
    if maxplayer:
        return max(minmax(depth+1,nodeindex*2,False,values,targetdepth),minmax(depth+1,nodeindex*2+1,False,values,targetdepth))
        
    else:
        return min(minmax(depth+1,nodeindex*2,True,values,targetdepth),minmax(depth+1,nodeindex*2+1,True,values,targetdepth))
        
values=[3,5,2,9,12,5,23,23]
targetdepth=math.log(len(values),2)
print(minmax(0,0,True,values,targetdepth))
        
