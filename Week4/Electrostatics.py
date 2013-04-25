def pointPotential(X, Y, q, posx, posy):
    #Returns electric potential due to given charge
    k = 8.9875517873681764*(10**9) #N m^2 C^-2
    Vxy = (k*q/((X - posx)**2 + (Y - posy)**2)**(1/2.)) 
    return Vxy

def dipolePotential(X, Y, q, d):
    #returns the dipole potential 
    k = 8.9875517873681764*(10**9) #N m^2 C^-2
    Vxy = (k*q/(X**2 + (Y - d)**2)**(1/2.)) + (k*q/(X**2 + (Y + d)**2)**(1/2.))
    #Uxy = -((k*q/(Y**2 + (X - d)**2)**(1/2.)) + (k*q/(Y**2 + (X + d)**2)**(1/2.)))
    return Vxy #+ Uxy
