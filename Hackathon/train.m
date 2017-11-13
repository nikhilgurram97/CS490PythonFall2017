%test=importdata('test.csv');
%train=importdata('train.csv');

%x=str2double(train.textdata(2:end,5)).';  %LotArea
%t=(train.data).';  %Target

net = feedforwardnet(10);
net = configure(net,x,t);

net = train(net,x,t);
