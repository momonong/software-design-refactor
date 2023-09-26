package movierental;

public class Childrens extends Movie{

    public Childrens(String title) {
        super(title);        
    }

    public double getAmount(double amounts, Rental rental) {
        amounts += 1.5;
        if (rental.getDaysRented() > 3) 
            amounts += (rental.getDaysRented() - 3) * 1.5;
        return amounts;
    }
}