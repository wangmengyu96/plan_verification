from random_objects import *
import numpy as np
from data_generator import *

#TODO: VSCode is not working with this test...
class TestClass:
    def setup(self):
        pass

    def gmm_quadform(self):
        n = 2
        mu_x = np.random.rand(n, 1)
        Sigma = random_psd_matrix(n)
        A = random_psd_matrix(n)
        mvn1 = MultivariateNormal(mu_x, Sigma)
        mvn2 = MultivariateNormal(mu_x, Sigma)
        gmm = MixtureModel([(0.1, mvn1), (0.9, mvn2)])
        gmmqf = GmmQuadForm(A, gmm)
        print(gmmqf.upper_tail_probability(1.0))

if __name__ == "__main__":
    tc = TestClass()
    tc.test_mvn_frame_change()