package DBData;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.*;

public class WifiData {
    private static String key = "777a4e78696a656a37344256594177";
    public static ArrayList<JSONObject> allData = new ArrayList<>();

    public static Long getDataCount(){
        /*URL*/

        String dataUrl = "http://openapi.seoul.go.kr:8088";
        dataUrl = dataUrl + "/" + key + "/json" + "/TbPublicWifiInfo" + "/1" + "/5";


        StringBuilder sb = new StringBuilder();
        try {
            URL url = new URL(dataUrl);

            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Content-type", "application/json");

            System.out.println("Response code: " + conn.getResponseCode()); /* 연결 자체에 대한 확인이 필요하므로 추가합니다.*/

            BufferedReader rd;

            // 서비스코드가 정상이면 200~300사이의 숫자가 나옵니다.
            if (conn.getResponseCode() >= 200 && conn.getResponseCode() <= 300) {
                rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            } else {
                rd = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
            }

            String line;
            while ((line = rd.readLine()) != null) {
                sb.append(line);
            }
            rd.close();
            conn.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }


        JSONObject result = null;
        try {
            result = (JSONObject) new JSONParser().parse(sb.toString());
        } catch (ParseException e) {
            throw new RuntimeException(e);
        }

        JSONObject data = (JSONObject) result.get("TbPublicWifiInfo");

        JSONArray rowData = (JSONArray) data.get("row");

        return (Long) data.get("list_total_count");
    }

    public static void getData(int start, int end) {

        String dataUrl = "http://openapi.seoul.go.kr:8088";
        dataUrl = dataUrl + "/" + key + "/json" + "/TbPublicWifiInfo" + String.format("/%d", start) + String.format("/%d", end);

        StringBuilder sb = new StringBuilder();
        try {
            URL url = new URL(dataUrl.toString());

            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Content-type", "application/json");

            System.out.println("Response code: " + conn.getResponseCode()); /* 연결 자체에 대한 확인이 필요하므로 추가합니다.*/

            BufferedReader rd;

            if (conn.getResponseCode() >= 200 && conn.getResponseCode() <= 300) {
                rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            } else {
                rd = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
            }

            String line;
            while ((line = rd.readLine()) != null) {
                sb.append(line);
            }
            rd.close();
            conn.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }


        JSONObject result = null;
        try {
            result = (JSONObject) new JSONParser().parse(sb.toString());
        } catch (ParseException e) {
            throw new RuntimeException(e);
        }

        JSONObject data = (JSONObject) result.get("TbPublicWifiInfo");

        JSONArray rowData = (JSONArray) data.get("row");

        for (int i = 0; i < rowData.size(); i ++) {
            allData.add((JSONObject) rowData.get(i));
        }
    }

    public static ArrayList<JSONObject> getAllData() {
        int dataCount = getDataCount().intValue();

        int s = 1;
        for (int i = 1000; i <= dataCount; i += 1000) {
            getData(s, i);
            s = i + 1;
        }

        getData((dataCount / 1000) * 1000 + 1, dataCount);

        return allData;
    }
}
