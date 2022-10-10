public class lesson {
    public static void main(String[] args) {
        yes();
        carLoop();
        day();
        switchCase();
        exception();
    }

    public static void yes() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Yes");
        }
    }

    public static void carLoop() {
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        for (String car : cars) {
            System.out.println(car);
        }
    }

    public static void day() {
        int day = 6;

        if (day == 6) {
            System.out.println("Today is Saturday.");
        }
        else if (day == 7) {
            System.out.println("Today is Sunday.");

        }
        else {
            System.out.println("Looking forward to the weekend.");

        }
    }

    public static void switchCase() {
        int day = 7;

        switch (day) {
            case 6:
                System.out.println("Today is Saturday.");
                break;
            case 7:
                System.out.println("Today is Sunday.");
                break;
            default:
                System.out.println("Looking forward to the weekend.");
        }
    }


    public static void exception() {
        int[] myNumbers = {1, 2, 3};

        try {
            System.out.println(myNumbers[10]);
        } catch (ArrayIndexOutOfBoundsException err) {
            System.out.println(err);
        }
    }
}