def my_max(a:int, b:float) -> int:
    if a>=b: 
        return a    
    else:
        return b

a: int = 6.5
y: float = 7.5
z: int = my_max(a, y)
print(z)

