package DBData;

import org.json.simple.JSONObject;
import org.json.simple.parser.ParseException;

import java.math.BigDecimal;
import java.sql.*;
import java.util.*;

public class DataInput {

    public static void dataInsert() {

        ArrayList<HashMap<String, String>> data = WifiData.getAllData();

        Connection con = null;

        try {
            // SQLite JDBC 체크
            Class.forName("org.sqlite.JDBC");

            // SQLite 데이터베이스 파일에 연결
            String dbFile = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\TIL\\Java\\제로베이스\\Projects\\MissionOne\\MissionOneProject\\seoulWifi.db";
            con = DriverManager.getConnection("jdbc:sqlite:" + dbFile);

            for (HashMap<String, String> mapData : data) {
                // SQL 수행
                Statement stat = con.createStatement();

                String sql =
                        "insert into wifiInfo (manage_num, Gu, wifi_name, address1, address2, building_floor, install_type, install_company, service_type, connection_type, install_year, in_or_out, wifi_con, lat, long, work_time)" +
                                "values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

                PreparedStatement statement = con.prepareStatement(sql);

                statement.setString(1, mapData.get("X_SWIFI_MGR_NO")); // manage_num, string

                statement.setString(2, mapData.get("X_SWIFI_WRDOFC")); // Gu, string
                statement.setString(3, mapData.get("X_SWIFI_MAIN_NM")); // wifi_name, string
                statement.setString(4, mapData.get("X_SWIFI_ADRES1")); // address1, string
                statement.setString(5, mapData.get("X_SWIFI_ADRES2")); // address2, string
                statement.setString(6, mapData.get("X_SWIFI_INSTL_FLOOR")); // building_floor, integer
                statement.setString(7, mapData.get("X_SWIFI_INSTL_TY")); // install_type, string
                statement.setString(8, mapData.get("X_SWIFI_INSTL_MBY")); // install_company, string
                statement.setString(9, mapData.get("X_SWIFI_SVC_SE")); // service_type, string
                statement.setString(10, mapData.get("X_SWIFI_CMCWR")); // connection_type, string

                int year = Integer.parseInt(mapData.get("X_SWIFI_CNSTC_YEAR"));
                statement.setInt(11, year); // install_year, integer
                statement.setString(12, mapData.get("X_SWIFI_INOUT_DOOR")); // in_or_out, string
                statement.setString(13, mapData.get("X_SWIFI_REMARS3")); // wifi_con, string

                BigDecimal num1 = new BigDecimal(mapData.get("LAT"));
                BigDecimal num2 = new BigDecimal(mapData.get("LNT"));
                BigDecimal latitude = null;
                BigDecimal longitude = null;

                if (num1.compareTo(num2) == 1) {
                    longitude = num1;
                    latitude = num2;
                } else if (num2.compareTo(num1) == 1) {
                    longitude = num2;
                    latitude = num1;
                }

                statement.setBigDecimal(14, latitude); // lat, integer
                statement.setBigDecimal(15, longitude); // long, Integer


                statement.setString(16, mapData.get("WORK_DTTM")); // worktime, datetime

                int affected = statement.executeUpdate();
                if (affected > 0) System.out.println(mapData.get("X_SWIFI_MGR_NO") + ": success");
                else System.out.println("fail");

            }

        }catch(Exception e) {
            e.printStackTrace();
        }finally {
            if(con != null) {
                try {con.close();}catch(Exception e) {}
            }
        }
    }

