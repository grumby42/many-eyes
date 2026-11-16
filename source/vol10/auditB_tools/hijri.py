import datetime
M=["Muharram","Safar","Rabi I","Rabi II","Jumada I","Jumada II","Rajab","Shaban","Ramadan","Shawwal","Dhu al-Qada","Dhu al-Hijja"]
EPOCH=1948439.5  # civil
def jd(y,m,d):
    a=(14-m)//12; y2=y+4800-a; m2=m+12*a-3
    return d+(153*m2+2)//5+365*y2+y2//4-y2//100+y2//400-32045
def toh(y,m,d):
    j=jd(y,m,d)
    yr=(30*(j-1948440)+10646)//10631
    def hj(Y,Mo,D): return D+ -(-29.5*(Mo-1))//1*0 + int(__import__('math').ceil(29.5*(Mo-1)))+(Y-1)*354+(3+11*Y)//30+1948440-1
    mo=min(12,int(__import__('math').ceil((j-(29+hj(yr,1,1)))/29.5))+1)
    dd=j-hj(yr,mo,1)+1
    return yr,mo,dd
for s in ["1799-02-07","1799-12-08","1800-01-21","1800-11-10","1802-06-07","1803-08-04","1826-04-13","1826-05-15","1826-08-13","1827-06-30","1827-07-09","1828-02-28","1830-07-27","1830-07-29","1830-08-01","1830-08-31","1830-12-15","1830-12-21","1831-08-16","1834-05-10","1835-04-28","1799-02-01","1799-06-01","1799-12-01","1803-01-01","1803-03-31"]:
    y,m,d=map(int,s.split('-')); h=toh(y,m,d)
    print(s, datetime.date(y,m,d).strftime('%A'), h[2], M[h[1]-1], h[0])
