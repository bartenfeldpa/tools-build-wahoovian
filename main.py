import numpy as np
import logging

import wahoovian

if __name__ == '__main__':
    logging.basicConfig(filename='wahoovian-log.txt', level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')
    logging.info("Program starting!")
    mat1 = np.matrix([[1, 2], [3, 4]])
    mat2 = np.matrix([[12, -3], [16, 7]])
    mat3 = np.matrix([[12, 5], [16, 7, 8]])
    wahoovian.wahoovian(mat1)
    wahoovian.wahoovian(mat2)
    wahoovian.wahoovian(mat3)
    logging.info("Program ending!")
