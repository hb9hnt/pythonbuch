#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

from math import sqrt
from random import randint

class Sparse():
    
    def __init__(self, dimension, nonzero_components_values, nonzero_components_indexes):
        '''
        Constructor
        '''
        self.__dimension = dimension
        self.__nonzero_components_values = nonzero_components_values
        self.__nonzero_components_indexes = nonzero_components_indexes
        
    def get_dimension(self):
        return self.__dimension

    def get_nonzero_components_values(self):
        return self.__nonzero_components_values

    def get_nonzero_components_indexes(self):
        return self.__nonzero_components_indexes

    def set_nonzero_component(self, value, i):
        if i < 1 or i > self.__dimension:
            print("Fehler: nicht gültiges Index.")
            return
        
        if i in self.__nonzero_components_indexes:
            j = self.__nonzero_components_indexes.index(i)
            self.__nonzero_components_values[j] = value
        else:
            self.__nonzero_components_values.append(value)
            self.__nonzero_components_indexes.append(i)
    
    def print_sparse(self):
        print("Dimension: ", self.__dimension,"\t Nonzero entries: ", end = "")
        print("[ ", end = "")
        for i in range(len(self.__nonzero_components_values)):
            print(self.__nonzero_components_indexes[i],":", self.__nonzero_components_values[i], sep = "", end = "")
            if i != len(self.__nonzero_components_values)-1:
                print(" , ", end="")
        print(" ]")
        
    def extended_print_sparse(self):
        print("[", end = "")
        for i in range(self.__dimension):
            if i+1 in self.__nonzero_components_indexes:
                j = self.__nonzero_components_indexes.index(i+1)
                print("{0:>5}".format(self.__nonzero_components_values[j]), end = "")
            else:
                print("{0:>5}".format(0), end = "")
        print("   ]")
            
    def modulus(self):
        m = 0
        for i in range(len(self.__nonzero_components_values)):
            m += self.__nonzero_components_values[i]**2
        return sqrt(m)
    
    def clean(self):
        while 0 in self.__nonzero_components_values:
            j = self.__nonzero_components_values.index(0)
            del self.__nonzero_components_indexes[j]
            self.__nonzero_components_values.remove(0)
        
        indexes = self.__nonzero_components_indexes
        values = self.__nonzero_components_values
        sorted_lists = sorted(zip(indexes, values), key=lambda x: x[0])
        indexes, values = [[x[i] for x in sorted_lists] for i in range(2)]
        self.__nonzero_components_indexes = indexes
        self.__nonzero_components_values = values
    
    def multiply(self, factor):
        s_dim = self.__dimension
        s_v = self.__nonzero_components_values[:]
        s_i = self.__nonzero_components_indexes[:]
        
        s_v = [x * factor for x in s_v]
        s = Sparse(s_dim,s_v,s_i)
        return s
        
def add_sparse(a, b):
    a_dim = a.get_dimension()
    b_dim = b.get_dimension()
    a_v = a.get_nonzero_components_values()
    b_v = b.get_nonzero_components_values()
    a_i = a.get_nonzero_components_indexes()
    b_i = b.get_nonzero_components_indexes()
    
    if a_dim != b_dim:
        print("Fehler: die zwei Vektoren haben verschiedene Dimensionen!")
        return
    
    s_dim = a_dim
    s_v = a_v[:]
    s_i = a_i[:]
    print(a_v)
    for i in range(len(b_i)):
        if b_i[i] in a_i:
            j = a_i.index(b_i[i])
            s_v[j] += b_v[i]
        else:
            s_i.append(b_i[i])
            s_v.append(b_v[i])
    s = Sparse(s_dim,s_v,s_i)
    s.clean()    
    print(a_v)
    return s

def dot_sparse(a,b):
    a_dim = a.get_dimension()
    b_dim = b.get_dimension()
    a_v = a.get_nonzero_components_values()
    b_v = b.get_nonzero_components_values()
    a_i = a.get_nonzero_components_indexes()
    b_i = b.get_nonzero_components_indexes()
    
    if a_dim != b_dim:
        print("Fehler: die zwei Vektoren haben verschiedene Dimensionen!")
        return
    
    p = 0
    
    for i in a_i:
        if i in b_i:
            index_a = a_i.index(i)
            index_b = b_i.index(i)
            p += a_v[index_a]*b_v[index_b]
    
    return p

def create_random_sparse(n,m,a,b):
    if n < m or a > b:
        print("Fehler: ungültige Eingaben.")
        return
    s = Sparse(n,[],[])
    for i in range(m):
        index = randint(1,n)
        value = randint(a,b)
        s.set_nonzero_component(value, index)
    return s
        

def main():
    v1 = Sparse(5,[1,-2],[2,4])
    v2 = Sparse(5,[-7,-1,9],[1,2,5])
    v3 = Sparse(5,[-7,-5,9],[1,2,5])
    print("v1: ",end="")
    v1.print_sparse()
    print("v2: ",end="")
    v2.print_sparse()
    print("v3: ",end="")
    v3.print_sparse()
    w = add_sparse(v1,v2)
    print("w=v1+v2: ",end="")
    w.print_sparse()
    u = add_sparse(v1,v3)
    print("u=v1+v3: ",end="")
    u.print_sparse()
    u.set_nonzero_component(2, 1)
    u.print_sparse()
    p = dot_sparse(v1,v1)
    print("v1*v1=",p)
    print("Betrag von v1 im Quadrat=",v1.modulus()**2)
    print("v1: ",end="")
    v1.print_sparse()
    print("v2: ",end="")
    v2.print_sparse()
    print("v1: ",end="")
    v1.extended_print_sparse()
    print("v2: ",end="")
    v2.extended_print_sparse()

    r1 = create_random_sparse(20, 3, -10, 10)
    r2 = create_random_sparse(20, 5, -10, 10)
    r3 = create_random_sparse(20, 10, -10, 10)

    print("r1= ",end="")
    r1.extended_print_sparse()
    print("r2= ",end="")
    r2.extended_print_sparse()
    print("r3= ",end="")
    r3.extended_print_sparse()
    
    print("r1*r2=",dot_sparse(r1,r2))
    print("r1*r3=",dot_sparse(r1,r3))
    print("r2*r3=",dot_sparse(r3,r2))
    
main()