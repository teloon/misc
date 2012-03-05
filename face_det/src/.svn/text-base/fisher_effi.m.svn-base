function [fisher_vecs, fisher_vals, classes] = fisher_effi( train_data, avg_data)
[row_num, col_num] = size(train_data);
for i=1:row_num
    train_data(i,:) = train_data(i,:)-avg_data;
end
scatter = train_data*train_data';
[eigen_vec, eigen_val] = pcacov(scatter);
true_eigen_vec = zeros(col_num, 199);
for j=1:199
    true_eigen_vec(:,j) = train_data'*eigen_vec(:,j);
    true_eigen_vec(:,j) = true_eigen_vec(:,j)/norm(true_eigen_vec(:,j));
end
train_data_proj = train_data*true_eigen_vec;
sw = zeros(199, 199);
avg_data_proj_mat = zeros(40, 199);
total_avg_data_proj = zeros(1, 199);
for i=1:40
    avg_data_proj = zeros(1, 199);
    for j=1:5
        avg_data_proj = avg_data_proj + train_data_proj((i-1)*5+j,:);
    end
    avg_data_proj = avg_data_proj/5;
    avg_data_proj_mat(i,:) = avg_data_proj;
    total_avg_data_proj = total_avg_data_proj + avg_data_proj;
    for j=1:5
        diff = train_data_proj((i-1)*5+j,:) - avg_data_proj;
        sw = sw + diff'*diff;
    end
end
total_avg_data_proj = total_avg_data_proj/40;
sb = zeros(199, 199);
for i=1:40
    sb = sb + 5*(avg_data_proj_mat(i,:)-total_avg_data_proj)'*(avg_data_proj_mat(i,:)-total_avg_data_proj);
end
[fisher_vecs, fisher_vals] = eig(sb, sw+sb);
fisher_vals_vec = zeros(1,199);
fisher_ws = zeros(199, 39);
for i=1:199
    fisher_vals_vec(1,i) = fisher_vals(i,i);
end
for i=1:39
    [v, pos] = max(fisher_vals_vec);
    fisher_vals_vec(1,pos) = -Inf;
    fisher_ws(:,i) = fisher_vecs(:,pos)/norm(fisher_vecs(:,pos));
end
train_data_fisher = train_data_proj*fisher_ws;
test_fld = 'E:\\study\\courses\\模式识别课件\\练习2\\exercise\\练习二数据与说明\\ORL\\test\\';
picstr_tt = dir([test_fld, '*.bmp']);
[row_num, col] = size(train_data_fisher);
[file_num, col_tt] = size(picstr_tt);
dists = zeros(1, row_num);
classes = zeros(1, file_num);
for i=1:file_num
    gry = imread([test_fld, picstr_tt(i).name]);
    gry = gry';
    gry = gry(1:end);
    gry = double(gry)-avg_data;
    tt_new_proj = gry*true_eigen_vec;
    tt_fisher_proj = tt_new_proj*fisher_ws;
    for j=1:row_num
        dists(j) = norm(tt_fisher_proj-train_data_fisher(j,:));
    end
    [v, classes(i)] = min(dists);
    
end