def is_multiple_of_4(n):
    """Return True if n is a multiple of 4; False otherwise."""
    return n % 4 == 0


def last_prime(m):
    """Return the largest prime number p that is less than or equal to m.
    You might wish to define a helper function for this.
    You may assume m is a positive integer."""
    i = m
    while i > 1:
        if isPrime(i):
            break
        i = i - 1
    return i

# Check if a number is a prime or not.
def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def quadratic_roots(a, b, c):
    """Return the roots of a quadratic equation (real cases only).
    Return results in tuple-of-floats form, e.g., (-7.0, 3.0)
    Return "complex" if real roots do not exist."""
    d = (b**2) - (4*a*c)
    if d < 0:
        return "complex"
    sol1 = (-b - d**0.5) / (2*a)
    sol2 = (-b + d**0.5) / (2*a)
    results = (float(sol1.real), float(sol2.real))
    return results


def new_quadratic_function(a, b, c):
    """Create and return a new, anonymous function (for example
    using a lambda expression) that takes one argument x and
    returns the value of ax^2 + bx + c."""
    result = lambda x: a*x**2 + b*x + c
    return result


def perfect_shuffle(even_list):
    """Assume even_list is a list of an even number of elements.
    Return a new list that is the perfect-shuffle of the input.
    Perfect shuffle means splitting a list into two halves and then interleaving
    them. For example, the perfect shuffle of [0, 1, 2, 3, 4, 5, 6, 7] is
    [0, 4, 1, 5, 2, 6, 3, 7]."""
    length = len(even_list)
    result = []
    if length == 0:
        return result
    half = int(length/2)
    list1 = even_list[0:half]
    list2 = even_list[half:]
    for i in range(half):
        result.append(list1[i])
        result.append(list2[i])
    return result


def list_of_3_times_elts_plus_1(input_list):
    """Assume a list of numbers is input. Using a list comprehension,
    return a new list in which each input element has been multiplied
    by 3 and had 1 added to it."""
    result = [3*x+1 for x in input_list]
    return result


def quadruple_vowels(text):
    """Return a new version of text, with all the vowels quadrupled.
    For example:  "The *BIG BAD* wolf!" => "Theeee *BIIIIG BAAAAD* woooolf!".
    For this exercise assume the vowels are
    the characters A,E,I,O, and U (and a,e,i,o, and u).
    Maintain the case of the characters."""
    vowels = "AaEeIiOoUu"
    length = len(text)
    index = 0
    while index < length:
        char = text[index]
        if char in vowels:
            text = text[:index+1] + char + char + char + text[index+1:]
            index = index + 3
            length = length + 3
        index = index + 1
    return text


def count_words(text):
    """Return a dictionary having the words in the text as keys,
    and the numbers of occurrences of the words as values.
    Assume a word is a substring of letters and digits and the characters
    '-', '+', '*', '/', '@', '#', '%', and "'" separated by whitespace,
    newlines, and/or punctuation (characters like . , ; ! ? & ( ) [ ] { } | : ).
    Convert all the letters to lower-case before the counting."""
    text = text.lower()
    result = dict()
    characters = ['-', '+', '*', '/', '@', '#', '%', "'"]
    word = ''
    for char in text:
        if char.isdigit() or char.isalpha() or char in characters:
            word = word + char
        else:
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
            word = ''
    if word in result:
        result[word] += 1
    else:
        result[word] = 1
    if '' in result:
        del result['']
    return result



