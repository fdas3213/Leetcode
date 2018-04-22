def romanToInt(self, s):
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        out = 0
        for i in range(len(s) - 1):
            if d[s[i]] < d[s[i+1]]:
                out -= d[s[i]]
            else:
                out += d[s[i]]
        out += d[s[-1]]
        return out
