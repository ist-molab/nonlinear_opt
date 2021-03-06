import numpy as np


class Optimizer:
    def __init__(self, f, df, ddf, alpha=1e-3, eps=1e-6, path=None):
        self.f = f
        self.df = df
        self.ddf = ddf
        self.alpha = alpha
        self.eps = eps
        self.path = path
        self.opt_sol = None
        self.opt_val = None

    def optimize(self, init_sol):
        x = init_sol
        path = []
        grad = self.df(x)
        hesse = self.ddf(x)
        path.append(x)
        while (grad**2).sum() > self.eps**2:
            x = x - np.linalg.solve(hesse, grad)
            grad = self.df(x)
            hesse = self.ddf(x)
            path.append(x)
        self.path = np.array(path)
        self.opt_sol = x
        self.opt_val = self.f(x)


if __name__ == '__main__':
    n_size = 10
    A = np.random.random((n_size, n_size))
    A = A.T @ A
    x0 = np.random.random(n_size)
    print(x0)

    optimizer = Optimizer(lambda x: x @ A @ x, lambda x: A @ x, lambda x: A)
    optimizer.optimize(x0)
    opt_val = optimizer.opt_val
    opt_sol = optimizer.opt_sol
    print(opt_val, opt_sol)
