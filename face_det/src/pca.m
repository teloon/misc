function [train_data ,true_eigen_vec, classes] = pca( train_data, avg_data, dim)
%PCA method
[row_num, col_num] = size(train_data);
for i=1:row_num
    train_data(i,:) = train_data(i,:)-avg_data;
end
scatter = train_data*train_data';
[eigen_vec, eigen_val] = pcacov(scatter);
true_eigen_vec = zeros(col_num, dim);
for j=1:dim
    true_eigen_vec(:,j) = train_data'*eigen_vec(:,j);
    true_eigen_vec(:,j) = true_eigen_vec(:,j)/norm(true_eigen_vec(:,j));
end
%test test-data
test_fld = 'E:\\study\\courses\\模式识别课件\\练习2\\exercise\\练习二数据与说明\\ORL\\test\\';
picstr_tt = dir([test_fld, '*.bmp']);
[row_num, col] = size(train_data);
[file_num, col_tr] = size(picstr_tt);
classes = zeros(1, file_num);
dists = zeros(1, row_num);
train_data_proj = train_data*true_eigen_vec;
for i=1:file_num
    gry = imread([test_fld, picstr_tt(i).name]);
    gry = gry';
    gry = gry(1:end);
    gry = double(gry)-avg_data;
    tt_new_proj = gry*true_eigen_vec;
    for j=1:row_num
        dists(j) = norm(train_data_proj(j,:)-tt_new_proj);
    end
    [v, classes(i)] = min(dists);
end
end
