s = tf('s');


G1 = zpk(-25,[-2,-3],2); % bieguy -2 dominujacy -3 nie 
G2 = zpk(0.01, [-2,-3],10); % to samo 
G3 = zpk([-1,-0.1],[-2,-3],100); % zera 0.1 dominujace 1 nie bieguny -2 bieguny to samo 
G4 = zpk([-1,0.1],[-0.1,-0.2],100); % zera to samo co wyzej bieguny -0.1 dominujace -0.2 nie 

%%

pzmap(G1)
pzmap(G2)
pzmap(G3)
pzmap(G4)
%%

G1p = zpk([],[-2,-3],2);
G2p = zpk([], [-2,-3],1000);
G3z = zpk([-0.1],[-2,-3],100);
G4z = zpk([-0.1],[-0.1,-0.2],100);

%%
%ltiview(G1,G1p)
%ltiview(G2,G2p)
%ltiview(G3,G3z)
ltiview(G4,G4z)

%% zad  2

G5 = zpk([],[-10,-10,-0.2,-1],20); %bieguny  -0.2 reszta nie dominujaca
G6 = zpk([],[-5,-0.5-1i,-0.5+1i],6.25); %bieguny zespolone dominujace 
G7 = zpk([],[-0.05,-0.5-1i,-0.5+1i],0.0625); %bieguny -0.05 dominujacy  
G8 = zpk([],[-10,-10,-0.05],5); %bieguny -0.05 dominuajcy 
G9 = zpk([],[0,-5],5); %biegun 0 dimunujacy 
G10 = zpk([],[-10,-10,100],10000);%bieguny nie wiem cos tam niestabilnosc 

%%

pzmap(G5);
pzmap(G6);
pzmap(G7);
pzmap(G8);
pzmap(G9);
pzmap(G10);

%%

G5z = zpk([],[-0.2,-1],20);
G6z = zpk([],[-0.5-1i,-0.5+1i],6.25); %bieguny zespolone dominujace 
G7z = zpk([],[-0.05],0.0625); %bieguny -0.05 dominujacy  
G8z = zpk([],[-0.05],5); %bieguny -0.05 dominuajcy 
G9z = zpk([],[0],5); %biegun 0 dimunujacy 
G10z = zpk([],[-10,-10,100],10000);%bieguny nie wiem cos tam niestabilnosc

%%

ltiview(G5,G5z);
ltiview(G6,G6z);
ltiview(G7,G7z);
ltiview(G8,G8z);
ltiview(G9,G9z);
ltiview(G10,G10z);

%%

G6z = zpk([],[-0.5-1i,-0.5+1i],6.25);

G620 = zpk([],[-0.5-1i,-0.5+1i],6.25*20);

G62 = zpk([],[-0.5-1i,-0.5+1i],6.25*2);

%%

G5z = zpk([],[-0.2,-1],20);

GO = tf(20,[1,0.2],'iodelay',1.25);

figure 
step(G5z)
figure
step(GO)