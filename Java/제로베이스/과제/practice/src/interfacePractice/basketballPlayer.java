package interfacePractice;

public class basketballPlayer extends AllPlayer implements Player{

    public String name;
    public basketballPlayer(int num, String club, String name) {
        super(num, club);
        this.name = name;
    }

    public void play() {
        System.out.println("Play Basketball");
    }

    @Override
    public void steal() {
        System.out.println(name + " went for slide tackle");
    }


    @Override
    public void shoot() {
        System.out.println(name + " shoots with his feet");
    }
}
