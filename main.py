import logging
import argparse

def main():
    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Parse input parameters
    parser = argparse.ArgumentParser(description='Football voter',
                                     formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=60))

    parser.add_argument('-t', '--token', help='Token from Bot Father')

    args = parser.parse_args()
    if args.token is None:
        parser.error('Token is not specified')


if __name__ == '__main__':
    main()

