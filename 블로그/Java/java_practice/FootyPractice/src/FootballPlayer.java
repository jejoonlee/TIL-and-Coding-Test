public class FootballPlayer {
    private String name;
    private int number;
    private int age;
    private Club footballClub;

    public FootballPlayer(String name, int age, int number, Club club) {
        this.name = name;
        this.age = age;
        this.number = number;
        this.footballClub = club;
    }

    void printPlayerInfo() {
        System.out.println("Player Name : " + this.name);
        System.out.println("Player Number : " + this.number);
        System.out.println("Player Age : " + this.age);
        System.out.println("Club : " + this.footballClub.getclubName());
    }
}
