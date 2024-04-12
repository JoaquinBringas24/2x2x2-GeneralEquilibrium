class Household:
    def __init__(self, L, K, ax, ay):
        self.L = L
        self.K = K
        self.ax = ax
        self.ay = ay

    @staticmethod
    def consumption_function(x, y, alpha, beta):
        return (x ** alpha) * (y ** beta)

    def income_function(self, profits_x, profits_y, w, r):
        return w * self.L + r * self.K + self.ax * profits_x + self.ay * profits_y


class Firm:
    def __init__(self, alpha, beta, w, r):
        self.alpha = alpha
        self.beta = beta
        self.w = w
        self.r = r

    def production_function(self, L, K):
        return (L ** self.alpha) * (K ** self.beta)

    def costs_function(self, L, K):
        return self.w * L + self.r * K

    def profits_function(self, price):
        return self.costs_function() * price - self.costs_function()



