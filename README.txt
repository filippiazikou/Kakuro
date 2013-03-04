Φιλιππία Ζήκου
11152006 00 019
std06019@di.uoa.gr

Arxeia:

kakuro.py -> Provlima 1. I epilogi tis eisodou kai tou algorithmou dinontai stin arxi tou programmatos kai xrisimopoiountai sa global metavlites.
README -> Provlima 1 + 2
std06019.pdf -> Provlimata 3 ws 8. 

KAKURO:

Παρακάτω φαίνονται οι χρόνοι εκτέλεσης των αλγορίθμων για διάφορες εισόδους. Για μικρή είσοδο παρατηρούμε ότι ο χρόνος είναι σχεδόν ίδιος ενώ για όταν το puzzle μεγαλώνει αργεί να βγάλει αποτελέσματα. Ο FC έχει μεγάλη διαφορά στο χρόνο εκτέλεσης από τον ΒΤ και κυρίως όταν χρησιμοποιείται με τον MRV, ο οποίος επιλέγει τη σειρά των μεταβλητών για την καλύτερη απόδοση.  

         |BT        |BT+MRV    | FC       |FC+MRV
puzzle0  |0m0.036s  |0m0.032s  |0m0.033s  |0m0.037s
puzzle1  |0m0.037s  |0m0.034s  |0m0.034s  |0m0.035s
puzzle2  |0m4.293s  |0m4.605s  |0m0.113s  |0m0.662s
puzzle3  |1m26.076s |2m55.571s |0m11.292s |0m0.270s


MAP COLORING:

Και σε αυτό το παράδειγμα παρόλο που οι διαφορές στους χρόνους εκτέλεσεις δεν είναι μεγάλες παρατηρούμε ότι ο FC σε συνδιασμό με τον MRV έχει τους καλύτερους χρόνους εκτέλεσης ενώ και ο ΜΑC είναι γρήγορος καθώς πιθανόν να επισκέπτεταί μικρότερο πλήθος κόμβων

           |FC+MRV    | MAC      |Min Conflicts
australia  |0m0.032s  |0m0.030s  |0m0.045s
usa        |0m0.038s  |0m0.123s  |0m0.045s
france     |0m0.034s  |0m0.034s  |0m0.036s
