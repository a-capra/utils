#!/usr/bin/python3

import pythonMidas

MAX_PAD_ROW=int(72)
MAX_PAD_SEC=int(4)
MAX_PWB_RING=int(8)
MAX_PWB_COL=int(8)


def secrow_pwbpos(sec, row):
    sec -= 1
    if sec < 0:
        sec = 31
    lsec=list(range(4))
    lrow=list(range(72))
    pwb_pos=[]
    for i in lsec:
        for j in lrow:
            pwb_col = int((sec - i)/MAX_PAD_SEC)
            pwb_row = int((row - j)/MAX_PAD_ROW)
            #print(pwb_col,pwb_row)
            pair=[pwb_col,pwb_row]
            if pair in pwb_pos:
                continue
            else:
                pwb_pos.append([pwb_col,pwb_row])
    return pwb_pos
        
def print_pwb(sec, row):
    for pos in secrow_pwbpos(sec, row):
        ipwb=pos[0]*MAX_PWB_COL+pos[1]
        print('pad sector:',sec,'row:',row,
              'corresponds to',pwbs[ipwb],'at position:',pos)


if __name__ == '__main__':

    key='/Equipment/CTRL/Settings/PWB/modules'
    pwbs=pythonMidas.getString( key ).split()

    sec,row=15,215
    print_pwb(sec, row)

    sec,row=15,216
    print_pwb(sec, row)

    sec,row=18,215
    print_pwb(sec, row)

    sec,row=15,288
    print_pwb(sec, row)

    sec,row=15,432
    print_pwb(sec, row)
