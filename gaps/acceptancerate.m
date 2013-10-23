function ar = acceptancerate(a, d)
C = 2*(sqrt(a) - 1/sqrt(a));
ar = (2/(d-1/2)-2*a^(-d+1/2)/(d-1/2))/C;