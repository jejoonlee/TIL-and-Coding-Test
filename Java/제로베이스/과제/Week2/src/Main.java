public class Main {
    public static void main(String[] args) {
        LinkedList2 myList = new LinkedList2(new Node (1, null));
        myList.printData();

        myList.addLast(2);
        myList.addLast(3);
        myList.addLast(4);
        myList.addLast(5);
        myList.addLast(6);
        myList.addLast(7);
        myList.printData();

        myList.addData(100, 1);
        myList.addData(200, 2);
        myList.addData(300, 3);
        myList.addData(400, 4);
        myList.addData(500, 5);
        myList.addData(600, 6);
        myList.printData();

        myList.removeData(100);
        myList.removeData(200);
        myList.removeData(300);
        myList.removeData(400);
        myList.removeData(500);
        myList.removeData(600);
        myList.printData();
    }
}