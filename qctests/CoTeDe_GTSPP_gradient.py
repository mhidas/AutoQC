from cotede_qc.cotede_test import get_qc
import numpy

def test(p, parameters):
    '''Run the gradient QC from the CoTeDe GTSPP config.'''

    config   = 'gtspp'
    testname = 'gradient'

    try:
        qc = get_qc(p, config, testname)
    except:
        qc = numpy.zeros(1, dtype=bool)

    return qc


