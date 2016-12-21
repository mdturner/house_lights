%Configuration parameters
dt = 1/24.0; 		%max framerate is 57 Hz, so let's get cinematic.
G = 20; 		%Eat your heart out, Jens.
braneSpacing = 20;	%Really, this wasn't a hack for stability, I promise.
boundary = 434/2;	%434 pixels.

%four masses, with position and velocity
m = [ 1 1 1 1]; 	%R, G, B, and W, of course :).
x = rand(1,4) * 2.0 * boundary - boundary;
v = randn(1,4)*0;	%Inefficiency is key in academia


NOps = 100000;
timeSeries = zeros(NOps, 11);

tic
for time = 1:NOps

potentialEnergy = 0;
kineticEnergy = 0;

for massCounter = 1:4

	%Index the other masses	
	notIndex = 1:4 != massCounter;

	accelerations = ... 
 			sign(x(notIndex) - x(massCounter) ) .* ... 
			G .* m(notIndex) ./ ...
			(( x(notIndex) - x(massCounter) ).^2 + braneSpacing^2);

%	potentialEnergies = -G * m(massCounter) * m(notIndex) ./...
%				sqrt(( x(notIndex) - x(massCounter) ).^2 + braneSpacing^2);

%	potentialEnergy += sum(potentialEnergies);

	%at the edge? bounce!
	if( abs( x(massCounter) ) > boundary )
		v(massCounter) = v(massCounter) * -1;
	end

	v(massCounter) = v(massCounter) + sum(accelerations)*dt;

end

%Step forward
x = x + v*dt;

%kineticEnergy = sum(0.5 * m .* v.^2);

timeSeries(time,:) = [x v potentialEnergy kineticEnergy time*dt];

end

%Plot it!
plot(timeSeries(:,11),timeSeries(:,1:4),'.')
title('Christmas Lights on the Brane')
xlabel('time(s)');
ylabel('pixel');

toc
