<%@ page import="DBData.DataInput" %>
<%@ page import="java.math.BigDecimal" %>
<%@ page import="java.util.HashMap" %>
<%@ page import="java.util.ArrayList" %>
<%@ page import="java.net.URLEncoder" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>

<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>와이파이 정보 구하기</title>
    <style>
        th {
            font-size: small;
            font-weight: bold;
            text-align: center;
        }

        th, td {
            border: 1px solid black;
        }
    </style>
</head>

<body>
<% request.setCharacterEncoding("UTF-8"); %>
<h1 style="text-align: center;">와이파이 정보 구하기</h1>
<section style="display: flex;align-items: center;justify-content: center;">
    <a href="http://localhost:8080">홈</a>
    <p style="margin: 0 10px;"> | </p>
    <a href="http://localhost:8080/history.jsp">위치 히스토리 목록</a>
    <p style="margin: 0 10px;"> | </p>
    <a class="update-data" href="http://localhost:8080/wifiConfirm.jsp">Open API 와이파이 정보 가져오기</a>
</section>

<section class="my_loc" style="display: flex;align-items: center;justify-content: center; margin: 20px 0;">
    <form action="http://localhost:8080" method="post" style="display:flex;">
        <%
            if (request.getParameter("longitude")==null && request.getParameter("latitude")==null) {
                out.write("<div style=\"display:flex;margin-right: 20px;\"><p style=\"margin-bottom:0;margin-right: 10px;\">LAT: </p>");
                out.write("<input class=\"lati\" type=\"text\" name=\"latitude\" value=\"0.0\"></div>");
                out.write("<div style=\"display:flex;margin-right: 20px;\"><p style=\"margin-bottom:0;margin-right: 10px;\">LNG: </p>");
                out.write("<input class=\"long\" type=\"text\" name=\"longitude\" value=\"0.0\"></div>");
            } else {
                out.write("<div style=\"display:flex;margin-right: 20px;\"><p style=\"margin-bottom:0;margin-right: 10px;\">LAT: </p>");
                out.write("<input class=\"lati\" type=\"text\" name=\"latitude\" value=" + request.getParameter("latitude") + "></div>");
                out.write("<div style=\"display:flex;margin-right: 20px;\"><p style=\"margin-bottom:0;margin-right: 10px;\">LNG: </p>");
                out.write("<input class=\"long\" type=\"text\" name=\"longitude\" value="+ request.getParameter("longitude") +"></div>");
            }
        %>
        <input class="btn btn-primary" style="padding: 3px 10px;" type="submit" value="근처 WiFI 정보 보기">
    </form>
    <button class="find-my-loc btn btn-success" style="padding: 3px 10px;margin-left:20px">내 위치 가져오기</button>
</section>
<table class="table">
    <thead>
    <tr>
        <th scope="col" style="background-color: #0d6efd;color: white;">거리(Km)</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">관리번호</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">자치구</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">와이파이명</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">도로명주소</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">상세주소</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">설치위치(층)</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">설치유형</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">설치기관</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">서비스구분</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">망종류</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">설치년도</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">실내외구분</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">WIFI 접속환경</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">경도</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">위도</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">작업일자</th>
    </tr>
    </thead>
    <tbody>
        <%
            String lng = request.getParameter("longitude");
            String lati = request.getParameter("latitude");

            if (lng == null && lati == null) {
                out.write("<tr>");
                out.write("<td colspan='17' style='text-align: center'>" + "위치 정보를 입력한 후에 조회해 주세요"+ "</td>");
                out.write("</tr>");
            } else if (lng.equals("0.0") && lati.equals("0.0")) {
                out.write("<tr>");
                out.write("<td colspan='17' style='text-align: center'>" + "위치 정보를 입력한 후에 조회해 주세요"+ "</td>");
                out.write("</tr>");
            } else {
                DataInput.saveInHistory(lati, lng);
                BigDecimal latitude = new BigDecimal(lati);
                BigDecimal longitude = new BigDecimal(lng);

                ArrayList<HashMap<String, String>> array = DataInput.getCloseWifi(latitude, longitude);

                for (int i = 0; i < array.size(); i++) {
                    out.write("<tr>");
                    HashMap<String, String> wifiD = array.get(i);

                    String distance = wifiD.get("dist");
                    out.write("<td style='text-align: center'>" + wifiD.get("dist") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("manage_num") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("gu") + "</td>");

                    System.out.println(wifiD.get("manage_num"));
                    String mngNum = URLEncoder.encode(wifiD.get("manage_num"), "UTF-8");
                    System.out.println(mngNum);
                    out.write("<td style='text-align: center'><a href=\"http://localhost:8080/detail.jsp?wifi="+ wifiD.get("manage_num") + "&dist=" + distance +"\">" + wifiD.get("wifi_name") + "</a></td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("address1") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("address2") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("building_floor") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("install_type") + "</td>");

                    String installCom = wifiD.get("install_company");
                    if(installCom == null) installCom = "";
                    out.write("<td style='text-align: center'>" + installCom + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("service_type") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("connection_type") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("install_year") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("in_or_out") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("wifi_con") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("long") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("lat") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("work_time") + "</td>");
                    out.write("</tr>");
                }
            }
        %>
    </tbody>
</table>
</body>
<script type="text/javascript" src="findLoc.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
</html>