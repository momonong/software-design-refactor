package movierental;

public class Regular extends Movie {

    public Regular(String title) {
        super(title);        
    }

    public double getAmount(double amounts, Rental rental) {
        amounts += 2;
        if (rental.getDaysRented() > 2)
            amounts += (rental.getDaysRented() - 2) * 1.5;
        return amounts;
    }
}