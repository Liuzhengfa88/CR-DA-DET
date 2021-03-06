import os

net = "res101"
part = "test_t"
dataset = "clipart"
begin_epoch = 6
end_epoch = 12

model_prefix = "/data/experiments/DA_Faster_ICR_CCR/clipart/model/clipart_"

commond = "python eval/test.py --net {} --cuda --dataset {} --part {} --model_dir {}".format(net, dataset, part, model_prefix)

for i in range(begin_epoch, end_epoch + 1):
    print("epoch:\t", i)
    os.system(commond + str(i) + ".pth")