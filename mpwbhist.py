#!/usr/bin/python3


varlist=['sfp_rx_power', 'sfp_tx_power','sfp_tx_bias', 'v_sca12', 'v_sca34', 'i_sca12', 'i_sca34', 'temp_board']
fcmd=open('mpwbhist.com','w')
# call me at end 
# odbedit -c @mpwbhist.com

for c in range(0,8):
    fcmd.write( 'cd /History/Display\n' )
    fcmd.write( 'mkdir PWBcol%d\n' % c )
    fcmd.write( 'cd PWBcol%d\n' % c )

    for var in varlist:
        fcmd.write( 'mkdir %s\n' % var )
        fcmd.write( 'cd %s\n' % var)

        fcmd.write( 'create string Variables[8][64]\n' )
        fcmd.write( 'create string Label[8][32]\n' )

        for r in range(0,8):
            fcmd.write( 'set Variables[%d] CTRL/pwb_%s:pwb_%s[%d]\n' % (r,var,var,c*8+r) )
            fcmd.write( 'set Label[%d] row%d\n' % (r,r) )
        
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
        fcmd.write( 'set Timescale "3d"\n' )

        fcmd.write( 'create bool "Zero ylow"\n' )
        fcmd.write( 'set "Zero ylow" 1\n' )
        fcmd.write( 'create bool "Log axis"\n' )
        fcmd.write( 'set "Log axis" 0\n' )

        fcmd.write( 'create bool "Sort vars"\n' )
        fcmd.write( 'set "Sort vars" 0\n' )
        fcmd.write( 'create bool "Show old vars"\n' )
        fcmd.write( 'set "Show old vars" 0\n' )
        
        fcmd.write( 'cd ..\n' )

    fcmd.write( 'cd /\n' )
fcmd.close()
