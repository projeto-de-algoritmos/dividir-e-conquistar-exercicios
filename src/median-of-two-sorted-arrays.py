class Solution(object):
    def findmom(self, array):
        # Se o array tiver 5 ou menos elementos, simplesmente ordenamos e retornamos a mediana
        if len(array) <= 5:
            array.sort()
            return array[len(array)//2]
        else:
            # Caso contrário, dividimos o array em grupos de 5, encontramos a mediana de cada grupo,
            # e recursivamente encontramos a mediana das medianas
            medians = [self.findmom(array[i:i+5]) for i in range(0, len(array), 5)]
            return self.findmom(medians)
    
    def findkth(self, array, k):
        # Encontramos a mediana do array
        median = self.findmom(array)
        # Dividimos o array em três partes: elementos menores que a mediana (L),
        # elementos iguais à mediana (M) e elementos maiores que a mediana (R)
        L, M, R = [], [], []
        for num in array:
            if num < median:
                L.append(num)
            elif num > median:
                R.append(num)
            else:
                M.append(num)
        # Se k está dentro do intervalo de L, procuramos o k-ésimo menor elemento em L
        if k < len(L):
            return self.findkth(L, k)
        # Se k está dentro do intervalo de L+M, retornamos a mediana
        elif k < len(L) + len(M):
            return M[0]
        # Se k está dentro do intervalo de L+M+R, procuramos o (k-len(L)-len(M))-ésimo menor elemento em R
        else:
            return self.findkth(R, k-len(L)-len(M))

    def findMedianSortedArrays(self, nums1, nums2):
        size = len(nums1) + len(nums2)
        # Se o tamanho total é par, encontramos os dois elementos do meio e retornamos a média deles
        if size % 2 == 0:
            mid1 = self.findkth(nums1+nums2, size//2 - 1)
            mid2 = self.findkth(nums1+nums2, size//2)
            return (mid1 + mid2) / 2.0
        # Se o tamanho total é ímpar, encontramos o elemento do meio e o retornamos
        else:
            return self.findkth(nums1+nums2, size//2)