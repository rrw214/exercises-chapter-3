from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        coefs_list = list(coefs)

        while len(coefs_list) > 1 and coefs_list[-1] ==0:
            coefs_list.pop()

        if len(coefs_list) ==1 and coefs_list[0] ==0:
            coefs_list = [0]
        
        self.coefficients = tuple(coefs_lsit)


    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        coefs = self.coefficients
        if isinstance(other,Number):
            return Polynomial( (coefs[0] - other,) + coefs[1:])
        if isinstance(other,Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a-b for a,b in zip(self.coefficients[:common], other.coefficients[:common]))
            coefs += tuple(-x for x in self.coefficients[common:]) + tuple(-y for y in other.coefficients[common:])
            return Polynomial(coefs)
        else:
            return NotImplemented



    def __rsub__(self, other):
        if isinstance(other, Number):
            new_coefs = (other-self.coefficients[0],)+ tuple(-x for x in self.coefficients[1:])
            return Polynomial(new_coefs)
        else:
            return NotImplemented
        
    def __mul__(self, other):
        if isinstance(other,Polynomial):
            coefs = self.coefficients
            result_dict = {}
            for a, b in enumerate(coefs):
                for c, d in enumerate(other.coefficients):
                    degree = a + c
                    coefficient = b * d
                    result_dict[degree] = result_dict.get(degree, 0) + coefficient

            max_degree = max(result_dict.keys())
            coefficients = []
            for degree in range(max_degree + 1):
                coefficients.append(result_dict.get(degree, 0))

            return Polynomial(tuple(coefficients))

        if isinstance(other,Number):
            coefs = self.coefficients
            new_coefs = tuple(other * c for c in coefs)


            return Polynomial(new_coefs)

        else:
            return NotImplemented


    def __rmul__(self, other):
        return self*other
    
    def __pow__(self, power, modulo=None):
        if isinstance(power,Integral) and power >= 0:
            result = Polynomial((1,))
            for x in range(power):
                result = result*self

        return result

    def __call__(self, x):
        coefs = self.coefficients
        total = 0
        for a,b in enumerate(coefs):
            total += b*x**a
        return total
    

