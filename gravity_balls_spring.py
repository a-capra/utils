from __future__ import division, print_function
from vpython import *
scene = canvas(title='3D scene')

R=0.1
ball1=sphere(pos=vector(-1,0,0), radius=R)
ball2=sphere(pos=vector(1,0,0), radius=R)

ball1.m=1
ball2.m=1

G=6.67e-4

ball1.p=vector(0,0,0)
ball2.p=vector(0,0,0)
#ball1.F=vector(1,2,3)
#print(ball1.F)

t=0
dt=0.001

k=5
kv=.02

while t<400:
    rate(1000)
    Fs=vector(0,0,0)
    r=ball2.pos-ball1.pos
    Fg=-G*ball1.m*ball2.m*norm(r)/mag(r)**2
    if mag(r)<2*R:
        s=mag(r)-2*R
        Fs=-k*s*norm(r)
        
    ball2.F=Fg+Fs-kv*ball2.p/ball2.m
    ball1.F=-Fg-Fs-kv*ball1.p/ball1.m
    ball2.p=ball2.p+ball2.F*dt
    ball1.p=ball1.p+ball1.F*dt
    ball2.pos=ball2.pos+ball2.p*dt/ball2.m
    ball1.pos=ball1.pos+ball1.p*dt/ball1.m
    t=t+dt
	