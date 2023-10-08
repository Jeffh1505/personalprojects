import math
import numpy as np
import PySimpleGUI as sg
from PySimpleGUI import Window
def calculate(values):
    h = float(values['-HEIGHT-'])
    Lat = float(values['-LATITUDE-'])
    Long = float(values['-LONGITUDE-'])
    Y = float(values['-YEAR-'])
    M = float(values['-MONTH-'])
    D = float(values['-DAY-'])
    hr = float(values['-HOUR-'])
    m = float(values['-MINUTE-'])
    s = float(values['-SECOND-'])
    psi = float(values['-ROLL-'])
    theta = float(values['-PITCH-'])
    phi = float(values['-YAW-'])
    TargetLat = float(values['-TARGET_LATITUDE-'])
    TargetLong = float(values['-TARGET_LONGITUDE-'])
    ErrorX = float(values['-ERROR_X-'])
    ErrorY = float(values['-ERROR_Y-'])
    ErrorZ = float(values['-ERROR_Z-'])
    Rearth = 6378.137

    Lat_rads = math.radians(float(Lat))
    Long_rads = math.radians(float(Long))
    TargetLat_rads = math.radians(float(TargetLat))
    TargetLong_rads = math.radians(float(TargetLong))
    psi_rads = math.radians(float(psi))
    theta_rads = math.radians(float(theta))
    phi_rads = math.radians(float(phi))
    x = (Rearth + float(h)) * math.cos(Lat_rads) * math.cos(Long_rads)
    y = (Rearth + float(h)) * math.cos(Lat_rads) * math.sin(Long_rads)
    z = (Rearth + float(h)) * math.sin(Lat_rads)
    r = math.sqrt((x**2)+(y**2)+(z**2))

    # Function to calculate the magnetic field
    def Magnetic_field(x, y, z, r):
        g1 = -1669.05
        h1 = 5077.99
        g0 = -29554.63
        a = 6371.2
        mx = (a ** 3) * g1
        my = (a ** 3) * h1
        mz = (a ** 3) * g0
        Bx = (3 * ((mx * x) + (my * y) + (mz * z)) * x - (r ** 2) * (mx)) / (r ** 5)
        By = (3 * ((mx * x) + (my * y) + (mz * z)) * y - (r ** 2) * (my)) / (r ** 5)
        Bz = (3 * ((mx * x) + (my * y) + (mz * z)) * z - (r ** 2) * (mz)) / (r ** 5)
        math.sqrt((Bx ** 2) + (By ** 2) + (Bz ** 2))
        B2 = np.array([[Bx], [By], [Bz]])
        return B2;

    B2 = Magnetic_field(x, y, z, r)

    # Function to calculate the sun's position
    def Sun_Position(Y, M, D, hr, m, s, x, y, z):
        b1 = (7 / 4) * (float(Y) + 1)
        b2 = round(b1)
        c1 = (275 * float(M)) / 9
        c2 = round(c1)
        Au = 149597870.691
        JD = 1721013.5 + 367 * float(Y) - b2 + c2 + float(D) + (60 * float(hr) + float(m) + float(s) / 60) / 1440;
        Tu = (JD - 2451545) / 36525;
        Phi = 280.460 + 36000.771 * Tu;
        Mo = 357.5277233 + 35999.05034 * Tu;
        math.radians(Phi)
        Mo_rads = math.radians(Mo)
        Phie = Phi + (1.914666471 * math.sin(Mo_rads)) + (0.019994643 * math.sin(2 * Mo_rads))
        Epsilon = 23.439291 - 0.0120042 * Tu
        Phie_rads = math.radians(Phie)
        Epsilon_rads = math.radians(Epsilon)
        eo = np.array([[(math.cos(Phie_rads))], [(math.cos(Epsilon_rads) * math.sin(Phie_rads))],
                       [(math.sin(Epsilon_rads)) * (math.sin(Phie_rads))]])
        r1 = 1.000140612 - 0.016708617 * math.cos(Mo_rads) - 0.000139589 * math.cos(2 * Mo_rads);
        R1 = r1 * Au
        RA = R1 * eo
        RB1 = (RA[0]) - x
        RC1 = (RA[1]) - y
        RD1 = (RA[2]) - z
        R2 = np.sqrt((RB1 ** 2) + (RC1 ** 2) + (RD1 ** 2))
        e1 = RB1 / R2
        e2 = RC1 / R2
        e3 = RD1 / R2
        Sun = np.array([e1, e2, e3])
        return Sun;

    Sun = Sun_Position(Y, M, D, hr, m, s, x, y, z)

    # Function to calculate the attitude matrix
    def Attitude_Matrix(psi_rads, theta_rads, phi_rads):
        A = np.array([[math.cos(theta_rads) * math.cos(phi_rads), math.cos(theta_rads) * math.sin(phi_rads),
                       -math.sin(theta_rads)], [(-math.cos(psi_rads) * math.sin(phi_rads)) + (
                    math.sin(psi_rads) * math.sin(theta_rads) * math.cos(phi_rads)),
                                                (math.cos(psi_rads) * math.cos(phi_rads)) + (
                                                            math.sin(psi_rads) * math.sin(theta_rads) * math.cos(
                                                        phi_rads)), math.sin(psi_rads) * math.cos(theta_rads)], [
                          (math.cos(psi_rads) * math.sin(theta_rads) * math.cos(phi_rads)) + (
                                      math.sin(psi_rads) * math.sin(phi_rads)), (
                                      (math.cos(psi_rads) * math.sin(theta_rads) * math.sin(phi_rads)) - (
                                          math.sin(psi_rads) * math.cos(phi_rads))),
                          (math.cos(psi_rads) * math.cos(theta_rads))]])
        return A;

    A = Attitude_Matrix(psi_rads, theta_rads, phi_rads)
    r1 = B2 / (np.linalg.norm(B2))
    r2 = Sun / (np.linalg.norm(Sun))
    b1 = A * r1.T
    b1x = b1[0][-1] + ((float(ErrorX)) * b1[0][-1])
    b1y = b1[1][1] + ((float(ErrorY)) * b1[1][1])
    b1z = b1[2][0] + ((float(ErrorZ)) * b1[2][0])
    b1error = [b1x, b1y, b1z]
    b2 = A * r2.T
    b2x = b2[0][-1] + ((float(ErrorX)) * b2[0][-1])
    b2y = b2[1][1] + ((float(ErrorY)) * b2[1][1])
    b2z = b2[2][0] + ((float(ErrorZ)) * b2[2][0])
    b2error = [b2x, b2y, b2z]
    b1errornorm = b1error / (np.linalg.norm(b1error))
    b2errornorm = b2error / (np.linalg.norm(b2error))
    j1 = np.cross(b1errornorm, b2errornorm)
    j1norm = j1 / (np.linalg.norm(j1))
    k = np.cross(b1errornorm, j1norm)
    knorm = k / (np.linalg.norm(k))
    L = np.array([b1errornorm, j1norm, knorm]).T
    r12 = np.array([r1])
    r22 = np.array([r2])
    r12 = np.reshape(r12, (1, 3))
    r22 = np.reshape(r22, (1, 3))
    M = np.cross(r12, r22)
    Mnorm = M / (np.linalg.norm(M))
    N = np.cross(r12, M)
    Nnorm = N / (np.linalg.norm(N))
    O = np.array([r12, Mnorm, Nnorm])
    O = np.reshape(O, (3, 3))
    O = np.transpose(O, (0, 1))
    TRIAD = L @ O

    # Function to calculate target visibility
    def Target_Visibility(x, y, z, r, Rearth, TargetLat_rads, TargetLong_rads):
        Sxvector = x / r
        Syvector = y / r
        Szvector = z / r
        S = np.array([Sxvector, Syvector, Szvector])
        OTx = (Rearth * math.cos(TargetLat_rads) * math.cos(TargetLong_rads))
        OTy = (Rearth * math.cos(TargetLat_rads) * math.sin(TargetLong_rads))
        OTz = (Rearth * math.sin(TargetLat_rads))
        OT = math.sqrt((OTx ** 2) + (OTy ** 2) + (OTz ** 2))
        OTxvector = OTx / OT
        OTyvector = OTy / OT
        OTzvector = OTz / OT
        Tvector = np.array([OTxvector, OTyvector, OTzvector])
        A = np.dot(S, Tvector)
        B = Rearth / r
        Lambda = math.degrees(math.acos(A))
        Phi2 = math.degrees(math.asin(B))
        Dx = OTx - x
        Dy = OTy - y
        Dz = OTz - z
        D = math.sqrt((Dx ** 2) + (Dy ** 2) + (Dz ** 2))
        Dxvector = Dx / D
        Dyvector = Dy / D
        Dzvector = Dz / D
        Dvector = np.array([Dxvector, Dyvector, Dzvector])
        return Lambda, Phi2, D, Dvector

    Lambda, Phi2, D, Dvector = Target_Visibility(x, y, z, r, Rearth, TargetLat_rads, TargetLong_rads)
    Cameramatrix = np.array([0.5, 0.5, 1])
    Cameramatrixnorm = Cameramatrix / (np.linalg.norm(Cameramatrix))
    Cameravector = TRIAD @ Cameramatrixnorm

    F = np.dot(Cameravector, Dvector)
    C1 = math.acos(F)
    C=math.degrees(C1)
    return TRIAD, C
