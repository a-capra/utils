import os
import datetime as dt
import argparse

def get_hours_minutes_seconds(td):
  days = td.days
  hours, remainder = divmod(td.seconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  # If you want to take into account fractions of a second
  seconds += td.microseconds / 1e6
  seconds, milliseconds = divmod(seconds, 1)
  return int(hours), int(minutes), int(seconds), int(milliseconds*1e3)

def get_time_shift(l,tss):
  tstr=''
  for i,x in enumerate( l.split('-->') ):
    ts=x.split(':')
    secs=ts[2].split(',')
    temp=dt.timedelta(hours=float(ts[0]), minutes=float(ts[1]), seconds=float(secs[0]), milliseconds=float(secs[1]))
    temp+=tss
    if temp < dt.timedelta():
      temp=dt.timedelta()
    h,m,s,ms=get_hours_minutes_seconds(temp)
    tstr+='{:02d}:{:02d}:{:02d},{:03d}'.format(h,m,s,ms)
    if i==0: tstr+=' --> '
  return tstr+'\n'


if __name__ == '__main__':

  parser = argparse.ArgumentParser(prog='subtitles adjust timing',
                                  description=''' This programs helps you rewrite a subtitle file 
                                              of type srt by shifting the timestamps by a chosen amount
                                              thus resynchronizing the subs to the audio track.
                                              You will have to determine the shift yourself ''')
  parser.add_argument('infile', type=str, help='subtitle file, usually ending in srt')
  parser.add_argument('shift', type=float, help='time shift in seconds')
  args = parser.parse_args()

  filename, ext = os.path.splitext(args.infile)
  if ext != '.srt':
    print('Are you sure?')
  fname=filename+'_resync_0xAC'+ext
  resync=open(fname,'w+')

  time_shift=dt.timedelta(seconds=args.shift)

  with open(args.infile,'r') as fin:
    print(f'{args.infile} is being processed...')
    for line in fin:
      if '-->' in line:
        resync.write( get_time_shift(line, time_shift) )  
      else:
        resync.write(line)
  print(f'{fname} has been written')
  resync.close()