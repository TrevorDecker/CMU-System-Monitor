function [ c ] = convolution(A,B )
%should act just like the built in convolve funciton
c = zeros(1,length(A) + length(B) -1);
for i = 1:length(B)
     for j = 1:length(c)
         h = zeros(1,length(c));
         h(i:i+length(B)-1) = B;
         x = zeros(1,length(c));
         x(1:length(A)) = A;
     c(i) = c(i) + h(j)*x(j);
     end
     c
end


end

