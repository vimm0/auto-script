public class Employee extends Manager{
    public static void main(String[] args){
        Employee emp = new Employee();
        emp.salary = 1000;
        System.out.println("Salary of a employee " + emp.salary);

        Manager mgr = new Manager();
        mgr.salary = 20000;
        System.out.println("Salary of a manager " + mgr.salary);
    }
}