
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
from matplotlib import pyplot as plt



class ProbabilityDensityFunction(InterpolatedUnivariateSpline):

    """Class describing a probability density function.
    """

    def __init__(self, x, y):
        """Constructor.
        """
        InterpolatedUnivariateSpline.__init__(self, x, y)
        ycdf = np.array([self.integral(x[0], xcdf) for xcdf in x])
        self.cdf = InterpolatedUnivariateSpline(x, ycdf)
        
        # a=np.unique(ycdf)
        # print(ycdf.shape, a.shape)
        """Se ycdf non avesse valori identici, la lumghezza di a sara' uguale alla lunghezza di ycdf. Invece vedo che hanno una lunghezza diversa. Posso scrivere np.diff(ycdf) per stampare le differenze relative tra gli elementi contigui dell'array, e se lo stampo vedo che tutti gli ultimi elementi di ycdf sno uguali perche' li' la gaussiana e' piccola e sono tutti cosi vicini da essere uguali.
        Ora non posso banalmente sotituire a ad ycdf perche' x e a avrebbero lunghezza divera, devo fare in modo che abbiano lunghezze uguali.
        """
        #Need to make sure that the vector I am passing to the ppf spline as the
        # x values has no duplicates --- and need to filter the y accordingly
        """ In questo modo io creao un array _x senza valori doppi, np.unique mi ritorna il vettore senza valori doppi e un array di indici che mi dice i valori che non sono stati eliminati _i. in questo modo io posso usare gli indici _i per filtrare i valori di y eliminando i valori corrispondenti a queeli che np.unique ha tolto da ycdf.
        """
        _x,_i = np.unique(ycdf, return_index=True)
        _y = x[_i]
        self.ppf = InterpolatedUnivariateSpline(_x, _y)
        #self.ppf = InterpolatedUnivariateSpline(ycdf, x) Quella non filtrata

    def prob(self, x1, x2):
        """Return the probability for the random variable to be included
        between x1 and x2.
        """
        return self.cdf(x2) - self.cdf(x1)

    def rnd(self, size=1000):
        """Return an array of random values from the pdf.
        """
        return self.ppf(np.random.uniform(size=size))

    def test_gauss(mu=0., sigma=1., support=10., num_points=500):
        """Unit test with a gaussian distribution. Support perche' per una gaussiana tutti i punti stanno entro 5 sigma (99%).
           ne metto 10 per sicurezza, la probabilita' che un punto stia a piu' di 10 sigma dalla media e' ridicolmente piccola.
        """
        x= np.linspace(-support * sigma + mu, support * sigma + mu, num_points)
        y= norm.pdf(x, mu, sigma)
        """funzione di numpy per la gaussiana
        """
        pdf= ProbabilityDensityFunction(x,y)
        """ questo in teoria dovrebbe funzionare ma non funziona, almeno che non corregga nel costruttore come ho fatto sopra togliendo i valori doppi da ycdf
        """
        plt.figure('pdf')
        plt.plot(x, pdf(x))
        plt.xlabel('x')
        plt.ylabel('pdf(x)')

        plt.figure('cdf')
        plt.plot(x, pdf.cdf(x))
        plt.xlabel('x')
        plt.ylabel('cdf(x)')

        plt.figure('ppf')
        q = np.linspace(0., 1., 250)
        plt.plot(q, pdf.ppf(q))
        plt.xlabel('q')
        plt.ylabel('ppf(q)')

        plt.figure('Sampling')
        rnd = pdf.rnd(1000000)
        ydata, edges, _ = plt.hist(rnd, bins=200)
        """ Inserire  un _ come nome della variabile restituite indica che non mi interessa nulla di quela variabile. edges sono i bordi dei bin (n+1). Mi serve il valor medio del bin per fittare l'istogramma
        """
        #Mi serve il valor medio. Traslo un vettore eliminando il primo elemento
        # e uno togliendo l'ultimo, sommandoli ottengo la somma di elementi
        #contigui, cosi' prendo il valor medio di ogni bin
        xdata= 0.5 * (edges[1:] + edges [-1])

        def f(x, C, mu, sigma):
            return C* norm.pdf(x, mu, xigma)
        
        popt, pcov = curve_fit(, xdata, ydata)
        _x = np.linspace(-10, 10, 500)
        _y = f(_x, *popt)
        plt.plot(_x, _y)

        # Ho alcuni bin vuoti, se non li levo il chi2 diverge
        mask = ydata >0 
        chi2 = sum((( ydata[mask]  -f(xdata[mask], *popt)) / np.sqrt(ydata[mask]))**2.)
        """ Radice quadrata di ydata come errore, verrebbe da pensare ad uma poissoniana ma non lo e' perche' io ho fissato il numero di bin e il numero di eventi, se io so quanti oggetti ci sono in n-1 bin so quanti sono gli elementi dell'n-esimo bit. Questa e' una multinomiale, non una poissoniana. Pero' con un cosi alto numero di bin piu' o meno viene una radice quadrata. Ho 200 bin, l'errore sara' radice quadrata di 2n percio' mi aspetto 200 +- 20.
        """
        nu = mask.sum() - 3
        sigma = np.sqrt(2*nu)
        """ Valori da conforntare, il valore del mio chi2 e' simile a questo significa che il mio generatore e' buono.
        """
    


if __name__ == '__main__':
    test_gauss()
    pyplot.show
    
    
