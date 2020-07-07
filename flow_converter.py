from sys import argv

inv=1.0
inu='m3/s'
if len(argv)==2:
    inv=float(argv[1])
elif len(argv)==3:
    inv=float(argv[1])
    inu=argv[2]

from pint import UnitRegistry
ureg = UnitRegistry()


flow_units={ 'm3/s'  : ureg.meter**3/ureg.second,
             'cm3/s' : ureg.centimeter**3/ureg.second,
             'l/min' : ureg.liter/ureg.minute,
             'l/s'   : ureg.liter/ureg.second,
             'ml/s'  : ureg.milliliter/ureg.second}

flow=inv*flow_units[inu]
for ustr in flow_units:
    out=flow.to(flow_units[ustr])
    print('{:1.5f} {:s}'.format(out.magnitude,out.units))
