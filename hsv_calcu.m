clear

% 读取图像
Image = imread('4.png');

% 图像尺寸
[M,N,O] = size(Image);

% 空间转换
[h,s,v] = rgb2hsv(Image);

% 360级分布
h = h*360;

% 定义空间存储
mtx = zeros(1,359);

% 遍历整幅图像
for i = 1:M
    for j = 1:N
        kk = floor(h(i,j)) + 1; % 此处将色相做了取整
        mtx(1,kk) = mtx(1,kk) + 1;
    end
end

% 显示色相分布图
% 横轴为色相值，对应色相环上的角度
% 纵轴为此色相值对应的像素数量

plot(mtx);
xmin = 0;
xmax = 300;
ymin = 0;
ymax = 4000;
axis([xmin xmax ymin ymax])