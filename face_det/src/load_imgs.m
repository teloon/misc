function [train_data, avg_data] = load_imgs()
%load train images
train_fld = 'E:\\study\\courses\\模式识别课件\\练习2\\exercise\\练习二数据与说明\\ORL\\train\\';
test_fld = 'E:\\study\\courses\\模式识别课件\\练习2\\exercise\\练习二数据与说明\\ORL\\test\\';
picstr_tr = dir([train_fld, '*.bmp']);
[row_tr, col_tr] = size(picstr_tr);
picstr_te = dir([test_fld, '*.bmp']);
[row_te, col_te] = size(picstr_te);
gry = imread([train_fld, picstr_tr(1).name]);
train_data = zeros(row_tr, numel(gry));
avg_data = zeros(1, numel(gry));
for i=1:row_tr
%    fprintf(['\nreading %d ',' ',picstr_tr(i).name,'...\n'],row_tr);
    gry = imread([train_fld, picstr_tr(i).name]);
    gry = gry';
    gry = gry(1:end);
    train_data(i,:) = gry;
    avg_data = avg_data+double(gry);
end
avg_data = avg_data/row_tr;

end