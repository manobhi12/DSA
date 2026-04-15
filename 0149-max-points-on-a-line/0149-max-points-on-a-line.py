class Solution:
    def maxPoints(self, points):
        from math import gcd
        n = len(points)
        if n <= 2:
            return n
        
        res = 0
        
        for i in range(n):
            slopes = {}
            same = 1
            
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                dx = x2 - x1
                dy = y2 - y1
                
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1
                
                slopes[(dx, dy)] = slopes.get((dx, dy), 0) + 1
            
            res = max(res, same)
            for v in slopes.values():
                res = max(res, v + same)
        
        return res