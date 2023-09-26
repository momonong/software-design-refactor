import java.util.HashSet;
import java.util.Set;

@SuppressWarnings("unused")
class Person {
    private String name;
    private String position;
    // Initialize person profile
    public void setProfile(String name, String position) {
        this.name = name;
        this.position = position;
    }
}

class Manager extends Person {
    private Set<Project> projects;
    public Manager(String name) {
        setProfile(name, "manager");
        this.projects = new HashSet<>();
    }
    public void addProject(Project project) {
        projects.add(project);
    }
}
@SuppressWarnings("unused")
class Worker extends Person {
    private Project project;
    public Worker(String name) {
        setProfile(name, "worker");
    }
    public void setProject(Project project) {
        this.project = project;
    }
}

@SuppressWarnings("unused")
class Project {
    private String name;
    private int budget;
    private int priority;
    private Manager manager;
    private Set<Worker> workers;
    // Initialize a project
    public Project(String name, int budget, int priority, Manager manager) {
        this.name = name;
        this.budget = budget;
        this.priority = priority;
        this.manager = manager;
        this.workers = new HashSet<>();
    }
    // Implement prcoess of adding a worker
    public void addWorker(Worker worker) {
        workers.add(worker);
    }
    // Implement process of removing a worker
    public void removeWorker(Worker worker) {
        workers.remove(worker);
    }
}