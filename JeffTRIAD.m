h = 422;
Lat = 48.5;
Long = -110.4;
Y = 2022;
M = 10;
D = 18;
hr = 11;
m = 50;
s = 02;
psi = 0;
theta = -90;
phi = 0;
TargetLat = 50.8;
TargetLong = -105.4;
Rearth = 6378.137; %Radius of the Earth
x = (Rearth+h)*cosd(Lat)*cosd(Long); %X coordinate
y = (Rearth+h)*cosd(Lat)*sind(Long); %Y coordinate
z = (Rearth+h)*sind(Lat); %Z coordinate
r = sqrt((x^2)+(y^2)+(z^2)); %Location on Earth
r1 = B_inner(x,y,z,r);
r2 = Sun_inner(Y,M,D,hr,m,s,x,y,z);
r1 = r1/(sqrt(dot(r1,r1)));
r2 = r2/(sqrt(dot(r2,r2)));
A = A_inner(psi,theta,phi);
b1 = A*r1;
b1x = b1(1)+(0.2*b1(1));
b1y = b1(2)+(0.1*b1(2));
b1z = b1(3)+(0.3*b1(3));
b1 = [b1x; b1y; b1z];
b2 = A*r2;
b2x = b2(1)+(0.2*b2(1));
b2y = b2(2)+(0.1*b2(2));
b2z = b2(3)+(0.3*b2(3));
b2 = [b2x; b2y; b2z];
b1 = b1/(sqrt(dot(b1,b1)));
b2 = b2/(sqrt(dot(b2,b2)));
j1 = cross(b1,b2);
j1=j1/(sqrt(dot(j1,j1)));
k = cross(b1,j1);
k = k/(sqrt(dot(k,k)));
L = [b1 j1 k];
M = cross(r1,r2);
M = M/(sqrt(dot(M,M)));
N = cross(r1,M);
N = N/(sqrt(dot(N,N)));
O = [r1 M N];
Otrans = transpose(O);
O = Otrans;
TRIAD = L*O
fprintf('Element of Triad matrix = %22.20f/n',TRIAD(3,3))
fprintf('Element of Triad matrix = %22.20f/n',TRIAD(2,3))
E1 = -(asind(TRIAD(1,3)))
E2 = atand(TRIAD(2,3)/TRIAD(3,3))
E3 = atand(TRIAD(1,2)/TRIAD(1,1))
[lambda, phi2, D, Dvector] = Camera_inner(x,y,z,r,Rearth,TargetLat,TargetLong)
Cameramatrix = [0.5; 0.5; 1];
Cameramatrix = Cameramatrix/(sqrt(dot(Cameramatrix,Cameramatrix)))
Cameravector = TRIAD*Cameramatrix
C = acosd(dot(Cameravector,Dvector))
function B = B_inner(x,y,z,r)
g1 = -1669.05;
h1 = 5077.99;
g0 = -29554.63;
a = 6371.2;
mx = (a^3)*g1; 
my = (a^3)*h1;
mz = (a^3)*g0; 
Bx = (3*((mx*x)+(my*y)+(mz*z))*x-(r^2)*(mx))/(r^5); %Magnetic field X component
By = (3*((mx*x)+(my*y)+(mz*z))*y-(r^2)*(my))/(r^5); %Magnetic field Y component 
Bz = (3*((mx*x)+(my*y)+(mz*z))*z-(r^2)*(mz))/(r^5); %Magnetic field Z component
B = sqrt((Bx^2)+(By^2)+(Bz^2)); %Total Magnetic field
B = [Bx; By; Bz];
end
function Sun = Sun_inner(Y,M,D,hr,m,s,x,y,z)
b1 = (7/4)*(Y+1);
b2 = round(b1);
c1 = (275*M)/9;
c2 = round(c1);
Au = 149597870.691;
JD = 1721013.5 + 367*Y - b2 + c2 + D + (60*hr+m+s/60)/1440;
Tu = (JD-2451545)/36525;
Phi = 280.460 + 36000.771*Tu;
Mo = 357.5277233 + 35999.05034*Tu;
Phie = Phi + (1.914666471*sind(Mo)) + (0.019994643*sind(2*Mo));
Epsilon = 23.439291 - 0.0120042*Tu;
eo = [cosd(Phie) cosd(Epsilon).*sind(Phie) sind(Epsilon).*sind(Phie);];
r1 = 1.000140612 - 0.016708617*cosd(Mo) - 0.000139589*cosd(2*Mo);
format long
R1 = r1*Au;
RA = R1*eo;
RB = RA(1)-x;
RC = RA(2)-y;
RD = RA(3)-z;
R2 = sqrt(RB^2+RC^2+RD^2);
e1 = RB/R2;
e2 = RC/R2;
e3 = RD/R2;
Sun = [e1; e2; e3]
end
function A = A_inner(psi, theta, phi)
A = [cosd(theta)*cosd(phi) cosd(theta)*sind(phi) -sind(theta); (sind(psi)*sind(theta)*cosd(phi))-cosd(psi)*sind(phi) (cosd(psi)*cosd(phi))+(sind(psi)*sind(theta)*sind(phi)) sind(psi)*cosd(theta); (cosd(psi)*sind(theta)*cosd(phi))+(sind(psi)*sind(phi)) (cosd(psi)*sind(theta)*sind(phi))-(sind(psi)*cosd(phi)) cosd(psi)*cosd(theta)];
end
function [lambda, phi2, D, Dvector] = Camera_inner(x,y,z,r,Rearth,TargetLat,TargetLong);
Sxvector = x/r;
Syvector = y/r;
Szvector = z/r;
S = [Sxvector Syvector Szvector];
OTx = (Rearth)*cosd(TargetLat)*cosd(TargetLong);
OTy = (Rearth)*cosd(TargetLat)*sind(TargetLong);
OTz = (Rearth)*sind(TargetLat);
OT = sqrt(OTx^2 + OTy^2 + OTz^2);
Txvector = OTx/OT;
Tyvector = OTy/OT;
Tzvector = OTz/OT;
Tvector = [Txvector Tyvector Tzvector];
lambda = acosd(dot(S,Tvector));
phi2 = asind(Rearth/r);
Dx = OTx - x;
Dy = OTy - y;
Dz = OTz - z;
D = sqrt(Dx^2 + Dy^2 + Dz^2);
Dxvector = Dx/D;
Dyvector = Dy/D;
Dzvector = Dz/D;
Dvector = [Dxvector; Dyvector; Dzvector]
end