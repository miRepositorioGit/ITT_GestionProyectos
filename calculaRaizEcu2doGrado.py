#!/usr/bin/python
# calculaRaizEcu2doGrado.py
# Calcula la raices de una ecuación de la forma ax^2+bx+c=0
#
# Coeficientes an0 estan representados por la lista an0=[a,b,c],
# donde: {a,b,c} pertenece a los Reales y an0 <>0.
#
# Se calcula el discriminante = b^2 - 4ac.
#
# Si, discriminante > 0. Entonces CASO I. Donde, las raices son reales distintas
# y conjugadas. (x1,x2) = -b/2a +- ((discriminante)^1/2)/2a
#
# Si, discriminante = 0. Entonces CASO II. Donde, la raiz real es tangente
# a la recta en X. (x1,x2) = -b/2a
#
# Si, dicriminante < 0. Entonces CASO III. Donde, las raices son imaginarias conjugadas
# y conjugadas. (x1,x2) = -b/2a +- i ((discriminante)^1/2)/2a

#
# fuentes:
# http://docs.python.org.ar/tutorial/3/datastructures.html
#
# Computación científica con Python para módulos de evaluación continua en asignaturas de ciencias aplicadas
# http://webs.ucm.es/info/aocg/python/modulos_cientificos/numpy/index.html
#
# Ecuaciones de Segundo Grado - by xassiz
# https://foro.elhacker.net/scripting/python_ecuaciones_de_segundo_grado_by_xassiz-t284796.0.html
#
# Números complejos con Python
# https://relopezbriega.github.io/blog/2015/10/12/numeros-complejos-con-python/
#
# ecuaciones de segundo grado aplicación para android Inizer Creations

# pendiente:
# 30 marzo 2019 corregir el calcúlo del complejo hacer uso del cmath
# 30 marzo 2019 no hace el calcúlo con def complex.
# 06 abril 2019 actualizar clase con métodos.
# 06 abril 2019 incluir método de verificarVector de coeficientes
import math
import cmath

# Método estático, define coeficientes

# CASO I. Donde, las raices son imaginarias conjugadas. Discriminante < 0.
menor_A_0 = [1,2,3];    # x1 = -1.0 + 1.4142i,  x2 = 1.0 - 1.4142i   Discriminante = -8.

# CASO II. Donde, las raiz es tangente. Discriminante == 0.
igual_A_0 = [2,-4,2];   # x1 =  1, x2 = 1   Discriminante = 0.

# CASO  III. Donde, las raices son reales distintas. Discriminante > 0.
mayor_A_0 = [-1,4,3];   # x1 = 4.6458, x2 = -0.6458   Discriminante = 28


# Ecuación de segundo grado de la forma x*x + 7x + 12 = 0
mm_mx_n = [1,7,12];
# forma ax^2+bx=0 436 Baldor

# forma ax^2+c=0 435 Baldor
axc =  [2,0,-18];   # f(x) = 2x^2 - 18 = 0  raices = [3, -3]
axc1 = [1,0,-2];    # f(x) =  x^2 - 2  = 0  raices = [1.4142135623730951, -1.4142135623730951]
axc2 = [1,0,-9];
axc3 = [3,0,-48];
axc4 = [1,0,-18];
axc5 = [4,0,-144];
axc1J = [2,0,32];   # f(x) = 2x^2 + 32 = 0, raices = [4i, -4i]
axc2J = [7,0,14];   # f(x) = 7x^2 + 14 = 0, raices = [1.4142135623730951j, -1.4142135623730951j]
axc3J = [1,0,7];


print('calculaRaizEcu2doGrado.py');
print('\n');
print('CASO     DISCRIMINANTE');
print('III      Discriminante >  0 ');
print(' II      Discriminante == 0 ');
print('  I      Discriminante <  0 ');
print('\n');

def discriminante(args):
    caso = 0;
    resultado = [];

    minuendo = (args[1])*(args[1]);       # b^2
    sustraendo = 4*args[0]*args[2];       # 4*a*c
    resultado = minuendo - sustraendo;    # b^2 - 4*a*c

    if  resultado > 0 :  # CASO III. Donde, las raices son reales.
        caso = [3,resultado];
    if  resultado == 0 : # CASO II.  Donde, las raiz tangente al eje X.
        caso = [2,resultado];
    if resultado < 0 : # CASO I.     Donde, las raices son imaginarias.
        caso = [1,resultado];

    return caso;


# retorna la raiz real
# @param args0[]= {a,b,c} coeficientes del polinomio
# Calcula el real, donde la función hace tangente

def raizReal(args0):
    raiz = []
    numerador = (args0[1]*-1); # -b
    denominador = 2*args0[0];  # 2*a
    raiz = (numerador/denominador);
    return [raiz,raiz];

# retorna la raices reales distintas
# @param args0[]= {a,b,c} coeficientes del polinomio
# Calcula las raices reales de la función.

