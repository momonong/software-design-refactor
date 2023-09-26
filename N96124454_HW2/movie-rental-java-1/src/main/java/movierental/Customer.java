package movierental;

import java.util.ArrayList;
import java.util.List;

public class Customer {

    private String _name;
    private List<Rental> _rentals = new ArrayList<Rental>();

    public Customer(String name) {
        _name = name;
    }

    public void addRental(Rental arg) {
        _rentals.add(arg);
    }

    public String getName() {
        return _name;
    }

    public String statement() {
        double totalAmount = 0;
        int frequentRenterPoints = 0;
        String result = "<h1>Rental Record for <em>" + getName() + "</em></h1>\n";
        result += "<table>\n";

        for (Rental each : _rentals) {
            double thisAmount = 0;
            Movie movie = each.getMovie();

            //determine amounts for each line
            thisAmount = movie.getAmount(thisAmount, each);
            // add frequent renter points
            frequentRenterPoints++;
            // add bonus for a two day new release rental
            frequentRenterPoints = movie.calBonus(frequentRenterPoints, each);

            // show figures for this rental
            result += "\t<tr><td>" + movie.getTitle() + "</td><td>" + String.valueOf(thisAmount) + "</td></tr>\n";
            totalAmount += thisAmount;
        }

        // add footer lines
        result += "</table>\n";
        result += "<p>Amount owed is <em>" + String.valueOf(totalAmount) + "</em></p>\n";
        result += "<p>You earned <em>" + String.valueOf(frequentRenterPoints) + "</em> frequent renter points<p>";

        return result;
    }
}
