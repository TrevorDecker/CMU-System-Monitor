function [  ] = histogram(path)
%Takes a path to a picture and a number between 0 and 255.
%Creates a thresholded image with all values greater then n set to black
%All values less then or equal to n are set to white
inputImage = imread(path);%pgm_read(path);
hist=zeros(1,255);
    for y =1:size(inputImage,1)
        for x = 1:size(inputImage,2)
            hist(inputImage(y,x)+1) = hist(inputImage(y,x)+1) + 1;
        end
        
    end

plot(hist)    
%image(outputImage);%for quick verification
%imwrite(outputImage, 'output.jpg');




end