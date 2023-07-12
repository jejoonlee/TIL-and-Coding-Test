import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {

        try {
            File file = new File("index.html");
            BufferedWriter writer = new BufferedWriter(new FileWriter(file));
            writer.write("<head>" +
                    "\n\t<meta charset=\"UTF-8\"/>" +
                    "\n\t<style>" +
                    "\n\t\ttable { border-collapse:collapse; width: 100%; }" +
                    "\n\t\tth, td { border: solid 1px #000; }" +
                    "\n\t</style>" +
                    "\n</head>");

            writer.write("\n\n<body>" +
                    "\n<h1>자바 환경정보</h1>" +
                    "\n\t<table>" +
                    "\n\t\t<th>키</th>" +
                    "\n\t\t<th></th>");

            for (Object k : System.getProperties().keySet()) {
                String key = k.toString();
                String value = System.getProperty(key);
                String htmlFormat = String.format("\n\t\t<tr>\n\t\t\t<td>%s</td>\n\t\t\t<td>%s</td>\n\t\t<tr>", key, value);
                writer.write(htmlFormat);
            }

            writer.write("\n\t</table>" +
                    "\n</body>");
            writer.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}