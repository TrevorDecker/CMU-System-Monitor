function [  ] = Thresholding(path,n  )
%Takes a path to a picture and a number between 0 and 255.
%Creates a thresholded image with all values greater then n set to black
%All values less then or equal to n are set to white
inputImage = imread(path);%pgm_read(path);
outputImage = ones(size(inputImage,1),size(inputImage,2));
for y =1:size(inputImage,1)
    for x = 1:size(inputImage,2)
        if  inputImage(y,x) > n
               outputImage(y,x) = 255;
        else
               outputImage(y,x) = 0;
        end
    end
end
image(outputImage);%for quick verification
imwrite(outputImage, 'output.jpg');




end



