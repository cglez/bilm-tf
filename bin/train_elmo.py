import argparse
import json
from pathlib import Path

from bilm.training import train, load_vocab
from bilm.data import BidirectionalLMDataset


def main(args):
    # load the vocab
    vocab = load_vocab(args.vocab_file, 50)

    # define the options
    with open(args.options_file) as options_file:
        options = json.load(options_file)
    options['n_tokens_vocab'] = vocab.size

    prefix = args.train_prefix
    data = BidirectionalLMDataset(prefix, vocab, test=False,
                                  shuffle_on_load=True)

    tf_save_dir = args.save_dir
    Path(tf_save_dir).mkdir(parents=True, exist_ok=True)
    tf_log_dir = args.save_dir

    train(options, data, args.n_gpus, tf_save_dir, tf_log_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train a model')
    parser.add_argument('--save_dir', help='Location of checkpoint files', default='model')
    parser.add_argument('--vocab_file', help='Vocabulary file', default='vocab.txt')
    parser.add_argument('--train_prefix', help='Prefix for train files', default='data.txt')
    parser.add_argument('--options_file', help='Options JSON file', default='options.json')
    parser.add_argument('--n_gpus', help='Number of GPUs', type=int, default=1)

    args = parser.parse_args()
    main(args)
