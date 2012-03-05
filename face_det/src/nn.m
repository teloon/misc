function classes = nn(train_data)
test_fld = 'E:\\study\\courses\\模式识别课件\\练习2\\exercise\\练习二数据与说明\\ORL\\test\\';
dirstr = dir([test_fld,'*.bmp']);
[file_num,col] = size(dirstr);
[train_num,col] = size(train_data);
classes = zeros(1, file_num);
dists = zeros(1, train_num);
for i=1:file_num
    gry = imread([test_fld, dirstr(i).name]);
    gry = gry';
    gry = gry(1:end);
    gry = double(gry)
    for j=1:train_num
        disp(size(gry));
        disp(size(train_data));
        disp(size(train_data(j,:)));
        r = train_data(j,:);
        diff = (gry-r);
        dists(j) = norm(diff);
    end
    [v,classes(i)] = min(dists);
end