import math
import sys
sys.setrecursionlimit(5000)
sys.modules['_decimal'] = None
import decimal
from decimal import *
from decimal import Decimal

getcontext().Emin = -10 ** 10000
getcontext().Emax = 10 ** 10000
getcontext().traps[Overflow] = 0
getcontext().traps[Underflow] = 0
getcontext().traps[DivisionByZero] = 0
getcontext().traps[InvalidOperation] = 0
getcontext().prec = 100


def add(a: int or float or Decimal, b: int or float or Decimal) -> Decimal:
    return Decimal(a) + Decimal(b)


def subtract(a: int or float or Decimal, b: int or float or Decimal) -> Decimal:
    return Decimal(a) - Decimal(b)


def multiply(a: int or float or Decimal, b: int or float or Decimal) -> Decimal:
    return Decimal(a) * Decimal(b)


def divide(a: int or float or Decimal, b: int or float or Decimal) -> Decimal:
    return Decimal(a) / Decimal(b)


def modulo(a: int or float or Decimal, b: int or float or Decimal) -> Decimal:
    return Decimal(a) % Decimal(b)


def integer_division(a: int or float or Decimal, b: int or float or Decimal) -> Decimal:
    return Decimal(a) // Decimal(b)


def exponent(a: int or float or Decimal, b: int or float or Decimal) -> Decimal:
    return Decimal(a) ** Decimal(b)


def sin(a: int or float or Decimal):
    return math.sin(a)


def cos(a: int or float or Decimal):
    return math.cos(a)


def tan(a: int or float or Decimal):
    return math.tan(a)


def asin(a: int or float or Decimal):
    return math.asin(a)


def acos(a: int or float or Decimal):
    return math.acos(a)


def atan(a: int or float or Decimal):
    return math.atan(a)


def sinh(a: int or float or Decimal):
    return math.sinh(a)


def cosh(a: int or float or Decimal):
    return math.cosh(a)


def tanh(a: int or float or Decimal):
    return math.tanh(a)


def asinh(a: int or float or Decimal):
    return math.asinh(a)


def acosh(a: int or float or Decimal):
    return math.acosh(a)


def atanh(a: int or float or Decimal):
    return math.atanh(a)


def main():
    """
    Fungsi ini dipakai untuk run program.
    :return:
    """
    print("SELAMAT DATANG KE APLIKASI KALKULATOR. BERIKUT ADALAH PETUNJUK-PETUNJUK CARA MENGGUNAKANNYA.")
    print("Fungsi add(a: int or float or Decimal, b: int or float or Decimal) dipakai untuk operasi penjumlahan antar"
          "dua bilangan. Contohnya add(5, 3) menghasilkan 5 + 3 = 8.")
    print("Fungsi subtract(a: int or float or Decimal, b: int or float or Decimal) dipakai untuk operasi pengurangan antar"
          "dua bilangan. Contohnya subtract(5, 3) menghasilkan 5 - 3 = 2.")
    print(
        "Fungsi multiply(a: int or float or Decimal, b: int or float or Decimal) dipakai untuk operasi perkalian antar"
        "dua bilangan. Contohnya multiply(5, 3) menghasilkan 5 * 3 = 15.")
    print(
        "Fungsi divide(a: int or float or Decimal, b: int or float or Decimal) dipakai untuk operasi pembagian antar"
        "dua bilangan. Contohnya divide(6, 3) menghasilkan 6 / 3 = 2.")
    print(
        "Fungsi modulo(a: int or float or Decimal, b: int or float or Decimal) dipakai untuk operasi modulo antar"
        "dua bilangan. Contohnya modulo(5, 3) menghasilkan 5 % 3 = 2.")
    print(
        "Fungsi integer_division(a: int or float or Decimal, b: int or float or Decimal) dipakai untuk operasi integer division antar"
        "dua bilangan. Contohnya integer_division(5, 3) menghasilkan 5 // 3 = 1.")
    print(
        "Fungsi exponent(a: int or float or Decimal, b: int or float or Decimal) dipakai untuk operasi pangkat antar"
        "dua bilangan. Contohnya exponent(2, 3) menghasilkan 2 ** 3 = 8.")
    print(
        "Fungsi sin(a: int or float or Decimal) dipakai untuk operasi sinus "
        "sebuah bilangan. Contohnya sin(0) menghasilkan 0.")
    print(
        "Fungsi cos(a: int or float or Decimal) dipakai untuk operasi cosinus "
        "sebuah bilangan. Contohnya cos(0) menghasilkan 1.")
    print(
        "Fungsi tan(a: int or float or Decimal) dipakai untuk operasi tangent "
        "sebuah bilangan. Contohnya tan(0) menghasilkan 0.")
    print(
        "Fungsi asin(a: int or float or Decimal) dipakai untuk operasi arcsin "
        "sebuah bilangan. Contohnya asin(0) menghasilkan 0.")
    print(
        "Fungsi acos(a: int or float or Decimal) dipakai untuk operasi arccos "
        "sebuah bilangan. Contohnya acos(0) menghasilkan 1.5707963267948966.")
    print(
        "Fungsi atan(a: int or float or Decimal) dipakai untuk operasi arctan "
        "sebuah bilangan. Contohnya atan(0) menghasilkan 0.")
    print(
        "Fungsi sinh(a: int or float or Decimal) dipakai untuk operasi sinh "
        "sebuah bilangan. Contohnya sinh(0) menghasilkan 0.")
    print(
        "Fungsi cosh(a: int or float or Decimal) dipakai untuk operasi cosh "
        "sebuah bilangan. Contohnya cosh(0) menghasilkan 1.")
    print(
        "Fungsi tanh(a: int or float or Decimal) dipakai untuk operasi tanh "
        "sebuah bilangan. Contohnya tanh(0) menghasilkan 0.")
    print(
        "Fungsi asinh(a: int or float or Decimal) dipakai untuk operasi asinh "
        "sebuah bilangan. Contohnya asinh(0) menghasilkan 0.")
    print(
        "Fungsi acosh(a: int or float or Decimal) dipakai untuk operasi acosh "
        "sebuah bilangan. Contohnya acosh(1) menghasilkan 0.")
    print(
        "Fungsi atanh(a: int or float or Decimal) dipakai untuk operasi atanh "
        "sebuah bilangan. Contohnya atanh(0) menghasilkan 0.")
    sah: bool = False
    while not sah:
        rumus: str = input("Ketikkan rumus: ")
        try:
            print(str(rumus) + " = " + str(eval(rumus)))
            sah = True
        except EOFError:
            sah = False

    print("Tekan Y untuk ya.")
    print("Tekan apapun yang lainnya untuk tidak.")
    tanya: str = input("Apakah Anda mau lanjut menggunakan kalkulator? ")
    if tanya == "Y":
        main()
    else:
        sys.exit()


if __name__ == '__main__':
    main()
