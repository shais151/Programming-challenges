public class TinyLife {
    public static void main(String args[]) throws Exception {
//        test();
        play(Long.decode(args[0]));
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
        return (col > 7 | col < 0 | row > 7 | row < 0) ? false : PackedLong.get(world, (col+ 8*row));
    }

    public static long setCell(long world, int col, int row, boolean value) {
        return (col > 7 | col < 0 | row > 7 | row < 0) ? false : PackedLong.set(world, (col+ 8*row), value);
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
        // Number of neighbours next to cell that will be returned
        int neighbours = 0;



        return neighbours;
    }

    public static boolean computeCell(long world, int col, int row) {
        // liveCell is true if the cell at postion (col,row) in world is live
        boolean liveCell = getCell(world, col, row);
        // neighbours is the number of live neighbours to cell (col,row)
        int neighbours = countNeighbours(world, col, row);
        /*
         * we will return this value at the end of the method to indicate whether
         * cell (col,row) should be live in the next generation
         */
        boolean nextCell = false;
        // A live cell with less than two neighbours dies (underpopulation)
        if (neighbours < 2) nextCell = false;
        // A live cell with two or three neighbours lives (a balanced population
        if (liveCell && neighbours == 2 || liveCell && neighbours == 3) nextCell = true;
        // A live cell with more than three neighbours dies (overcrowding)
        if (neighbours > 3) nextCell = false;
        //
        if (!liveCell && neighbours == 3) nextCell = true;

        return nextCell;
    }

    public static long nextGeneration(long world) {

    }

    public static void play(long world) throws Exception {
        int userResponse = 0;
        while (userResponse != 'q') {
            print(world);
            userResponse = System.in.read();
            world = nextGeneration(world);
        }
    }
}
