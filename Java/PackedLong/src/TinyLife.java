public class TinyLife {
    public static void main(String args[]) throws Exception {
        test();
    }

    public static void test() {
        System.out.println(getCell(0x20A0600000000000L,1,1));
        System.out.println(getCell(0x20A0600000000000L,-1,1));
        System.out.println(getCell(0x20A0600000000000L,3,8));
        System.out.println(getCell(0x20A0600000000000L,1,-12));
        System.out.println(getCell(0x20A0600000000000L,72,2));
        System.out.println(getCell(0x20A0600000000000L,5,5));
        System.out.println(getCell(0x20A0600000000000L,5,6));
        System.out.println(getCell(0x20A0600000000000L,6,6));
    }

    public static boolean getCell(long world, int col, int row) {
        if (col > 7 | col < 0 | row > 7 | row < 0) {
            return false;
        }
        return true;
    }

    public static long setCell(long world, int col, int row, boolean value) {
        PackedLong.set();
    }

    public static void print(long world) {
        System.out.println("-");
        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                System.out.println(getCell(world,col,row) ? "#" : "_");
            }
            System.out.println();
        }
    }

    public static int countNeighbours(long world, int col, int row) {
        return 0;
    }

    public static boolean computeCell(long world, int col, int row) {
        return true;
    }

    public static long nextGeneration(long world) {
        return 0;
    }
}
