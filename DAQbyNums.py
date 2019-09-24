import pint

ureg = pint.UnitRegistry()

evt_size=78*511*2*4*64*ureg.byte
print( 'PWB Event Size: {:1.3f}'.format(evt_size.to(ureg.megabyte)) )

dead_time = 2.5*ureg.ms+511*16*ureg.ns
dead_time.ito(ureg.s)
print( 'Dead Time due to AFTER: {:1.2e}'.format(dead_time) )
rate=(dead_time**-1).to(ureg.Hz)
print( 'Maximum Rate: {:.0f}'.format(rate) )

event_rate=(rate*evt_size).to(ureg.Gbytes/ureg.s)
print( 'MAX PWB event rate: {:.5f}'.format(event_rate) )

print(' ')

evt_size=256*511*2*ureg.byte
print( 'AW Event Size: {:1.3f}'.format(evt_size.to(ureg.kilobyte)) )

evt_size=128*701*2*ureg.byte
print( 'SiPM Event Size: {:1.3f}'.format(evt_size.to(ureg.kilobyte)) )
