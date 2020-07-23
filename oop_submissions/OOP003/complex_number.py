import math
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        
        
        if(type(real_part)!=int and type(real_part)!=float):
            if(type(imaginary_part)!=int and type(imaginary_part)!=float):
                raise ValueError('Invalid value for real and imaginary part')
            else:
                raise ValueError('Invalid value for real part')
        elif(type(imaginary_part)!=int and type(imaginary_part)!=float):
            raise ValueError('Invalid value for imaginary part')
    
    def __str__(self):
            if (self.imaginary_part>=0):
                return '{}+{}i'.format(self.real_part,self.imaginary_part)
            else:
                return '{}{}i'.format(self.real_part,self.imaginary_part)
       
    def __mul__(self, other):
        return ComplexNumber(self.real_part*other.real_part - self.imaginary_part*other.imaginary_part,
                       self.imaginary_part*other.real_part + self.real_part*other.imaginary_part)        
            
    def conjugate(self):
       return ComplexNumber(self.real_part,-self.imaginary_part)
       
    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)
    
    def __sub__(self, other):
        return ComplexNumber(self.real_part - other.real_part, self.imaginary_part - other.imaginary_part)
    
    def __truediv__(self,other):
        if(other.real_part ==0 and other.imaginary_part==0):
            raise ZeroDivisionError('division by zero')
            
        else:
            r=other.real_part**2+other.imaginary_part**2
            x=(self.real_part*other.real_part - self.imaginary_part*-1*other.imaginary_part)/r
            y=(self.imaginary_part*other.real_part + self.real_part*-1*other.imaginary_part)/r
            return ComplexNumber(round(x,2),round(y,2))
    
    def __eq__(self,other):
        return self.real_part==other.real_part and self.imaginary_part==other.imaginary_part 
    
    def __abs__(self):
        k=math.sqrt(self.real_part**2 + self.imaginary_part**2)
        k=round(k,3)
        return k

#xy= ComplexNumber()
#ab= abs(xy)
#print(ab)

#from complex_number import ComplexNumber
#one_plus_two_i = ComplexNumber(2,1)
#absolute_value = abs(one_plus_two_i)
#print(absolute_value)
#2.236


#"""
            
        
        
        