public class dbTestMain {
    public static void main(String[] args) {
        DbTest dbTest = new DbTest();

        dbTest.dbRead();
//        dbTest.dbInsert();
//        dbTest.dbUpdate();
        dbTest.dbDelete();
        dbTest.dbRead();
    }
}
