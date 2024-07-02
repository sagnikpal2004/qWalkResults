import qWalkBuilder as qWB

# Command line arguments
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Get memoized quantum walk results')

    help = "The shift operator to use [16nT: 4x4-node torus]"
    parser.add_argument('--shift', type=str, choices = ['16nT'], default='16nT', help=help)

    help = "The coin operator to use [H: Hadamard, G: Grover]"
    parser.add_argument('--coin', type=str, choices = ['H'], default='H', help=help)

    help = "The initial state to use. [singleNode: Single node]"
    parser.add_argument('--init', type=str, choices = ['singleNode'], default='singleNode', help=help)

    help = "The measurement basis to use. [Eigen: Eigenvectors of the shift-coin operator, Z: Computational basis]"
    parser.add_argument('--basis', type=str, choices=['Eigen', 'Z'], default='Eigen', help=help)

    help = "The number of time steps to take"
    parser.add_argument('--steps', type=int, default=64, help=help)

    help = "Force re-measure and overwrite existing results"
    parser.add_argument('--remeasure', action='store_true', help=help)

    help = "The mode of display of results"
    parser.add_argument('--display', type=str, choices=['PASS'], default='PASS', help=help)

    args = parser.parse_args()
    if args.coin == 'H':
        coin = qWB.buildQC.Coin.hadamard
    if args.init == 'singleNode':
        init = qWB.buildQC.Init.singleNode
# End Command line arguments

# File path to store results
RESULT_FILE = f"./{args.shift}.{args.coin}.{args.basis}/{args.init}.csv"
def displayResult():
    pass

# Check if file exists
import os
if not args.remeasure and os.path.exists(RESULT_FILE):
    displayResult()
    exit()

# Run the quantum walk
if args.shift == '16nT':
    shiftCoinQC = qWB.buildQC.build16nTQW(1, coin, init)