class Polygon:
    """Polygon class.  See the spec web page for details."""
    def __init__(self, n_sides, lengths=None, angles=None):
        self.n_sides = n_sides
        self.lengths = lengths
        self.angles = angles

    def is_rectangle(self):
        """ returns True if the polygon is a rectangle,
        False if it is definitely not a rectangle, and None
        if the angle list is unknown (None)."""
        if self.n_sides != 4:
            return False
        if self.lengths is None and self.angles is None:
            return None
        side_check = None
        angle_check = None
        if self.lengths is not None:
            side_check = True
            if (self.lengths[0] != self.lengths[2]
                or self.lengths[1] != self.lengths[3]):
                side_check = False
        if self.angles is not None:
            angle_check = True
            for i in range(4):
                if self.angles[i] != 90:
                    angle_check = False
        if self.angles is not None:
            if angle_check:
                return True
        else:
            if side_check:
                return None
        return False

    def is_rhombus(self):
        if self.n_sides != 4:
            return False
        if self.lengths is None and self.angles is None:
            return None
        side_check = None
        angle_check = None
        if self.lengths is not None:
            side_check = True
            side_length = self.lengths[0]
            for i in range(3):
                if self.lengths[i+1] != side_length:
                    side_check = False
        if self.angles is not None:
            angle_check = True
            if (self.angles[0] != self.angles[2]
                or self.angles[1] != self.angles[3]):
                angle_check = False
        if self.lengths is not None:
            if side_check:
                return True
        else:
            if angle_check:
                return None
        return False

    def is_square(self):
        if self.n_sides != 4:
            return False
        if self.lengths is None and self.angles is None:
            return None
        side_check = None
        angle_check = None
        if self.angles is not None:
            angle_check = True
            for i in range(4):
                if self.angles[i] != 90:
                    angle_check = False
        if self.lengths is not None:
            side_check = True
            side_length = self.lengths[0]
            for i in range(3):
                if self.lengths[i+1] != side_length:
                    side_check = False
        if ((side_check and angle_check is None) or
            (angle_check and side_check is None)):
            return None
        if side_check and angle_check:
            return True
        return False

    def is_regular_hexagon(self):
        if self.n_sides != 6:
            return False
        if self.lengths is None and self.angles is None:
            return None
        side_check = None
        angle_check = None
        if self.angles is not None:
            angle_check = True
            for i in range(6):
                if self.angles[i] != 120:
                    angle_check = False
        if self.lengths is not None:
            side_check = True
            side_length = self.lengths[0]
            for i in range(5):
                if self.lengths[i+1] != side_length:
                    side_check = False
        if ((side_check and angle_check is None) or
            (angle_check and side_check is None)):
            return None
        if side_check and angle_check:
            return True
        return False

    def is_isosceles_triangle(self):
        if self.n_sides != 3:
            return False
        if self.lengths is None and self.angles is None:
            return None
        side_check = None
        angle_check = None
        if self.angles is not None:
            angle_check = True
            if (self.angles[0] != self.angles[1]
                and self.angles[1] != self.angles[2]
                and self.angles[0] != self.angles[2]):
                angle_check = False
        if self.lengths is not None:
            side_check = True
            if (self.lengths[0] != self.lengths[1]
                and self.lengths[1] != self.lengths[2]
                and self.lengths[0] != self.lengths[2]):
                side_check = False
        if side_check or angle_check:
            return True
        return False

    def is_equilateral_triangle(self):
        if self.n_sides != 3:
            return False
        if self.lengths is None and self.angles is None:
            return None
        side_check = None
        angle_check = None
        if self.angles is not None:
            angle_check = True
            for i in range(3):
                if self.angles[i] != 60:
                    angle_check = False
        if self.lengths is not None:
            side_check = True
            length = self.lengths[0]
            for i in range(2):
                if self.lengths[i+1] != length:
                    side_check = False
        if side_check or angle_check:
            return True
        return False

    def is_scalene_triangle(self):
        if self.n_sides != 3:
            return False
        if self.lengths is None and self.angles is None:
            return None
        side_check = None
        angle_check = None
        if self.angles is not None:
            angle_check = True
            if (self.angles[0] == self.angles[1]
                or self.angles[1] == self.angles[2]
                or self.angles[0] == self.angles[2]):
                angle_check = False
        if self.lengths is not None:
            side_check = True
            if (self.lengths[0] == self.lengths[1]
                or self.lengths[1] == self.lengths[2]
                or self.lengths[0] == self.lengths[2]):
                side_check = False
        if side_check or angle_check:
            return True
        return False
