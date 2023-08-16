<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="DBData.DataInput"%>
<%@ page import="java.util.*" %>

<html>
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
<h1 style="text-align: center; margin-top:70px;">와이파이 정보 구하기</h1>
<section style="display: flex;align-items: center;justify-content: center;">
    <a href="http://localhost:8080">홈</a>
    <p style="margin: 0 10px;"> | </p>
    <a href="http://localhost:8080/history.jsp">위치 히스토리 목록</a>
    <p style="margin: 0 10px;"> | </p>
    <a class="update-data" href="http://localhost:8080/wifiConfirm.jsp">Open API 와이파이 정보 가져오기</a>
    <p style="margin: 0 10px;"> | </p>
    <a class="update-data" href="http://localhost:8080/show-bookmark.jsp">즐겨 찾기 보기</a>
    <p style="margin: 0 10px;"> | </p>
    <a class="update-data" href="http://localhost:8080/bookmark-group.jsp">즐겨 찾기 그룹 관리</a>
</section>

<div style="display:flex; justify-content: center">
    <table class="table" style="width:80%; margin-top:30px;">
        <thead>
        <tr>
            <th scope="col" style="background-color: #0d6efd;color: white;">ID</th>
            <th scope="col" style="background-color: #0d6efd;color: white;">경도 (Longitude)</th>
            <th scope="col" style="background-color: #0d6efd;color: white;">위도 (Latitude)</th>
            <th scope="col" style="background-color: #0d6efd;color: white;">조회일자</th>
            <th scope="col" style="background-color: #0d6efd;color: white;">비고</th>
        </tr>
        </thead>
        <tbody>
        <% request.setCharacterEncoding("UTF-8"); %>

        <%
            ArrayList<HashMap<String, String>> array = DataInput.showHistory();
            String[] links = new String[array.size()];

            if (array.isEmpty()) {
                out.write("<tr>");
                out.write("<td colspan='5' style='text-align: center'>정보가 존재하지 않습니다</td>");
                out.write("</tr>");
            } else {
                for (int i = 0; i < array.size(); i++) {
                    links[i] = array.get(i).get("historyId");
                }
                for (int i = 0; i < array.size(); i++) {
                    out.write("<tr>");
                    HashMap<String, String> wifiD = array.get(i);
                    out.write("<td style='text-align: center'>" + wifiD.get("historyId") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("lat") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("lng") + "</td>");
                    out.write("<td style='text-align: center'>" + wifiD.get("searchTime") + "</td>");
                    out.write("<td style='text-align: center'>" + "<a class=\"btn btn-danger\" href=\"http://localhost:8080/history/delete.jsp?delete=" + links[i] + "\">삭제 버튼</a>" + "</td>");
                    out.write("</tr>");
                }
            }

        %>
        </tbody>
    </table>
</div>

</body>
</html>