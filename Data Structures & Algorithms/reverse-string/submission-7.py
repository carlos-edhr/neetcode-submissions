class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #inicializamos variables (declaración y asignación)
        puntero_izquierdo = 0
        puntero_derecho = len(s) - 1 # [ 7, 4, 9, 1, 5] 

        while puntero_izquierdo < puntero_derecho:
          # intercambia los pares y avanza los punteros
          s[puntero_izquierdo], s[puntero_derecho] = s[puntero_derecho], s[puntero_izquierdo]
          puntero_izquierdo += 1
          puntero_derecho -= 1
          
        