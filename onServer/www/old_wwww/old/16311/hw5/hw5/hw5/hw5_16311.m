function hw5_16311()

Thearshold = .4;
if(exist('findWaldo.png','file'));
    SearchImage =im2bw(imread('findWaldo.png','backgroundColor',1),Thearshold);
else
        SearchImage =im2bw(imread('findWaldo.pgm'));
end



waldo = im2bw(imread('waldo.png'),Thearshold);
BigWaldo = imresize(waldo, 2);
maxX = size(SearchImage,1);
maxY = size(SearchImage,2);

waldos = {waldo,BigWaldo};
PossiblePosition = {};
num = 1;

MaxError = 8;%for noisebetween 4 and 8
%waldos = [cos(th) -sin(th);sin(th) cos(th)]*waldo;
for w = 1:length(waldos)
waldo = waldos{w};
waldoWidth = size(waldo,1);
waldoHeigth = size(waldo,2);
for(x = 1:maxX)
   for(y = 1:maxY)
      %checks if waldo fits
      error = 100;
      if(x+waldoWidth < maxX && y+waldoHeigth < maxY)
            %is inbounds
            error = 0;
            for i = 1:waldoWidth
               for j =1:waldoHeigth
                    if SearchImage(x+i,y+j) ~= waldo(i,j)
                           %not a good match
                           error = error+1;
                           
                    end
                end
            end
      end
      if error < MaxError%possibleMatch == true
        PossiblePosition{num} = [x+waldoWidth/2,y+waldoHeigth/2];
        num = num +1;
      end
   end
end
end
fileID = fopen('waldo.txt','w');
for i = 1:length(PossiblePosition)
    A =PossiblePosition{i};
    fprintf(fileID,'%6.2f %12.2f\n',A);
end
length(PossiblePosition)


end