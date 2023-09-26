package movierental;

public abstract class Movie {

    private String _title;

    public Movie(String title){
        _title = title;
    }

    public abstract double getAmount(double amounts, Rental rental);

    public int calBonus(int frequentRenterPoints, Rental rental) {
        return frequentRenterPoints;
    }

    public String getTitle() {
        return _title;
    }
}