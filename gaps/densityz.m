function fz = densityz(z, t)
if (z < -2*t+1)
    fz = 0;
end
if ((z >= -2*t+1) && (z < -1))
    fz = 1/t*(z+2*t-1);
end
if ((z >= -1) && (z < 1))
    fz = 2*(t-1)/t;
end
if ((z >= 1) && (z < 2*t-1))
    fz = 1/t*(-z+2*t-1);
end
if (z >= 2*t-1)
    fz = 0;
end