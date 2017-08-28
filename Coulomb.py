# This effects comes when you rub the bloon against the head
# the the bloon gains electrons
Triboelectric.effect = StaticBetween(Head, Bloon)

Atom = Neutrons + protons
    protons.Charge = positive
    electrons.Charge = negative
    neutron.Charge = null

e = protons.Charge
-e = electron.Charge

Charge.Unit = coulomb = 6.24 * pow(10,18) * e
# then based on coulomb definition
e = 1.6 * pow(10,-19) * coulomb

# Coulom's Law
# If I have 2 charges (q1, q2), separated by r distance
# then the magnitude of the force is
# proportional to the magnitude of the product of the charges

# Electrostatic Force
Fe = (K * |q1 * q2| )/ pow(r,2) [Newton]
    # Fe : Electrostatic force
    # K : Electric constant = 9 * pow(10,9)
    # q1, q2 : charges
    # r : distance between charges
