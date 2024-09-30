class Solution:
    def maximumTime(self, time: str) -> str:
        h, m = time.split(':')
        hh, mm = list(h), list(m)
        if hh[0] == '?' and hh[1] == '?':
            hh[0] = '2'
            hh[1] = '3'
        elif hh[0] == '?':
            if hh[1] >= '4':
                hh[0] = '1'
            else:
                hh[0] = '2'
        elif hh[1] == '?':
            if hh[0] == '2':
                hh[1] = '3'
            else:
                hh[1] = '9'

        if mm[0] == '?':
            mm[0] = '5'

        if mm[1] == '?':
            mm[1] = '9'
        
        return "".join(hh) + ":" + "".join(mm)