print("Informe as coordenadas da primeira força (F1)")
f1 =[]
f1.append(float(input("F1 - x: ")))
f1.append(float(input("F1 - y: ")))
f1.append(float(input("F1 - z: ")))


print("Informe as coordenadas da segunda força (F2)")
f2 =[]
f2.append(float(input("F2 - x: ")))
f2.append(float(input("F2 - y: ")))
f2.append(float(input("F2 - z: ")))

print("Informe as coordenadas da terceira força (F3)")
f3 =[]
f3.append(float(input("F3 - x: ")))
f3.append(float(input("F3 - y: ")))
f3.append(float(input("F3 - z: ")))

rx = f1[0] + f2[0]
ry = f1[1] + f2[1]
rz = f1[2] + f2[2]

força_resultante = [rx,ry, rz]
print("-"*30)
print( f" A força resultante no espaço 3D é :{força_resultante} ")
print(f" comoponetse individuais -> : {rx} , {ry} , {rz}")



