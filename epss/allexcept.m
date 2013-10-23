function sam = allexcept(total, ens, ini)
sam(int32(total*(ens-1)/ens),1)=int32(0);
j = 1;
if ini == ens
    ini = 0;
end
for i = 1:total
    if mod(i,ens) ~= ini
        sam(j) = i;
        j = j + 1;
    end
end