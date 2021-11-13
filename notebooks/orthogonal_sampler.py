import numpy as np
from itertools import product

def orthogonal_sampler_2d(rng, n_samples):
    r = 2
    m = 2
    s = int(np.ceil(np.sqrt(n_samples)))

    oa = np.array(list(product(list(range(1, s+1)), repeat=m)))
    lh = np.zeros(oa.shape)

    for c in range(oa.shape[1]):
        for k in range(1, s+1):
            idxs = np.where(oa[:,c] == k)
            col = oa[idxs]
            new_col = np.zeros(len(idxs[0]))

            for i in range(1, col.shape[0]+1):
                new_col[i-1] = (k - 1)*s + i

            rng.shuffle(new_col)

            lh[idxs[0],c] = new_col

    samples = rng.uniform(size=oa.shape)
    lh = (lh - samples)/np.max(lh)

    return lh
