
import java.util.Random;
public class Person {
    public static void Person(String Name, String Gender) {
        String name = Name;
        String gender = Gender;
    }

    Random rand = new Random();
    int int_random = rand.nextInt(0xFFF);
    String favourite_colour = int_random + "03x";

    String dob = "";

    public String get_dob() {
        return dob;
    }

    public void set_Dob(String date) {
         dob = date;
    }

    public static String[] people = new String[3];
}