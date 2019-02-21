#!/usr/bin/python3

import pythonMidas

def mv2hist():
    key='/Equipment/CTRL/Settings/PWB/modules'
    pwbs=pythonMidas.getString( key ).split()
    fcmd=open('mMV2hist.com','w')
    #varlist=['pwb_mv2_xaxis', 'pwb_mv2_yaxis', 'pwb_mv2_zaxis', 'pwb_mv2_temp']
    varlist=['pwb_mv2_xaxis', 'pwb_mv2_yaxis', 'pwb_mv2_zaxis']
    lablist=['xaxis [T]', 'yaxis [T]', 'zaxis [T]']
    pwb_list=open('pwb_withMV2.list')
    for ipwb in pwb_list:
        ipwb = ipwb.strip()
        odb_index = pwbs.index(ipwb)
        fcmd.write( 'cd /History/Display/TPCHallProbes\n' )

        fcmd.write( 'mkdir %s\n' % ipwb )
        fcmd.write( 'cd %s\n' % ipwb )
        fcmd.write( 'create string Variables[%d][64]\n' % len(varlist) )
        fcmd.write( 'create string Label[%d][32]\n' % len(varlist) )
        for var in varlist:  
            #fcmd.write( 'mkdir %s\n' % var )
            #fcmd.write( 'cd %s\n' % var)

            hist_var_cmd = 'set Variables[%d] CTRL/%s:%s[%d]\n' % (varlist.index(var),var,var,odb_index)
            print(hist_var_cmd)
            fcmd.write( hist_var_cmd )

            fcmd.write( 'set Label[%d] "%s"\n' % (varlist.index(var), lablist[varlist.index(var)] ))

        fcmd.write( 'create float Minimum\n' )
        fcmd.write( 'set Minimum 0\n' )
        fcmd.write( 'create float Maximum \n' )
        fcmd.write( 'set Maximum 0\n' )
        
        fcmd.write( 'create bool "Show values"\n' )
        fcmd.write( 'set "Show values" 1\n' )
        fcmd.write( 'create bool "Show run markers"\n' )
        fcmd.write( 'set "Show run markers" 0\n' )
        
        fcmd.write( 'create float Factor\n' )
        fcmd.write( 'set Factor[*] 1\n' )
        fcmd.write( 'create float Offset\n' )
        fcmd.write( 'set Offset[*] 0\n' )
        
        fcmd.write( 'create string Timescale[1][32]\n' )
        fcmd.write( 'set Timescale "10m"\n' )
        
        fcmd.write( 'create bool "Zero ylow"\n' )
        fcmd.write( 'set "Zero ylow" 1\n' )
        fcmd.write( 'create bool "Log axis"\n' )
        fcmd.write( 'set "Log axis" 0\n' )
        
        fcmd.write( 'create bool "Sort vars"\n' )
        fcmd.write( 'set "Sort vars" 0\n' )
        fcmd.write( 'create bool "Show old vars"\n' )
        fcmd.write( 'set "Show old vars" 0\n' )
  
        fcmd.write( 'cd /\n' )
    fcmd.close()

if __name__ == '__main__':
    
    mv2hist()
    print('odbedit -c @mMV2hist.com')
