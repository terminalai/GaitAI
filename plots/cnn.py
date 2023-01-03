import sys
sys.path.append('PlotNeuralNet/')
from pycore.tikzeng import *

arch = [
    to_head('PlotNeuralNet'),
    to_cor(),
    to_begin(),

    #input
    to_input('hello.png'),
    to_Conv("conv1", 16, 8, offset="(0,0,0)",
            to="(0,0,0)", height=16, depth=16, width=2),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    to_Conv("conv2", 128, 64, offset="(1,0,0)",
            to="(pool1-east)", height=32, depth=32, width=2),
    to_connection("pool1", "conv2"),
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)",
            height=28, depth=28, width=1),
    to_SoftMax("soft1", 10, "(3,0,0)", "(pool1-east)", caption="SOFT"),
    to_connection("pool2", "soft1"),
    to_Sum("sum1", offset="(1.5,0,0)",
           to="(soft1-east)", radius=2.5, opacity=0.6),
    to_connection("soft1", "sum1"),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
