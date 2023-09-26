import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Company {
    private Set<Department> departments; // each department within a company is uniquely identified by its name
    public Company() {
        departments = new HashSet<>();
    }
    public void addDepartment(Department department) {
        departments.add(department);
    }
}

@SuppressWarnings("unused")
class Department {
    private String name;
    private Manager manager;
    private List<Product> products = new ArrayList<>();
    public Department(String name) {
        this.name = name;
    }
    public void setManager(Manager manager) {
        this.manager = manager;
        manager.setDepartment(this);
    }
    public void addProduct(Product product) {
        products.add(product);
        product.setDepartment(this);
    }
}

@SuppressWarnings("unused")
class Manager {
    private Department department;
    private String name;
    public Manager(String name) {
        this.name = name;
    }
    public void setDepartment(Department department) {
        this.department = department;
    }
}

@SuppressWarnings("unused")
class Product {
    private String name;
    private int cost;
    private double weight;
    private Department department;
    public Product(String name, int cost, double weight) {
        this.name = name;
        this.cost = cost;
        this.weight = weight;
    }
    public void setDepartment(Department department) {
        this.department = department;
    }
}