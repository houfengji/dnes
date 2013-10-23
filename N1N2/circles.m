s = [ 7.4142 4.1611 2.2523; 7.4045 4.4941 2.3438; 7.3988 4.2809 2.3565];

llim = 3.5;
rlim = 5.5;
n1 = 4:0.5:5;
n2 = 4:0.5:5;
cx=zeros(3,1);
cy=zeros(3,1);

figure('Position', [0 0 800 800]);
xlim([llim rlim]);
ylim([llim rlim]);
p  = get(gca, 'Position');
lx = get(gca, 'XLim');
ly = get(gca, 'YLim');

for i = 1:3
    cx(i) = (n1(i) - lx(1))/(lx(2) - lx(1)) * p(3) + p(1);
    cy(i) = (n2(i) - ly(1))/(ly(2) - ly(1)) * p(4) + p(2);
end

r = 0.006;
rt = 0.05;  %textbox radius...
for i = 1:3
    for j = 1:3
        rs = r*s(i,j);
        annotation('ellipse', [cx(i)-rs cy(j)-rs 2*rs 2*rs], 'LineWidth', 3);
        ss = sprintf('%.4f',s(i,j));
        annotation('textbox', [cx(i)-rt cy(j)+rs 2*rt rt], 'String', ss, 'FontSize', 16, 'FitHeightToText', 'on', 'LineStyle', 'none');
    end
end

stitle = sprintf('dimension %d, true evidence is %.4s \n stdev of these experiments is the number above the circle times 10^{-15} \n mean of these experiments are very close to true value \n experiments are repeated 10^3 times', 10, 9.7656e-14);
title(stitle,'FontSize',16);
set(gca, 'FontSize', 16);
xlabel('log_{10} N2 (chain length to evaluate evidence)','FontSize',16)
ylabel('log_{10} N1 (chain length to build levels)','FontSize',16)