s = tf("s");

G1 = 2/(s^2+s+5);

%step(G1)

% ts = 4 / xi wn

% ts = 8

Gf = 1/(1+8.8/22.5 *s);




Gz = (0.9+0.032*s)/(s^2*0.1+s*0.3906+1);

Gzf = Gf*Gz;


ltiview(Gz,Gzf)
