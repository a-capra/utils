#!/usr/bin/python3

adc=['BarsADC11','BarsADC12','BarsADC13','BarsADC14','BarsADC17','BarsADC16']
ich=0   
fcmd=open('mBarsHist.com','w')
for iadc in adc:
    fcmd.write( 'cd /History/Display/Trigger\n' )
    fcmd.write( 'mkdir %s\n'%iadc )
    fcmd.write( 'cd %s\n'%iadc )
    fcmd.write( 'create string Variables[8][64]\n' )
    fcmd.write( 'create string Label[8][32]\n' )
    for ibar in range(8):
        hist_var_cmd = 'set Variables[%d] CTRL/scalers_rate:scalers_rate[%d]\n' % (ibar,112+ich)
        fcmd.write( hist_var_cmd )
        fcmd.write( 'set Label[%d] "Bar%02d"\n' % (ibar, ich+16) )
        ich += 1
        
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
