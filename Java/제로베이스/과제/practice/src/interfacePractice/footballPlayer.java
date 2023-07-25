package interfacePractice;

public class footballPlayer extends AllPlayer implements Player{

    public String name;

    public footballPlayer(int num, String club, String name) {
        super(num, club);
        this.name = name;
    }

    public void play() {
        System.out.println("Play Football");
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
