caja = [
    (500,0),
    (200,0),
    (100,0),
    (50,1),
    (20,4),
    (10,8),
    (5,2),
    (2,5),
    (1,4),
    (0.50,0),
    (0.20,0),
    (0.10,1),
    (0.05,2),
    (0.02,3),
    (0.01,1)
]

total_caja=234.27

precio=17.5
pagado=[0,0,0,0,0,1,1,0,2,1,0,0,0,0,0]

total_pagado=0

for i in range(15):
    total_pagado+=pagado[i]*caja[i][0]

if (total_pagado==precio):
    print("Se ha pagado de forma corecta")
elif tota_pagado<precio:
    print("Falta dinero")
else
    cambio=total_pagado-precio
    print("Debo devolver "+str(cambio))
    desglose_cambio=[]
    for i in range(15):
        cantidad= cambio/caja[i][0]