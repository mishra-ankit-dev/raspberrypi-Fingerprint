clc
clear all
close all
pkg load image

%%%%%%%%-----------Reference image------------%%%%%%%%%

A_ref=imread('/home/pi/Documents/projects/fingerprint/webcam/image/amit1.jpeg');
% figure 
imagesc(A_ref)
A_ref=A_ref(100:170,300:340,:);
imshow(A_ref)


    %Isolate Y. 
Y_ref = A_ref(:,:,1);
    %Isolate Cb. 
Cb_ref = A_ref(:,:,2);
    %Isolate Cr. 
Cr_ref= A_ref(:,:,3);
    %Create a YCbCr image with only the Y component.  

% figure
% imshow(Y_ref)
% 
% figure
% imshow(Cb_ref)
% 
% figure
% imshow(Cr_ref)
%%%%------Local Binary Features---------------------%%%%%%5
features1_ref = imhist(Y_ref);
features2_ref = imhist(Cb_ref);
features3_ref = imhist(Cr_ref);

% figure
% bar(features1_ref)
% 
% figure
% bar(features2_ref)

% figure
% bar(features3_ref)

features_ref=[features1_ref features2_ref features3_ref];






%%%%%%------------Test image------------------------%%%%%%


A_test=imread('/home/pi/Documents/projects/fingerprint/webcam/image/amit2.jpeg');
% figure 
 imshow(A_test)
A_test=A_test(100:170,300:340,:);
 imshow(A_test)
% figure  
% imshow(YCbCr_test)
    %Isolate Y. 
Y_test = A_test(:,:,1);
    %Isolate Cb. 
Cb_test = A_test(:,:,2);
    %Isolate Cr. 
Cr_test= A_test(:,:,3);
    %Create a YCbCr image with only the Y component.  



% figure
% imshow(Y_test)
% 
% figure
% imshow(Cb_test)
% 
% figure
% imshow(Cr_test)

features1_test = imhist(Y_test);
features2_test = imhist(Cb_test);
features3_test = imhist(Cr_test);

%figure
%bar(features1_test)

%figure
%bar(features2_test)

%figure
%bar(features3_test)

features_test=[features1_test features2_test features3_test];

%figure
%bar(features_test)

%%%%%%%%%%------------------Co-occurrence of LBP-----------%%%%%5

D_LBP= sum((features_ref-features_test).^2).^0.5

%%%%%%------Chi square distance-------------------------%%%%%%
C_LBP=(sum((features_ref-features_test).^2).^0.5)./(sum(features_ref+features_test))

