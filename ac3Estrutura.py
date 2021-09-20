from abc import ABCMeta, abstractmethod
from unittest import TestCase, main, result



class OperacaoFabrica(object):

    def criar(self, operador):
        if(operador == 'soma'):
           return Soma()
        elif (operador == 'subtracao'):
           return Subtracao()
        elif (operador == 'divisao'):
           return Divisao()
        elif (operador == 'multiplicacao'):
           return Multiplicacao()


class Calculadora (object):
    def calcular(self, n1, n2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
 
        if (operacao == None):
          return 0
        else:
          resultado = operacao.executar(n1, n2)
          return resultado
      
      
       

class Operacao():
    __metaclass__ = ABCMeta
    @abstractmethod
    def executar(self, n1, n2):
     pass


class Soma(Operacao):
     def executar(self, n1, n2):
         resultado = n1 + n2
         return resultado

class Subtracao(Operacao):
     def executar(self, n1, n2):
         resultado = n1 - n2
         return resultado

class Multiplicacao(Operacao):
      def executar(self, n1, n2):
          resultado = n1 * n2
          return resultado


class Divisao(Operacao):
      def executar(self, n1, n2):
          resultado = n1 / n2
          return resultado


class Testes(TestCase):

      def test_soma(self):
        calculadorSom = Calculadora()
        result = calculadorSom.calcular(2,3, 'soma')
        self.assertEqual(result, 5)
        

      def test_multiplicacao(self):
         calculadorMult = Calculadora()
         self.assertEqual (calculadorMult.calcular(2,5, 'multiplicacao'), 10)

      def test_divisao(self):
         calculadorDiv = Calculadora()
         self.assertEqual(calculadorDiv.calcular(4,2, 'divisao'), 2)

      def test_subtracao(self):
         calculadorSub = Calculadora()
         result = calculadorSub.calcular(2,4, 'subtracao')
         print(result)
         self.assertEqual(result, -2)

      def test_fail(self):
         calculadorfail = Calculadora()
         self.assertEqual(calculadorfail.calcular(2, 4, 'subfail'), 0)

calculador = Calculadora()
x = calculador.calcular(2,3, 'soma')
print(x)

if __name__ == '__main__':
    main()