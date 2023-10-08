classdef TRIAD_Calculator_exported < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        UIFigure                        matlab.ui.Figure
        Label                           matlab.ui.control.Label
        TRIADandAngleBetweenTargetandCubeSatCameraCalculatorLabel  matlab.ui.control.Label
        DayEditField                    matlab.ui.control.NumericEditField
        DayEditFieldLabel               matlab.ui.control.Label
        MonthEditField                  matlab.ui.control.NumericEditField
        MonthEditFieldLabel             matlab.ui.control.Label
        YearEditField                   matlab.ui.control.NumericEditField
        YearEditFieldLabel              matlab.ui.control.Label
        CameraPositionYCoordinateEditField  matlab.ui.control.NumericEditField
        CameraPositionYCoordinateEditFieldLabel  matlab.ui.control.Label
        CameraPositionXcoordinateEditField  matlab.ui.control.NumericEditField
        CameraPositionXcoordinateEditFieldLabel  matlab.ui.control.Label
        HeightAbovetheEarthEditField    matlab.ui.control.NumericEditField
        HeightAbovetheEarthEditFieldLabel  matlab.ui.control.Label
        CubeSatLatitudeEditField        matlab.ui.control.NumericEditField
        CubeSatLatitudeEditFieldLabel   matlab.ui.control.Label
        CalculateButton                 matlab.ui.control.Button
        CEditField                      matlab.ui.control.NumericEditField
        CEditFieldLabel                 matlab.ui.control.Label
        ErrorinZDirectionEditField      matlab.ui.control.NumericEditField
        ErrorinZDirectionEditFieldLabel  matlab.ui.control.Label
        ErrorinYDirectionEditField      matlab.ui.control.NumericEditField
        ErrorinYDirectionEditFieldLabel  matlab.ui.control.Label
        ErrorinXDirectionEditField      matlab.ui.control.NumericEditField
        ErrorinXDirectionEditFieldLabel  matlab.ui.control.Label
        TargetLongitudeEditField        matlab.ui.control.NumericEditField
        TargetLongitudeEditFieldLabel   matlab.ui.control.Label
        TargetLatitudeEditField         matlab.ui.control.NumericEditField
        TargetLatitudeEditFieldLabel    matlab.ui.control.Label
        YawPsiEditField                 matlab.ui.control.NumericEditField
        YawPsiEditFieldLabel            matlab.ui.control.Label
        PitchThetaEditField             matlab.ui.control.NumericEditField
        PitchThetaEditFieldLabel        matlab.ui.control.Label
        RollPhiEditField                matlab.ui.control.NumericEditField
        RollPhiEditFieldLabel           matlab.ui.control.Label
        SecondEditField                 matlab.ui.control.NumericEditField
        SecondEditFieldLabel            matlab.ui.control.Label
        MinuteEditField                 matlab.ui.control.NumericEditField
        MinuteEditFieldLabel            matlab.ui.control.Label
        HourEditField                   matlab.ui.control.NumericEditField
        HourEditFieldLabel              matlab.ui.control.Label
        CubeSatLongitudeEditField       matlab.ui.control.NumericEditField
        CubeSatLongitudeEditFieldLabel  matlab.ui.control.Label
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Button pushed function: CalculateButton
        function CalculateButtonPushed(app, event)
            h = app.HeightAbovetheEarthEditField.Value;
            Lat = app.CubeSatLatitudeEditField.Value;
            Long = app.CubeSatLongitudeEditField.Value;
            yr=app.YearEditField.Value;
            Month=app.MonthEditField.Value;
            Day=app.DayEditField.Value;
            hr=app.HourEditField.Value;
            Min=app.MinuteEditField.Value;
            Sec=app.SecondEditField.Value;
            psi = app.RollPhiEditField.Value;
            theta = app.PitchThetaEditField.Value;
            phi = app.YawPsiEditField.Value;
            TargetLat = app.TargetLatitudeEditField.Value;
            TargetLong = app.TargetLongitudeEditField.Value;
            Rearth = 6378.137; %Radius of the Earth
            x = (Rearth+h)*cosd(Lat)*cosd(Long); %X coordinate
            y = (Rearth+h)*cosd(Lat)*sind(Long); %Y coordinate
            z = (Rearth+h)*sind(Lat); %Z coordinate
            r = sqrt((x^2)+(y^2)+(z^2)); %Location on Earth
            r1 = B_inner(x,y,z,r);
            r2 = Sun_inner(yr,Month,Day,hr,Min,Sec,x,y,z);
            r1a = r1/(sqrt(dot(r1,r1)))
            r2 = r2/(sqrt(dot(r2,r2)))
            A = A_inner(psi,theta,phi);
            b1 = A*r1a;
            b1x = b1(1)+(app.ErrorinXDirectionEditField.Value*b1(1));
            b1y = b1(2)+(app.ErrorinYDirectionEditField.Value*b1(2));
            b1z = b1(3)+(app.ErrorinZDirectionEditField.Value*b1(3));
            b1 = [b1x; b1y; b1z];
            b2 = A*r2;
            b2x = b2(1)+(app.ErrorinXDirectionEditField.Value*b2(1));
            b2y = b2(2)+(app.ErrorinYDirectionEditField.Value*b2(2));
            b2z = b2(3)+(app.ErrorinZDirectionEditField.Value*b2(3));
            b2 = [b2x; b2y; b2z];
            b1 = b1/(sqrt(dot(b1,b1)));
            b2 = b2/(sqrt(dot(b2,b2))); 
            j1 = cross(b1,b2);
            j1=j1/(sqrt(dot(j1,j1)));
            k = cross(b1,j1);
            k = k/(sqrt(dot(k,k)));
            L = [b1 j1 k];
            M = cross(r1a,r2);
            M = M/(sqrt(dot(M,M)));
            N = cross(r1a,M);
            N = N/(sqrt(dot(N,N)));
            O = [r1a M N];
            Otrans = transpose(O);
            O = Otrans;
            TRIAD = L*O
            fig = uifigure;
            uitable(fig,"DATA",TRIAD(:,:));
            fprintf('Element of Triad matrix = %22.20f/n',TRIAD(3,3))
            fprintf('Element of Triad matrix = %22.20f/n',TRIAD(2,3))
            E1 = -(asind(TRIAD(1,3)))
            E2 = atand(TRIAD(2,3)/TRIAD(3,3))
            E3 = atand(TRIAD(1,2)/TRIAD(1,1))
            [lambda, phi2, D, Dvector] = Camera_inner(x,y,z,r,Rearth,TargetLat,TargetLong)
            Cameramatrix = [app.CameraPositionXcoordinateEditField.Value; app.CameraPositionYCoordinateEditField.Value; 1];
            Cameramatrix = Cameramatrix/(sqrt(dot(Cameramatrix,Cameramatrix)))
            Cameravector = TRIAD*Cameramatrix
            app.CEditField.Value = acosd(dot(Cameravector,Dvector))
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
            B = [Bx; By; Bz]
            end
            function Sun = Sun_inner(yr,Month,Day,hr,Min,Sec,x,y,z)
            b1 = (7/4)*(yr+1);
            b2 = round(b1);
            c1 = (275*Month)/9;
            c2 = round(c1);
            Au = 149597870.691;
            JD = 1721013.5 + 367*yr - b2 + c2 +  Day + (60*hr+Min+Sec/60)/1440;
            Tu = (JD-2451545)/36525;
            Phi = 280.460 + 36000.771*Tu;
            Mo = 357.5277233 + 35999.05034*Tu;
            Phie = Phi + (1.914666471*sind(Mo)) + (0.019994643*sind(2*Mo));
            Epsilon = 23.439291 - 0.0120042*Tu;
            eo = [cosd(Phie) cosd(Epsilon).*sind(Phie) sind(Epsilon).*sind(Phie);];
            r1a = 1.000140612 - 0.016708617*cosd(Mo) - 0.000139589*cosd(2*Mo);
            format long
            R1 = r1a*Au;
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
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Create UIFigure and hide until all components are created
            app.UIFigure = uifigure('Visible', 'off');
            app.UIFigure.Position = [100 100 650 592];
            app.UIFigure.Name = 'MATLAB App';

            % Create CubeSatLongitudeEditFieldLabel
            app.CubeSatLongitudeEditFieldLabel = uilabel(app.UIFigure);
            app.CubeSatLongitudeEditFieldLabel.HorizontalAlignment = 'right';
            app.CubeSatLongitudeEditFieldLabel.Position = [438 529 108 22];
            app.CubeSatLongitudeEditFieldLabel.Text = 'CubeSat Longitude';

            % Create CubeSatLongitudeEditField
            app.CubeSatLongitudeEditField = uieditfield(app.UIFigure, 'numeric');
            app.CubeSatLongitudeEditField.Limits = [-180 180];
            app.CubeSatLongitudeEditField.Position = [561 529 80 22];

            % Create HourEditFieldLabel
            app.HourEditFieldLabel = uilabel(app.UIFigure);
            app.HourEditFieldLabel.HorizontalAlignment = 'right';
            app.HourEditFieldLabel.Position = [34 445 31 22];
            app.HourEditFieldLabel.Text = 'Hour';

            % Create HourEditField
            app.HourEditField = uieditfield(app.UIFigure, 'numeric');
            app.HourEditField.Limits = [0 24];
            app.HourEditField.Position = [80 445 62 22];

            % Create MinuteEditFieldLabel
            app.MinuteEditFieldLabel = uilabel(app.UIFigure);
            app.MinuteEditFieldLabel.HorizontalAlignment = 'right';
            app.MinuteEditFieldLabel.Position = [220 445 41 22];
            app.MinuteEditFieldLabel.Text = 'Minute';

            % Create MinuteEditField
            app.MinuteEditField = uieditfield(app.UIFigure, 'numeric');
            app.MinuteEditField.Limits = [0 59];
            app.MinuteEditField.Position = [276 445 69 22];

            % Create SecondEditFieldLabel
            app.SecondEditFieldLabel = uilabel(app.UIFigure);
            app.SecondEditFieldLabel.HorizontalAlignment = 'right';
            app.SecondEditFieldLabel.Position = [413 445 46 22];
            app.SecondEditFieldLabel.Text = 'Second';

            % Create SecondEditField
            app.SecondEditField = uieditfield(app.UIFigure, 'numeric');
            app.SecondEditField.Limits = [0 59];
            app.SecondEditField.Position = [474 445 52 22];

            % Create RollPhiEditFieldLabel
            app.RollPhiEditFieldLabel = uilabel(app.UIFigure);
            app.RollPhiEditFieldLabel.HorizontalAlignment = 'right';
            app.RollPhiEditFieldLabel.Position = [6 411 51 22];
            app.RollPhiEditFieldLabel.Text = 'Roll(Phi)';

            % Create RollPhiEditField
            app.RollPhiEditField = uieditfield(app.UIFigure, 'numeric');
            app.RollPhiEditField.Limits = [-360 360];
            app.RollPhiEditField.Position = [72 411 100 22];

            % Create PitchThetaEditFieldLabel
            app.PitchThetaEditFieldLabel = uilabel(app.UIFigure);
            app.PitchThetaEditFieldLabel.HorizontalAlignment = 'right';
            app.PitchThetaEditFieldLabel.Position = [189 411 70 22];
            app.PitchThetaEditFieldLabel.Text = 'Pitch(Theta)';

            % Create PitchThetaEditField
            app.PitchThetaEditField = uieditfield(app.UIFigure, 'numeric');
            app.PitchThetaEditField.Limits = [-360 360];
            app.PitchThetaEditField.Position = [274 411 100 22];

            % Create YawPsiEditFieldLabel
            app.YawPsiEditFieldLabel = uilabel(app.UIFigure);
            app.YawPsiEditFieldLabel.HorizontalAlignment = 'right';
            app.YawPsiEditFieldLabel.Position = [410 411 52 22];
            app.YawPsiEditFieldLabel.Text = 'Yaw(Psi)';

            % Create YawPsiEditField
            app.YawPsiEditField = uieditfield(app.UIFigure, 'numeric');
            app.YawPsiEditField.Limits = [-360 360];
            app.YawPsiEditField.Position = [477 411 100 22];

            % Create TargetLatitudeEditFieldLabel
            app.TargetLatitudeEditFieldLabel = uilabel(app.UIFigure);
            app.TargetLatitudeEditFieldLabel.HorizontalAlignment = 'right';
            app.TargetLatitudeEditFieldLabel.Position = [72 367 84 22];
            app.TargetLatitudeEditFieldLabel.Text = 'Target Latitude';

            % Create TargetLatitudeEditField
            app.TargetLatitudeEditField = uieditfield(app.UIFigure, 'numeric');
            app.TargetLatitudeEditField.Limits = [-90 90];
            app.TargetLatitudeEditField.Position = [171 367 100 22];

            % Create TargetLongitudeEditFieldLabel
            app.TargetLongitudeEditFieldLabel = uilabel(app.UIFigure);
            app.TargetLongitudeEditFieldLabel.HorizontalAlignment = 'right';
            app.TargetLongitudeEditFieldLabel.Position = [371 367 94 22];
            app.TargetLongitudeEditFieldLabel.Text = 'Target Longitude';

            % Create TargetLongitudeEditField
            app.TargetLongitudeEditField = uieditfield(app.UIFigure, 'numeric');
            app.TargetLongitudeEditField.Limits = [-180 180];
            app.TargetLongitudeEditField.Position = [480 367 100 22];

            % Create ErrorinXDirectionEditFieldLabel
            app.ErrorinXDirectionEditFieldLabel = uilabel(app.UIFigure);
            app.ErrorinXDirectionEditFieldLabel.HorizontalAlignment = 'right';
            app.ErrorinXDirectionEditFieldLabel.Position = [6 327 106 22];
            app.ErrorinXDirectionEditFieldLabel.Text = 'Error in X Direction';

            % Create ErrorinXDirectionEditField
            app.ErrorinXDirectionEditField = uieditfield(app.UIFigure, 'numeric');
            app.ErrorinXDirectionEditField.Limits = [0 1];
            app.ErrorinXDirectionEditField.Position = [127 327 60 22];

            % Create ErrorinYDirectionEditFieldLabel
            app.ErrorinYDirectionEditFieldLabel = uilabel(app.UIFigure);
            app.ErrorinYDirectionEditFieldLabel.HorizontalAlignment = 'right';
            app.ErrorinYDirectionEditFieldLabel.Position = [200 327 106 22];
            app.ErrorinYDirectionEditFieldLabel.Text = 'Error in Y Direction';

            % Create ErrorinYDirectionEditField
            app.ErrorinYDirectionEditField = uieditfield(app.UIFigure, 'numeric');
            app.ErrorinYDirectionEditField.Limits = [0 1];
            app.ErrorinYDirectionEditField.Position = [321 327 66 22];

            % Create ErrorinZDirectionEditFieldLabel
            app.ErrorinZDirectionEditFieldLabel = uilabel(app.UIFigure);
            app.ErrorinZDirectionEditFieldLabel.HorizontalAlignment = 'right';
            app.ErrorinZDirectionEditFieldLabel.Position = [404 327 106 22];
            app.ErrorinZDirectionEditFieldLabel.Text = 'Error in Z Direction';

            % Create ErrorinZDirectionEditField
            app.ErrorinZDirectionEditField = uieditfield(app.UIFigure, 'numeric');
            app.ErrorinZDirectionEditField.Limits = [0 1];
            app.ErrorinZDirectionEditField.Position = [525 327 76 22];

            % Create CEditFieldLabel
            app.CEditFieldLabel = uilabel(app.UIFigure);
            app.CEditFieldLabel.HorizontalAlignment = 'right';
            app.CEditFieldLabel.Position = [212 172 25 22];
            app.CEditFieldLabel.Text = 'C=';

            % Create CEditField
            app.CEditField = uieditfield(app.UIFigure, 'numeric');
            app.CEditField.ValueDisplayFormat = '%.15f';
            app.CEditField.Position = [252 172 135 22];

            % Create CalculateButton
            app.CalculateButton = uibutton(app.UIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.Position = [243 235 100 23];
            app.CalculateButton.Text = 'Calculate';

            % Create CubeSatLatitudeEditFieldLabel
            app.CubeSatLatitudeEditFieldLabel = uilabel(app.UIFigure);
            app.CubeSatLatitudeEditFieldLabel.HorizontalAlignment = 'right';
            app.CubeSatLatitudeEditFieldLabel.Position = [233 529 98 22];
            app.CubeSatLatitudeEditFieldLabel.Text = 'CubeSat Latitude';

            % Create CubeSatLatitudeEditField
            app.CubeSatLatitudeEditField = uieditfield(app.UIFigure, 'numeric');
            app.CubeSatLatitudeEditField.Position = [346 529 76 22];

            % Create HeightAbovetheEarthEditFieldLabel
            app.HeightAbovetheEarthEditFieldLabel = uilabel(app.UIFigure);
            app.HeightAbovetheEarthEditFieldLabel.HorizontalAlignment = 'right';
            app.HeightAbovetheEarthEditFieldLabel.Position = [12 529 128 22];
            app.HeightAbovetheEarthEditFieldLabel.Text = 'Height Above the Earth';

            % Create HeightAbovetheEarthEditField
            app.HeightAbovetheEarthEditField = uieditfield(app.UIFigure, 'numeric');
            app.HeightAbovetheEarthEditField.Position = [155 529 66 22];

            % Create CameraPositionXcoordinateEditFieldLabel
            app.CameraPositionXcoordinateEditFieldLabel = uilabel(app.UIFigure);
            app.CameraPositionXcoordinateEditFieldLabel.HorizontalAlignment = 'right';
            app.CameraPositionXcoordinateEditFieldLabel.Position = [6 282 164 22];
            app.CameraPositionXcoordinateEditFieldLabel.Text = 'Camera Position X coordinate';

            % Create CameraPositionXcoordinateEditField
            app.CameraPositionXcoordinateEditField = uieditfield(app.UIFigure, 'numeric');
            app.CameraPositionXcoordinateEditField.Limits = [-1 1];
            app.CameraPositionXcoordinateEditField.Position = [185 282 100 22];

            % Create CameraPositionYCoordinateEditFieldLabel
            app.CameraPositionYCoordinateEditFieldLabel = uilabel(app.UIFigure);
            app.CameraPositionYCoordinateEditFieldLabel.HorizontalAlignment = 'right';
            app.CameraPositionYCoordinateEditFieldLabel.Position = [297 282 167 22];
            app.CameraPositionYCoordinateEditFieldLabel.Text = 'Camera Position Y Coordinate';

            % Create CameraPositionYCoordinateEditField
            app.CameraPositionYCoordinateEditField = uieditfield(app.UIFigure, 'numeric');
            app.CameraPositionYCoordinateEditField.Limits = [-1 1];
            app.CameraPositionYCoordinateEditField.Position = [479 282 100 22];

            % Create YearEditFieldLabel
            app.YearEditFieldLabel = uilabel(app.UIFigure);
            app.YearEditFieldLabel.HorizontalAlignment = 'right';
            app.YearEditFieldLabel.Position = [17 483 29 22];
            app.YearEditFieldLabel.Text = 'Year';

            % Create YearEditField
            app.YearEditField = uieditfield(app.UIFigure, 'numeric');
            app.YearEditField.Position = [61 483 100 22];

            % Create MonthEditFieldLabel
            app.MonthEditFieldLabel = uilabel(app.UIFigure);
            app.MonthEditFieldLabel.HorizontalAlignment = 'right';
            app.MonthEditFieldLabel.Position = [206 483 38 22];
            app.MonthEditFieldLabel.Text = 'Month';

            % Create MonthEditField
            app.MonthEditField = uieditfield(app.UIFigure, 'numeric');
            app.MonthEditField.Position = [259 483 100 22];

            % Create DayEditFieldLabel
            app.DayEditFieldLabel = uilabel(app.UIFigure);
            app.DayEditFieldLabel.HorizontalAlignment = 'right';
            app.DayEditFieldLabel.Position = [444 483 26 22];
            app.DayEditFieldLabel.Text = 'Day';

            % Create DayEditField
            app.DayEditField = uieditfield(app.UIFigure, 'numeric');
            app.DayEditField.Position = [485 483 100 22];

            % Create TRIADandAngleBetweenTargetandCubeSatCameraCalculatorLabel
            app.TRIADandAngleBetweenTargetandCubeSatCameraCalculatorLabel = uilabel(app.UIFigure);
            app.TRIADandAngleBetweenTargetandCubeSatCameraCalculatorLabel.FontSize = 18;
            app.TRIADandAngleBetweenTargetandCubeSatCameraCalculatorLabel.FontWeight = 'bold';
            app.TRIADandAngleBetweenTargetandCubeSatCameraCalculatorLabel.Position = [34 561 580 23];
            app.TRIADandAngleBetweenTargetandCubeSatCameraCalculatorLabel.Text = 'TRIAD and Angle Between Target and CubeSat Camera Calculator';

            % Create Label
            app.Label = uilabel(app.UIFigure);
            app.Label.HorizontalAlignment = 'center';
            app.Label.WordWrap = 'on';
            app.Label.Position = [1 38 650 70];
            app.Label.Text = 'This calculates the TRIAD Algorithim for a CubeSat and the angle between an onboard camera on the CubeSat and a target. It simulates the effects of errors in the onboard sensors on these calculations. ';

            % Show the figure after all components are created
            app.UIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = TRIAD_Calculator_exported

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.UIFigure)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.UIFigure)
        end
    end
end