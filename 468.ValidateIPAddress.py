class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.find('.') != -1:
            item = IP.split('.')
            if len(item) != 4: return 'Neither'
            for num in item:
                try:
                    n = int(num)
                except:
                    return 'Neither'
                
                if n > 255 or n < 0: return 'Neither'
                if n == 0:
                    if len(num) != 1: return 'Neither'
                else: 
                    if num[0] == '0': return 'Neither'
            return 'IPv4'       

        elif IP.find(':') != -1: 
            item = IP.split(':')
            if len(item) != 8: return 'Neither'
            for num in item:
                if len(num) < 1 or len(num) > 4: return 'Neither'
                for n in num:
                    if ord('a') <= ord(n) <= ord('f') or ord('0') <= ord(n) <= ord('9') or ord('A') <= ord(n) <= ord('F'):
                        continue
                    return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'

a = Solution()
print(a.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
