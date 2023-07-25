package interfacePractice;

public abstract class AllPlayer {
    public int num;
    public String club;

    public AllPlayer(int num, String club) {
        this.num = num;
        this.club = club;
    }

    public abstract void play();
}
