import logging
from threading import Thread

# define the global variable
value = 0
# initialize logger
logging.basicConfig(format='%(asctime)s.%(msecs)03d: %(message)s', level=logging.INFO, datefmt="%H:%M:%S")


# make additions into the global variable
def adder(amount, repeats):
    global value
    for _ in range(repeats):
        value += amount


# make subtractions from the global variable
def subtractor(amount, repeats):
    global value
    for _ in range(repeats):
        value -= amount


def start_threads():
    # start the adder thread
    adder_thr = Thread(target=adder, args=(100, 1000000))
    adder_thr.start()
    # start the subtractor thread
    subtractor_thr = Thread(target=subtractor, args=(100, 1000000))
    subtractor_thr.start()
    return adder_thr, subtractor_thr


def main():
    global value
    logging.info(f'Expected final value: 0')
    adder_thread, subtractor_thread = start_threads()
    # wait for both threads to finish
    logging.debug(f'Waiting for threads to finish...')
    adder_thread.join()
    subtractor_thread.join()
    # report the value
    logging.critical(f'Actual final value: {value}')


if __name__ == "__main__":
    main()
