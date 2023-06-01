// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        Club manUtd = new Club("Manchester United", "Manchester", "Old Trafford");
        FootballPlayer player1 = new FootballPlayer("Rashford", 24, 10, manUtd);

        player1.printPlayerInfo();
    }
}