    public static int dataUpdate() {
        ArrayList<HashMap<String, String>> data = WifiData.getAllData();

        Connection con = null;

        try {
            // SQLite JDBC 체크
            Class.forName("org.sqlite.JDBC");

            // SQLite 데이터베이스 파일에 연결
            String dbFile = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\TIL\\Java\\제로베이스\\Projects\\MissionOne\\MissionOneProject\\seoulWifi.db";

            Properties props = new Properties();
            props.put("charSet", "utf-8");

            con = DriverManager.getConnection("jdbc:sqlite:" + dbFile, props);

            for (HashMap<String, String> jsonData : data) {
                // SQL 수행
                Statement stat = con.createStatement();

                // 데이터를 아예 업데이트 할 떄에는 insert or replace으로
                String sql =
                        "insert or ignore into wifiInfo (manage_num, Gu, wifi_name, address1, address2, building_floor, install_type, install_company, service_type, connection_type, install_year, in_or_out, wifi_con, lat, long, work_time)" +
                                "values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

                PreparedStatement statement = con.prepareStatement(sql);

                String manageNum = jsonData.get("X_SWIFI_MGR_NO");
                statement.setString(1, manageNum); // manage_num, string

                statement.setString(2, jsonData.get("X_SWIFI_WRDOFC")); // Gu, string
                statement.setString(3, jsonData.get("X_SWIFI_MAIN_NM")); // wifi_name, string
                statement.setString(4, jsonData.get("X_SWIFI_ADRES1")); // address1, string
                statement.setString(5, jsonData.get("X_SWIFI_ADRES2")); // address2, string
                statement.setString(6, jsonData.get("X_SWIFI_INSTL_FLOOR")); // building_floor, integer
                statement.setString(7, jsonData.get("X_SWIFI_INSTL_TY")); // install_type, string
                statement.setString(8, jsonData.get("X_SWIFI_INSTL_MBY")); // install_company, string
                statement.setString(9, jsonData.get("X_SWIFI_SVC_SE")); // service_type, string
                statement.setString(10, jsonData.get("X_SWIFI_CMCWR")); // connection_type, string

                int year = Integer.parseInt(jsonData.get("X_SWIFI_CNSTC_YEAR"));
                statement.setInt(11, year); // install_year, integer
                statement.setString(12, jsonData.get("X_SWIFI_INOUT_DOOR")); // in_or_out, string
                statement.setString(13, jsonData.get("X_SWIFI_REMARS3")); // wifi_con, string

                BigDecimal num1 = new BigDecimal(jsonData.get("LAT"));
                BigDecimal num2 = new BigDecimal(jsonData.get("LNT"));
                BigDecimal latitude = null;
                BigDecimal longitude = null;

                if (num1.compareTo(num2) == 1) {
                    longitude = num1;
                    latitude = num2;
                } else if (num2.compareTo(num1) == 1) {
                    longitude = num2;
                    latitude = num1;
                }

                statement.setBigDecimal(14, latitude); // lat, integer
                statement.setBigDecimal(15, longitude); // long, Integer

                statement.setString(16, jsonData.get("WORK_DTTM")); // worktime, datetime


                int affected = statement.executeUpdate();
                if (affected > 0) System.out.println(manageNum + ": success");
            }

        }catch(Exception e) {
            e.printStackTrace();
        }finally {
            if(con != null) {
                try {con.close();}catch(Exception e) {}
            }
        }

        return data.size();
    }

    public static void dataAllDelete() {

        Connection con = null;

        try {
            // SQLite JDBC 체크
            Class.forName("org.sqlite.JDBC");

            // SQLite 데이터베이스 파일에 연결
            String dbFile = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\TIL\\Java\\제로베이스\\Projects\\MissionOne\\MissionOneProject\\seoulWifi.db";
            con = DriverManager.getConnection("jdbc:sqlite:" + dbFile);


            Statement stat = con.createStatement();

            // 데이터를 아예 업데이트 할 떄에는 insert or replace으로
            String sql =
                    "delete from wifiInfo";

            PreparedStatement statement = con.prepareStatement(sql);
            statement.executeUpdate();


        }catch(Exception e) {
            e.printStackTrace();
        }finally {
            if(con != null) {
                try {con.close();}catch(Exception e) {}
            }
        }
    }

