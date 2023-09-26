package movierental;

public class Movie {

    public static final int CHILDRENS = 2;
    public static final int NEW_RELEASE = 1;
    public static final int REGULAR = 0;

    private String _title;
    private int _priceCode;

    public Movie(String title, int priceCode) {
        _title = title;
        _priceCode = priceCode;
    }
 
    public double getAmount(double amount, Rental rental) {
        switch (_priceCode) {
            case REGULAR:
                amount += 2;
                if (rental.getDaysRented() > 2)
                    amount += (rental.getDaysRented() - 2) * 1.5;
                break;
            case NEW_RELEASE:
                amount += rental.getDaysRented() * 3;
                break;
            case CHILDRENS:
                amount += 1.5;
                if (rental.getDaysRented() > 3)
                    amount += (rental.getDaysRented() - 3) * 1.5;
                break;
        }
        return amount;
    }

    public int calBonus(int frequentRenterPoints, Rental rental) {
        if (_priceCode == NEW_RELEASE && (rental.getDaysRented() > 1))
            frequentRenterPoints++;
        return frequentRenterPoints;
    }

    public String getTitle() {
        return _title;
    }
}