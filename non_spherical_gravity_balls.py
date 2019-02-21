from vpython import *

R=0.02
N=10
m=1
G=6.67e-6

#g is the local attraction
g=1e-7
k=30
kv=1 #this is the velocity drag
kr=3*G*4*R**2 #this is the repulsive constant (1/r^4)
Fmax=100

theta=random()*pi
phi=random()*pi*2
rr=random()

#balls=[sphere(pos=vector(2*random()-1,2*random()-1,2*random()-1), radius=R)]
#balls=[sphere(pos=rr*vector(sin(theta)*cos(phi),sin(theta)*sin(phi),cos(theta)), radius=R)]
balls=[sphere(pos=vector(-((N/2)-1)*R+.5*R,0,0), radius=R)]
def overlap(b1,blist):
    #this function looks for ANY overlap
    for k in blist:
        r=b1-k.pos
        if mag(r)<2*R:
            return(True)
    return(False)

dx=2*R
bcount=1
#this just makes some random balls
#while bcount<N:
#    theta=random()*pi
#    phi=random()*pi*2
#    rr=random()
#    temp=rr*vector(sin(theta)*cos(phi),sin(theta)*sin(phi),cos(theta))
#    #temp=vector(2*random()-1,2*random()-1,2*random()-1)
#    if not overlap(temp,balls):
#        
#        balls=balls+[sphere(pos=temp, radius=R,make_trail=False)]
#        bcount=bcount+1
#    for i in balls:
#        i.p=vector(0,0,0)
#        i.m=m
tempx=vector(-((N/2)-1)*R+.5*R,0,0)

while bcount<N:
    tempx=tempx+vector(dx,0,0)
    balls=balls+[sphere(pos=tempx,radius=R)]
    bcount=bcount+1
    

bcount=1
tempx=vector(-((N/2)-1)*R+.5*R,R*2,0)
while bcount<N:
    tempx=tempx+vector(dx,0,0)
    balls=balls+[sphere(pos=tempx,radius=R)]
    bcount=bcount+1

bcount=1
tempx=vector(-((N/2)-1)*R+.5*R,0,R*2)
while bcount<N:
    tempx=tempx+vector(dx,0,0)
    balls=balls+[sphere(pos=tempx,radius=R)]
    bcount=bcount+1
    
for i in balls:
    i.m=m
    i.p=vector(0,0,0)

def gforce(bball, balllist):
    #this takes one ball and calculates the net gravitational force on it
    tempforce=vector(0,0,0)
    for i in balllist:
        
        rtemp=bball.pos-i.pos
        if mag(rtemp)>R:
            tempforce=tempforce-G*i.m*bball.m*norm(rtemp)/mag(rtemp)**2-g*i.m*bball.m*norm(rtemp)/mag(rtemp)**3
    #tempforce=tempforce-kv*i.p/i.m
    return(tempforce)
            
def springforce(bball,balllist):
    
    #this finds the net spring force on the balls
    tempforce=vector(0,0,0)
    for i in balllist:
        if bball.pos.x==i.pos.x and bball.pos.y==i.pos.y and bball.pos.z==i.pos.z:
            tempforce=tempforce+vector(0,0,0)
        else:
            rr=bball.pos-i.pos
            if mag(rr)<2.2*R:
                s=mag(rr)-2*R
                Fs=-k*s*norm(rr)
                tempforce=tempforce+Fs
    return(tempforce)
        
    #check for overlap
    #find s
    #find force
    #add to total force
    
    
    
t=0
dt=0.01

while t<1500:
    rate(100000)
    for i in balls:
        i.F=springforce(i,balls)+gforce(i,balls)-kv*i.p/i.m
        i.p=i.p+i.F*dt
        #i.p=i.p+(calcforce(i,balls)-kv*i.p/i.m)*dt
        i.pos=i.pos+i.p*dt/i.m
        print(t,i.pos,)
    t=t+dt
print(t)