    public static ArrayList<HashMap<String, String>> getCloseWifi(BigDecimal latitude, BigDecimal longitude) {
        Connection con = null;
        ResultSet resultSet = null;
        ArrayList<HashMap<String, String>> array = new ArrayList<>();

        try {
            // SQLite JDBC 체크
            Class.forName("org.sqlite.JDBC");

            // SQLite 데이터베이스 파일에 연결
            String dbFile = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\TIL\\Java\\제로베이스\\Projects\\MissionOne\\MissionOneProject\\seoulWifi.db";
            con = DriverManager.getConnection("jdbc:sqlite:" + dbFile);


            Statement stat = con.createStatement();

            String sql =
                    "SELECT *, Round(( 6371 * acos( cos( radians(?) ) * cos( radians( lat ) ) * cos( radians(?) - radians(long) ) + sin( radians(?) ) * sin( radians(lat)))), 4) AS dist" +
                            " FROM wifiInfo" +
                            " WHERE lat is not null and long is not null" +
                            " ORDER BY dist ASC" +
                            " Limit 20";

            PreparedStatement statement = con.prepareStatement(sql);

            statement.setString(1, latitude.toString());
            statement.setString(2, longitude.toString());
            statement.setString(3, latitude.toString());

            resultSet = statement.executeQuery();

            while(resultSet.next()) {
                HashMap<String, String> tempMap = new HashMap<>();

                tempMap.put("dist", resultSet.getString("dist"));
                tempMap.put("manage_num", resultSet.getString("manage_num"));
                tempMap.put("gu", resultSet.getString("Gu"));
                tempMap.put("wifi_name", resultSet.getString("wifi_name"));
                tempMap.put("address1", resultSet.getString("address1"));
                tempMap.put("address2", resultSet.getString("address2"));
                tempMap.put("building_floor", resultSet.getString("building_floor"));
                tempMap.put("install_type", resultSet.getString("install_type"));
                tempMap.put("install_company", resultSet.getString("install_company"));
                tempMap.put("service_type", resultSet.getString("service_type"));
                tempMap.put("connection_type", resultSet.getString("connection_type"));
                tempMap.put("install_year", resultSet.getString("install_year"));
                tempMap.put("in_or_out", resultSet.getString("in_or_out"));
                tempMap.put("wifi_con", resultSet.getString("wifi_con"));
                tempMap.put("lat", resultSet.getString("lat"));
                tempMap.put("long", resultSet.getString("long"));
                tempMap.put("work_time", resultSet.getString("work_time"));

                array.add(tempMap);
            }

        }catch(Exception e) {
            e.printStackTrace();
        }finally {
            if(con != null) {
                try {con.close();}catch(Exception e) {}
            }
        }

        return array;
    }

    public static void saveInHistory(String lat, String lng) {

        Connection con = null;

        try {
            // SQLite JDBC 체크
            Class.forName("org.sqlite.JDBC");

            // SQLite 데이터베이스 파일에 연결
            String dbFile = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\TIL\\Java\\제로베이스\\Projects\\MissionOne\\MissionOneProject\\seoulWifi.db";
            con = DriverManager.getConnection("jdbc:sqlite:" + dbFile);

            // SQL 수행
            Statement stat = con.createStatement();

            String sql =
                    "INSERT into History (lat, long, search_time)\n" +
                            "values (?, ?, datetime('now', 'localtime'))";


            PreparedStatement statement = con.prepareStatement(sql);
            statement.setString(1, lat);
            statement.setString(2, lng);

            statement.executeUpdate();

        }catch(Exception e) {
            e.printStackTrace();
        }finally {
            if(con != null) {
                try {con.close();}catch(Exception e) {}
            }
        }
    }

