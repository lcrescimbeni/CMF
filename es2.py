import math

class Particle:
    """ Class describing a Particle"""
  def __init__(self, name, mass, charge, momentum=0.):
    """Arguments
        -name of the particle
        -mass (in Mev/c^2)
        -charge (in e)
        -momentum [optional] in (Mev/c)"""
        self.name = name
        self.mass = mass """dobbiamo proteggere massa e carica, facciamole diventare proprieta' read only"""
        self.charge = charge
        self.momentum = momentum """Qui chiamo il setter della properties, se metto un valore non valido il programma stampa il 
        messaggio di errore, se il valore e' fisicamente amissibile sto inizializzando la variabile"""
        
 def print_info(self):
    "Print Particle info in a nice, formatted way"""
    message = 'Particle "{}": '
    message += 'mass = {} MeV/c^2, charge = {} e, momentum = {} Mev/c'
    print(message.format(self.name, self.mass, self.charge, self.momentum)
 
 """definendo solo le property ho reso le variabili read only, basta non definire la funzione setter"""
 @property
 def mass(self):
    return self._mass
    
 @property
 def charge(self):
    return self._charge
   
 @property
 def momentum(self):
    return self._momentum """Lo rendo privato con l'underscore, o almeno dico all'utente che non andrebbe modificato"""
    
 @momentum.setter
  def momentum(self, value):
     if(value < 0):
        print ('Cannot set the momentumlue inferior to zero')
     else:
     self._momentum = value
 
   
 @property """i due comandi con la chiocciola permettono di usare le funzioni senza doverle chiamare ogni volta, e' in grado di riconoscere
 cosa vuoi fare e reagisc di conseguenza, se c'e' un assegnamento uso set, se voglio vedere lo chiamo senza assegnamento, basta il punto per
 chiamare"""
 def energy(self)
     return math.sqrt((self.momentum*LIGHT_SPEED)**2 + (self.mass * LIGHT_SPEED**2)**2)
 
 @energy.setter
 
 def set_energy(self, energy):
     if(value < self.mass):
        print ('Cannot set the energy to a value inferior to zero')
        print('The momentum will be set to zero')
        self._momentum = 0.
     else:
     self.momentum = math.sqrt(energy**2 - (self.mass * LIGHT_SPEED**2)**2)/LIGHT_SPEED**2)
 
 @property
    def beta(self):
        if not (self.energy > 0.):
            return 0.
         else:
            return LIGHT_SPEED * self.momentum/self.energy
            
  @beta.setter
  def beta(self, value):
      if(value <0.) or (value >1.):
        print('Beta must be in the [0., 1.] range')
        return
      if (not (value < 1.)) and (self.mass > 0.) :
          print(' Only massless particle can travel at Beta = 1!')
          return
      self.momentum = LIGHT_SPEED * value * self.mass / math.sqrt(1 - value**2)
   
   class Proton(Particle):
      """Class describing a Proton, classe figlia della classe madre Particle"""
      
          NAME = 'Proton' """Le definisco fuori e le chiamo con un nome tutto in maiuscolo per dire che sono costanti fissate"""
          MASS = 938 #Mev / c^2
          CHARGE = +1 #e
      
      
      def __init__(self, momentum =0.):
          Particle.__init__(self, self.NAME, self.MASS, self.CHARGE,momentum) """eredita tutte le funzioni di Particle"""
          """Si puo usare la notazione super() al posto di
          Particle e togliere il self dal primo argomento per scrivere la stessa cosa, questo fa in modo che il programma funzioni
          anche se cambio il nome della classe madre"""
          
    class Alpha(Particle):
      """Class describing un alpha,classe figlia della classe madre Particle """
      
          NAME = 'Alpha'
          MASS = 938*4 #Mev/ c^2
          CHARGE = +2 #e
      
      
      def __init__(self, momentum =0.):
          super().__init__(self.NAME, self.MASS, self.CHARGE,momentum) 
     
 if _name_ = '_main_': """fa le cose scritte qui solo se il programma e' il principale, se usassi questo come un modulo
 da importere, tutto questo pezzo non partirebbe"""
    particle = Particle('test_particle', mass=10., charge=2., momentum=100.) """Roba per testare, forse e' il caso di 
    implementarlo con argparse in mod da poter definire le costanti modificabili da terminale"""
    particle.print_info()
    proton = Proton (200.)
    proton.print_info()
    proton
        
