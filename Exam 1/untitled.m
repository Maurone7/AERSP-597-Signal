% In this question you will attempt to build a ”camscanner” equivalent code that identifies the edges of a piece
% of paper, identifies the perspective transformation, and applies adaptive thresholding. You may assume that
% the original paper has only 4 sides and is of rectangular shape. Your tasks are as follows
I = (imread("Im8.png"));
imshow(I);
I = imresize(I, 0.3);
h = drawpolygon('FaceAlpha',0);
% Extract the vertices of the polygon
vertices = h.Position;
% Sort the vertices in a clockwise order
vertices = sortrows(vertices);
% Find the top and bottom vertices
top = vertices(1:2,:);
bottom = vertices(3:4,:);
% Sort the top and bottom vertices
top = sortrows(top);
bottom = sortrows(bottom);
% Find the top-left and top-right vertices
top_left = top(1,:);
top_right = top(2,:);
% Find the bottom-left and bottom-right vertices
bottom_left = bottom(1,:);
bottom_right = bottom(2,:);
% Find the width and height of the paper
width = sqrt((bottom_right(1) - bottom_left(1))^2 + (bottom_right(2) - bottom_left(2))^2);
height = sqrt((top_right(1) - bottom_right(1))^2 + (top_right(2) - bottom_right(2))^2);
% Define the destination points
destination_points = [0, 0; width, 0; width, height; 0, height];
% Define the source points
source_points = [top_left; top_right; bottom_right; bottom_left];
% Compute the perspective transformation
tform = maketform('projective', source_points, destination_points);
% Apply the perspective transformation
J = imtransform(I, tform);
% Show the original and transformed images
figure;
imshow(J)
% Convert the transformed image to grayscale
K = rgb2gray(J);
% Apply adaptive thresholding
L = adaptthresh(K, 0.4);
L = imbinarize(K, L);
% Show the thresholded image
figure;
imshow(L);
% Save the thresholded image
imwrite(L, 'thresholded_image.png');
% Save the perspective transformation

