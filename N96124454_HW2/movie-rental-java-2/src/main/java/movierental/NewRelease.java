package movierental;

public class NewRelease extends Movie {

    public NewRelease(String title) {
        super(title);        
    }

    public double getAmount(double amounts, Rental rental) {
        amounts += rental.getDaysRented() * 3;
        return amounts;
    }

    public int calBonus(int frequentRenterPoints, Rental rental) {
        if (rental.getDaysRented() > 1)
            frequentRenterPoints++;
        return frequentRenterPoints;
    }
}
