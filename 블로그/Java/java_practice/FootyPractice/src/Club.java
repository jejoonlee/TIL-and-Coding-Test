public class Club {
    private String clubName;
    private String location;
    private String stadium;
    public Club (String name, String location, String stadium) {
        this.clubName = name;
        this.location = location;
        this.stadium = stadium;
    }

    public String getclubName () {
        return this.clubName;
    }
}
