true_level = load('uni_2_levels_e.txt');
temp = 0;
file_head = 'gaps_01000000_';
ll = 0;
llvar = 0;
lm = 0;
for i = 1:11
    label = i - 1;
    if label < 10
        command = strcat('temp = ',file_head,'00',int2str(label),';');
    else
        command = strcat('temp = ',file_head,'0',int2str(label),';');
    end
    eval(command);
    
    if i == 1
        ll = temp;
        lm = priormass(temp);
    else
        ll = [ll;temp];
        lm = [lm;priormass(temp)];
    end
    
    if label < 10
        command = strcat('temp = std(exp(',file_head,'00',int2str(label),'));');
    else
        command = strcat('temp = std(exp(',file_head,'0',int2str(label),'));');
    end
    eval(command);
    if i == 1
        llvar = temp;
    else
        llvar = [llvar;temp];
    end
end


llvarlm(11) = 0;
llvarlm(1) = (true_level(1,2)+0)/2;
llvarlm(11) = (true_level(10,2)+min(log(lm)))/2;
for i = 2:10
    llvarlm(i) = (true_level(i,2) + true_level(i-1,2))/2;
end
ll = sort(ll,'descend');
lm = sort(lm,'ascend');

figure('Position', [0 0 1600 1600]);
%[AX, H1, H2] = plotyy(true_level(:,2), true_level(:,1), llvarlm, llvar);
%set(H1, 'LineStyle', 'none', 'Marker','o','MarkerFaceColor', 'b', 'MarkerEdgeColor','b', 'MarkerSize',8);
%hold(AX(1), 'on');
%plot(AX(1),log(lm),ll,'-','Color','b');
%set(H2, 'LineStyle', 'none', 'Marker', 'd', 'MarkerFaceColor', [0 0.502 0], 'MarkerSize', 8);
%set(AX, 'XLim', [min(log(lm)) max(log(lm))], 'FontSize', 16);
%xlabel(AX(1),'Log Prior Mass log(M)', 'FontSize', 20);
%ylabel(AX(1),'Log Likelihood log(L(M)), Blue Dots being the Levels', 'FontSize', 20);
%ylabel(AX(2),'Stdev of Likelihoods between Levels (Not Log)', 'FontSize', 20);
%set(AX(1),'XGrid','on');

subplot(211)
plot(true_level(:,2), true_level(:,1), 'd', 'MarkerFaceColor', 'b', 'MarkerEdgeColor','b', 'MarkerSize',8); hold all;
plot(log(lm),ll,'-','Color','b'); hold off;
set(gca, 'XLim', [min(log(lm)) max(log(lm))], 'FontSize', 16);
ylabel(gca,'Log Likelihood Threshold log(L^*(M))', 'FontSize', 20);
set(gca,'XGrid','on');

subplot(212)
plot(llvarlm, llvar, 'o', 'MarkerFaceColor', [0 0.502 0], 'MarkerEdgeColor', [0 0.502 0], 'MarkerSize', 8);
set(gca, 'XLim', [min(log(lm)) max(log(lm))], 'FontSize', 16);
xlabel(gca,'Log Prior Mass log(M)', 'FontSize', 20);
ylabel(gca,'Stdev of Likelihoods between Levels', 'FontSize', 20);
set(gca,'XGrid','on');

%nbins = 50;
%nintervals = 11;
%n(nintervals, nbins) = 0;
%x(nintervals, nbins) = 0;

%[AX, H1, H2] = plotyy(true_level(:,2),true_level(:,1),0,0);
%set(H1, 'LineStyle','none','Marker','o','MarkerFaceColor', 'b', 'MarkerEdgeColor','b', 'MarkerSize',8);
%hold(AX(1),'on');
%plot(AX(1),log(lm),ll,'-','Color','b');
%set(AX(1),'XLim',[-12 -0.5]);
%set(AX(2),'XLim',[-12 -0.5]);
%hold(AX(2),'on');
%for i = 2:11
%    label = i - 1;
%    if label < 10
%        command = strcat('temp = priormass(',file_head,'00',int2str(label),');');
%    else
%       command = strcat('temp = priormass(',file_head,'0',int2str(label),');');
%    end
%    eval(command);
%    if i == 1
%        temp = temp(find(temp<pi/4.));
%    end
%    [n(i,:) x(i,:)] = hist(temp, nbins);
%    bar(AX(2),log(x(i,:)), n(i,:), 'FaceColor', [0 0.5 0], 'EdgeColor', [0 0.5 0]);hold(AX(2),'on');
%end
%set(AX(2),'YLim',[0 5000]);
%set(AX(1),'XGrid','on');
%xlabel(AX(1),'Log Prior Mass log (M)', 'FontSize', 20);
%ylabel(AX(1),'Log Likelihood log (L(M))', 'FontSize', 20);
%set(AX(1),'FontSize',16);
%set(AX(2),'FontSize',16);