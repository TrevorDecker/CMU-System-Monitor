function [  ] = Contrasting(path)
%Takes a path to a picture and a number between 0 and 255.
%Creates a thresholded image with all values greater then n set to black
%All values less then or equal to n are set to white
inputImage = imread(path);%pgm_read(path);
    min =255;%max possible value
    max = 0; %min possible value
    for y =1:size(inputImage,1)
        for x = 1:size(inputImage,2)
            if  inputImage(y,x) <min
                min = inputImage(y,x);
            end
            if inputImage(y,x) >max
                   max = inputImage(y,x);
            end
        end
        
    end
multiplyer = (255/double(max -min));
outputImage = multiplyer*(inputImage-min);

image(outputImage);%for quick verification
imwrite(outputImage, 'output.jpg');




end







