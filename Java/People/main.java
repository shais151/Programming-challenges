public class main {
    public static Person[] load_people(String[][] information) {
        Person[] loaded = new Person[3];
        for (int i = 0; i < 3; i++) {
            loaded[i] = new Person(information[i][0], information[i][1]);
        }
        return loaded;
    }

    String[][] people = {
            {"James", "M"},
            {"Jane", "F"},
            {"Alex", "B"}
    };

    Person[] people_classes = load_people(people);
}