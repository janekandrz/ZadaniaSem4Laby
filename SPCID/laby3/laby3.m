s = tf('s');

%% 2

G = ((B/k *s) + 1)/(M/k *s^2 + B/k * s +1) ;















%% 3.3

T1 = 1;
T2 = 2;
c = [-1,0,0.2,0.5,1,2,2.1,5,10];

for k=1:1:length(c)
    GA(k) = (c(k)*s+1)/((T1*s+1)*(T2*s+1));
end

ltiview(GA(1),GA(2),GA(3),GA(4),GA(5),GA(6),GA(7),GA(8),GA(9))


%% 3.8

T=0.25;
Eps = 0.25;
c = [0,0.05,0.1,0.2,0.5,1,1.5,5,-0.05];

for k=1:1:length(c)
    GB(k) = (c(k)*s+1)/(T^2*s^2+2*T*Eps*s+1);
end

ltiview(GB(1),GB(2),GB(3),GB(4),GB(5),GB(6),GB(7),GB(9))

%% 3.10

for k=1:1:length(c)
    GbC(k)=feedback(GB(k),1);
end

ltiview(GbC(1),GbC(2),GbC(3),GbC(4),GbC(5),GbC(6),GbC(7),GbC(8),GbC(9))







%% 4

k = 2 

Go = 

Gz = feedback(k*Go,1)

%tak kazdy inny regulator wplywa na zera bo I to 1/sT dodaje biegun który
%moze zadziałać na któres zero 
%a D jest dodaniem zera 