sg.theme('DarkTeal6')
# Define the layout of the GUI
layout = [
    [sg.Text('Height above the Earth:'), sg.Input(key='-HEIGHT-')],
    [sg.Text('Cubesat Latitude:'), sg.Input(key='-LATITUDE-')],
    [sg.Text('Cubesat Longitude:'), sg.Input(key='-LONGITUDE-')],
    [sg.Text('Year:'), sg.Input(key='-YEAR-')],
    [sg.Text('Month:'), sg.Input(key='-MONTH-')],
    [sg.Text('Day:'), sg.Input(key='-DAY-')],
    [sg.Text('Hour:'), sg.Input(key='-HOUR-')],
    [sg.Text('Minute:'), sg.Input(key='-MINUTE-')],
    [sg.Text('Second:'), sg.Input(key='-SECOND-')],
    [sg.Text('Roll(Phi):'), sg.Input(key='-ROLL-')],
    [sg.Text('Pitch(Theta):'), sg.Input(key='-PITCH-')],
    [sg.Text('Yaw(Psi):'), sg.Input(key='-YAW-')],
    [sg.Text('Target Latitude:'), sg.Input(key='-TARGET_LATITUDE-')],
    [sg.Text('Target Longitude:'), sg.Input(key='-TARGET_LONGITUDE-')],
    [sg.Text('Error In X Direction:'), sg.Input(key='-ERROR_X-')],
    [sg.Text('Error In Y Direction:'), sg.Input(key='-ERROR_Y-')],
    [sg.Text('Error in Z Direction:'), sg.Input(key='-ERROR_Z-')],

    [sg.Button('Calculate')],
    [sg.Text('TRIAD:'), sg.Text(size=(50, 5), key='-TRIAD-')],
    [sg.Text('C:'), sg.Text(size=(50, 1), key='-C-')],
    [sg.Text(size=(50, 5), key='-OUTPUT-')],

]

# Create the window
window: Window = sg.Window('Attitude Calculation', layout)


# Event loop to process GUI events
while True:
    event, values = window.read()

    # Handle events
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Calculate':
        TRIAD, C = calculate(values)
        window['-TRIAD-'].update(str(TRIAD))
        window['-C-'].update(str(C))

window.close()