x = gaps_01000000_007;
[N,X] = hist(priormass(x),50);
figure('Position', [0 0 800 600]);
hist(priormass(x),50);
xlim([min(X) max(X)]);
set(gca,'YTickLabel','');
set(gca,'FontSize',20);
title('Prior Mass between Level 7 and Level 8','FontSize',25);