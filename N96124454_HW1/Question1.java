import java.util.Set;

@SuppressWarnings("unused")
class Person {
    private String name;
    private String address;
    private String ssn;  // social security number
    private int salary;
    private Set<Company> companies;
    // Initialize a Person class 
    public Person(String name, String address, String ssn) {
        this.name = name;
        this.address = address;
        this.ssn = ssn;
        this.salary = 0; // Initialize salary as 0 dollars
    }
    // Implement the charging process 
    public void chargeByProject(int hours, int wage) {
        this.salary += hours*wage;
    }
    // Define a method to get companies person belons to help fire and hire process 
    public Set<Company> getCompanies() {
        return companies;
    }
}

@SuppressWarnings("unused")
class Company {
    private String name;
    private String address;
    private String phoneNumber;
    private String primaryProduct;
    private Set<Person> people;
    // Initialize a Company class
    public Company(String name, String address, String phoneNumber, String primaryProduct) {
        this.name = name;
        this.address = address;
        this.phoneNumber = phoneNumber;
        this.primaryProduct = primaryProduct;
    }
    public void hirePerson(Person person) {
        if (!people.contains(person)) {
            // Add the person into the people set
            people.add((person));
            // Add the company into the companies set
            person.getCompanies().add(this);
        }
    }
    public void firePerson(Person person) {
        if (!people.contains(person)) {
            // Remove the person out of the people set
            people.remove(person);
            // Remove the person out of the propele set
            person.getCompanies().remove(this);
        }
    }
}