def raicesRealesDistintas(args1):
    raicesReales = [];

    # calcula el factor_1 = -b / 2a
    numerador = (args1[1]*-1);          # -b
    denominador = 2*args1[0];           # 2*a
    factor_1 = numerador/denominador;   # -b / 2a

    # calcula el discriminante y su raiz
    minuendo = numerador * numerador;       # b^2
    sustraendo = 4*args1[0]*args1[2];       # 4*a*c
    resultado = minuendo - sustraendo;      # b^2 - 4*a*c
    raizDiscriminante = (math.sqrt(resultado) / denominador );  # ((discriminante)^1/2)/2a

    # calcula raicesReales = -b / 2a +- ((discriminante)^1/2)/2
    raiz_1 = factor_1 + raizDiscriminante;
    raiz_2 = factor_1 - raizDiscriminante;

    raicesReales = [raiz_2,raiz_1];
    return raicesReales;

# retorna la raices complejas
# @param args0[]= {a,b,c} coeficientes del polinomio
# Calcula las raices complejas de la función.

def raicesComplejasConjugadas(args1):
    raicesComplejas = [1,1];

    # calcula el factor_1 = -b / 2a
    numerador = (args1[1])*(-1);            # -b
    denominador = float(2*args1[0]);        # 2*a
    parteReal = numerador/denominador;      # -b / 2a

    # calcula el discriminante
    minuendo = args1[1]**2;                 # b^2
    sustraendo = 4*args1[0]*args1[2];       # 4*a*c
    resultado = (minuendo - sustraendo);    # (b^2 - 4*a*c)

    parteImaginaria = (math.sqrt(-(resultado))) / (2*args1[0])

    x1=complex(parteReal,parteImaginaria);  # obtiene número complejo

    raicesComplejas = [x1, (x1)*(-1)];
    return raicesComplejas;


# Polinomio de la forma: x^2 + mx + n = 0
# -(m/2)+- math.sqrt( (mm^2 /4) - n )
def xx_mx_n(args1):
    raices = [];

    m  = args1[1];
    mm = args1[1]**2; # m*m
    n  = args1[2];

    factor_1 = (-1)*(m/2)
    factor_2 = math.sqrt( (mm/4) - n )
    raiz_1 = factor_1 + factor_2;
    raiz_2 = factor_1 - factor_2;

    raices = [raiz_1,raiz_2];
    return raices;

# Polinomio de la forma: ax^2 + c = 0
#
def ax2_c(args1):
    raices = [];
    raicesComplejas = [];

    c = args1[2];
    a = args1[0];

    if c > 0:
        # imaginarias
        print(" ")
        print("\t",args1[0],"x^2", "+", args1[2], "= 0");

        parteImaginaria = math.sqrt(  c/a )

        x1=complex(0,parteImaginaria);  # obtiene número complejo

        raiz_1 = x1.imag*1j
        raiz_2 = x1.imag*1j

        [x,y] = cmath.polar(complex(raiz_1, raiz_2));

        print("\t", "Cartesianas: ",[x,y]);

        # comprobación ax^2 + c = 0
        #factor_1 = x**2;
        #factor_2 = y**2;
        #factor_3 = c;

        #factor = factor_1 - factor_3;
        #resultadoX1 = round(factor);

        #factor = factor_2 - factor_3;
        #resultadoX2 = round(factor);

        #if(resultadoX1 == 0):
        #    raicesComplejas = [raiz_1,raiz_2,resultadoX1];

        #if(resultadoX2 == 0):
        #    raicesComplejas = [raiz_1,raiz_2,resultadoX2];

        raicesComplejas=[raiz_1,raiz_2];

        return raicesComplejas;

    else:
        print("reales")
        raiz_1 = math.sqrt( -1 * (c/a) );

        # comprobación
        factor_1 = (a) * (raiz_1**2) ;
        factor_2 = c;
        resultado = factor_1 + factor_2;

        raicesReales = [raiz_1,-1 * raiz_1, round(resultado)];

        return raicesReales;

#   imprime resultados
# @param args0[0] tipo de polinomio.
# @param args1[1] magnitud del discriminante.
# @param args1[2] magnitud parte real
# @param args1[3] magnitud parte imaginaria

    def imprimeResultado(arg0):
        forma = args0[0];
        discriminante = args0[1];
        raiz_1  = args0[2];
        raiz_2  = args0[3];


try:
    #  Calcula el discriminante e imprime el CASO
    #print("\t CASO, Discriminante")
    print("\t  III", discriminante(mayor_A_0));
    #print("\t   II", discriminante(igual_A_0));
    #print("\t    I", discriminante(menor_A_0));

    # calcula las raices reales
    #print("\t Raiz III",raicesRealesDistintas(mayor_A_0));

    # calcula la raiz
    #print("\t Raiz  II",raizReal(igual_A_0));

    # calcula las raices imaginarias
    print("\t Raiz   I",raicesComplejasConjugadas(menor_A_0));

    #print("\t", mm_mx_n , xx_mx_n(mm_mx_n) );

    #print("\t", "Complejas:   ",ax2_c(axc2J) );

except:
    print ("Hay un error....! ")