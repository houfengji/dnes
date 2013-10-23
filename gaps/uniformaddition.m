for t = 1:0.1:3
    [N X] = hist(t.*x + (1-t).*y, 50);
    dX = X(2)-X(1);
    bar(X, N./sum(N)./dX);
    xlim([-5 5]);
    title(t);
    z = (-2*t+1):0.1:(2*t-1);
    fz = zeros(length(z));
    for i = 1:length(z)
        fz(i) = densityz(z(i), t);
    end
    hold all;
    plot(z, fz, '.');
    hold off;
    pause;
end