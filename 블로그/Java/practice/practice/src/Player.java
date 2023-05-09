public class Player {
    void kick() {
        System.out.println("Kick!");
    }
    void head() {
        System.out.println("Head!");
    }
    public static void main(String[] args) {
      Player playerA = new Player();
      playerA.kick();
    }
}