    public static ArrayList<HashMap<String, String>> showHistory() {
        Connection con = null;
        ResultSet resultSet = null;
        ArrayList<HashMap<String, String>> array = new ArrayList<>();

        try {
            // SQLite JDBC 체크
            Class.forName("org.sqlite.JDBC");

            // SQLite 데이터베이스 파일에 연결
            String dbFile = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\TIL\\Java\\제로베이스\\Projects\\MissionOne\\MissionOneProject\\seoulWifi.db";
            con = DriverManager.getConnection("jdbc:sqlite:" + dbFile);


            Statement stat = con.createStatement();

            String sql =
                    "SELECT * from History";

            PreparedStatement statement = con.prepareStatement(sql);

            resultSet = statement.executeQuery();

            while(resultSet.next()) {
                HashMap<String, String> tempMap = new HashMap<>();

                tempMap.put("historyId", resultSet.getString("history_id"));
                tempMap.put("lat", resultSet.getString("lat"));
                tempMap.put("lng", resultSet.getString("long"));
                tempMap.put("searchTime", resultSet.getString("search_time"));

                array.add(tempMap);
            }

        }catch(Exception e) {
            e.printStackTrace();
        }finally {
            if(con != null) {
                try {con.close();}catch(Exception e) {}
            }
        }

        return array;

    }

    public static void deleteHistory(int id) {
        Connection con = null;

        try {
            // SQLite JDBC 체크
            Class.forName("org.sqlite.JDBC");

            // SQLite 데이터베이스 파일에 연결
            String dbFile = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\TIL\\Java\\제로베이스\\Projects\\MissionOne\\MissionOneProject\\seoulWifi.db";
            con = DriverManager.getConnection("jdbc:sqlite:" + dbFile);


            Statement stat = con.createStatement();


            String sql =
                    "delete from History WHERE history_id = ?";

            PreparedStatement statement = con.prepareStatement(sql);

            statement.setInt(1, id);

            int confirm = statement.executeUpdate();

            if (confirm > 0) System.out.println("Success");

        }catch(Exception e) {
            e.printStackTrace();
        }finally {
            if(con != null) {
                try {con.close();}catch(Exception e) {};
            }
        }

    }

    public static HashMap<String, String> getDetailData(String code) {
        Connection con = null;
        ResultSet resultSet = null;
        HashMap<String, String> map = new HashMap<>();

        try {
            // SQLite JDBC 체크
            Class.forName("org.sqlite.JDBC");

            // SQLite 데이터베이스 파일에 연결
            String dbFile = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\TIL\\Java\\제로베이스\\Projects\\MissionOne\\MissionOneProject\\seoulWifi.db";
            con = DriverManager.getConnection("jdbc:sqlite:" + dbFile);


            Statement stat = con.createStatement();

            String sql =
                    "select * from wifiInfo where manage_num = ?";

            PreparedStatement statement = con.prepareStatement(sql);

            statement.setString(1, code);

            resultSet = statement.executeQuery();

            while(resultSet.next()) {
                map.put("manage_num", resultSet.getString("manage_num"));
                map.put("gu", resultSet.getString("Gu"));
                map.put("wifi_name", resultSet.getString("wifi_name"));
                map.put("address1", resultSet.getString("address1"));
                map.put("address2", resultSet.getString("address2"));
                map.put("building_floor", resultSet.getString("building_floor"));
                map.put("install_type", resultSet.getString("install_type"));
                map.put("install_company", resultSet.getString("install_company"));
                map.put("service_type", resultSet.getString("service_type"));
                map.put("connection_type", resultSet.getString("connection_type"));
                map.put("install_year", resultSet.getString("install_year"));
                map.put("in_or_out", resultSet.getString("in_or_out"));
                map.put("wifi_con", resultSet.getString("wifi_con"));
                map.put("lat", resultSet.getString("lat"));
                map.put("long", resultSet.getString("long"));
                map.put("work_time", resultSet.getString("work_time"));
            }
        }catch(Exception e) {
            e.printStackTrace();
        }finally {
            if(con != null) {
                try {con.close();}catch(Exception e) {}
            }
        }

        return map;
    }
}
