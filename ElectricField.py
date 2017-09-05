# Electrostatic Force
Fe = (K * |q1 * q2| )/ pow(r,2) [Newton]
    # Fe : Electrostatic force
    # K : Electric constant = 9 * pow(10,9)
    # q1, q2 : charges
    # r : distance between charges
Fe = Q * E
=> E = Fe / Q

# Electric field : amount of force per charge
E = "Electric field"
E != Fe # Electric field is not Electric Force
E = Fe / Q [Newton / coulomb] # Q : charge

# E is a property on the charges
q1 = "charge 1"
q1.E

# When E of a charge q1 is applied on a charge q2 then Fe appears
q2 = "charge 2"
if q2.IsOnE(q1.E):
    q2.Fe[q1] = E * q2 [Newton]

# Direction of Fe, if the charges are different they atract
if q1.charge == "positive": # repel
    if q2.charge == "positive": # repel
        Fe.direction = E.direction
    else if q2.charge == "negative": # atract
        Fe.direction = -(E.direction)
else if q1.charge == "negative": # atract
    if q2.charge == "positive": # atract
        Fe.direction = E.direction
    else if q2.charge == "negative": # repel
        Fe.direction = -(E.direction)

# Magnitude of E
E = Fe / q2 = k ((q1 * q2) / pow(r,2)) / q2 [Newton / coulomb]# elemintate q2
|E1| = (k * q1) * pow(r,2) # E created by q1, r is distance from point to charge

# Escalar
f(X,Y,Z) # is different depending on values
temperature
# Vectorial
speed