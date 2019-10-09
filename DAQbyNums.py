import pint

ureg = pint.UnitRegistry()

pwb_evt_size=78*511*2*4*64*ureg.byte
print( 'PWB Event Size: {:1.3f}'.format(pwb_evt_size.to(ureg.megabyte)) )

#dead_time = 2.5*ureg.ms+511*16*ureg.ns
dead_time = 1.6*ureg.ms+511*16*ureg.ns
dead_time.ito(ureg.s)
print( 'Dead Time due to AFTER: {:1.2e}'.format(dead_time) )
rate=(dead_time**-1).to(ureg.Hz)
print( 'Maximum Rate: {:.0f}'.format(rate) )

event_rate=(rate*pwb_evt_size).to(ureg.Gbytes/ureg.s)
print( 'MAX PWB event rate: {:.5f}'.format(event_rate) )

print(' ')

aw_evt_size=256*511*2*ureg.byte
print( 'AW Event Size: {:1.3f}'.format(aw_evt_size.to(ureg.kilobyte)) )

sipm_evt_size=128*701*2*ureg.byte
print( 'SiPM Event Size: {:1.3f}'.format(sipm_evt_size.to(ureg.kilobyte)) )

a16_evt_size=aw_evt_size+sipm_evt_size
print( 'ALPHA-16 Event Size: {:1.2f}'.format(a16_evt_size.to(ureg.kilobyte)) )

a16_event_rate=(rate*a16_evt_size).to(ureg.Gbytes/ureg.s)
print( 'ALPHA-16 event rate (assuming PWB dead time): {:.5f}'.format(a16_event_rate) )
