function hw4_16311try2(  )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

%img_path = input('Enter relative path to the image: ', 's');
%mask_path = input('Enter relative path to the mask: ', 's');

img_path = 'image2.pgm';
mask_path = 'mask3.pgm';

img = imread(img_path,'pgm');
mask = imread(mask_path,'pgm');
out = conv2((img),(mask));
%out = scale(out,255)
%out = contrast(out)
%out = convolve(img,mask);

%adjust contrast of image to make the mask more visable,
%only contrasts the range that was caulated so the outside 0's are not
%biassing the contrast
%out(1:size(img,1) - size(mask,1) +1,1:size(img,2)-size(mask,2) +1)= contrast(out(1:size(img,1) - size(mask,1) +1,1:size(img,2)-size(mask,2) +1));
%out = conv2(img,mask)
%out = scale(out,255);
%out(size(mask,1):size(img,1) - size(mask,1) +1,size(mask,1):size(img,2) - size(mask,2) +1)= contrast(out(size(mask,1):size(img,1) - size(mask,1) +1,size(mask,2):size(img,2)-size(mask,2) +1));
out= contrast(out(size(mask,1):size(img,1) - size(mask,1) +1,size(mask,2):size(img,2)-size(mask,2) +1));

image(out)
imwrite(out, 'output.pgm','pgm');




end

%scales all values to inside the range
function out = scale(matrix,range )
    max = 0;
    for m = 1:size(matrix,1)
        for n = 1:size(matrix,2)
            if(matrix(m,n) > max)
                 max = matrix(m,n);
            end
        end
    end
    
    for m = 1:size(matrix,1)
        for n = 1:size(matrix,2)
            matrix(m,n) = round(range*(matrix(m,n)/max));
        end
    end
    out = matrix;
end 


function out = convolve(x,h)
out = zeros(size(x,1),size(x,2));
for m = 1:size(x,1)-size(h,1)+1
for n = 1:size(x,2)-size(h,2)+1
    out(m:m+size(h,1)-1,n:n+size(h,2)-1) = double(out(m:m+size(h,1)-1,n:n+size(h,2)-1)) + double(x(m:m+size(h,1)-1,n:n+size(h,2)-1).*h);
end
end

%for m = 1:size(x,1) - size(h,1)+1
%    for n = 1:size(x,2) - size(h,2)+1
%        out(m,n) = 0;
%        for m0 = 1:size(h,1)
%            for n0 = 1:size(h,2)
%                out(m,n) = out(m,n) + x(m+m0-1,n+n0-1)*h(m0,n0);
                
                %i = m0 + m;
                %j = n0 + n;
                %if i < size(x,1) + 1 && j < size(x,2) + 1 
                %    out(m,n) = out(m,n) + x(i,j)*h(m0,n0);
                %end
%            end
%        end
%    end
%end

end

function contrasted = contrast(inputImage)
    %Takes a matrix of a picture and a number between 0 and 255.
    %Creates a thresholded image with all values greater then n set to black
    %All values less then or equal to n are set to white
        min =100000;%max possible value
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
    contrasted = round(multiplyer*(inputImage-min));
end