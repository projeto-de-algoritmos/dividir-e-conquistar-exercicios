class Solution(object):
    def kthLargestNumber(self, nums, k):
        nums = [int(num) for num in nums]  # Converte strings para inteiros
        # Encontra o k-ésimo maior número e o converte de volta para string
        return str(self.findkth(nums, len(nums)-k))

    def findmom(self, array):
        # Se o array tiver 5 ou menos elementos, ordena e retorna a mediana
        if len(array) <= 5:
            array.sort()
            return array[len(array)//2]
        else:
            # Caso contrário, divide o array em grupos de 5 e encontra a mediana de cada grupo
            medians = []
            for i in range(0, len(array), 5):
                group = array[i:i+5]
                medians.append(self.findmom(group))
            # Encontra a mediana das medianas recursivamente
            return self.findmom(medians)
    
    def findkth(self, array, k):
        # Se o array tiver 5 ou menos elementos, ordena e retorna o k-ésimo elemento
        if len(array) <= 5:
            array.sort()
            return array[k]  # Retorna o k-ésimo menor número
        else:
            # Caso contrário, encontra a mediana das medianas
            median = self.findmom(array)
        # Particiona o array em três partes: menor que, igual a, e maior que a mediana
        L, M, R = [], [], []
        for i in range(len(array)):
            if array[i] < median:
                L.append(array[i])
            elif array[i] > median:
                R.append(array[i])
            else:
                M.append(array[i])
        # Encontra o k-ésimo elemento na parte apropriada recursivamente
        if k < len(L):
            return self.findkth(L, k)
        elif k < len(L) + len(M):
            return M[0]
        else:
            return self.findkth(R, k-len(L)-len(M))
    