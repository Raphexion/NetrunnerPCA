import numpy as np


def create_space(points):
    X = np.vstack(points) # .transpose()
    U, ss, V = np.linalg.svd(X, full_matrices=0)

    # the eigenvalues of SVD is the square of
    # of the covariance eigenvalues
    s = np.sqrt(ss)

    # for our own convinience,
    # normalize s
    s = s / np.sum(s)

    return U, s, V

def transform(s, V, x, depth=1.0):
    taken_V = []
    taken_s = 0.0
    for sv, Vv in zip(s, V):
        taken_V.append(Vv)
        taken_s += sv
        if taken_s >= depth:
            break

    y = np.zeros_like(x)
    tot_resp = 0.0
    for Vv in taken_V:
       resp = np.dot(x, Vv)
       tot_resp += resp

       y += resp * Vv

    y = -y # why do we need this?
    return y / tot_resp
