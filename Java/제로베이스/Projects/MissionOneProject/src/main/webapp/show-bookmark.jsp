<%@ page import="DBData.DataInput" %>
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
            font-weight: bold;
        }

        th, td {
            border: 1px solid black;
            text-align: center;
        }
    </style>
</head>

<body>
    <% request.setCharacterEncoding("UTF-8"); %>
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

<div style="display:flex; justify-content: center; margin: 30px 0;">
    <table class="table" style="width: 80%;">
        <thead>
        <tr>
            <th scope="col" style="background-color: #0d6efd;color: white;">ID</th>
            <th scope="col" style="background-color: #0d6efd;color: white;">북마크 이름</th>
            <th scope="col" style="background-color: #0d6efd;color: white;">와이파이명</th>
            <th scope="col" style="background-color: #0d6efd;color: white;">등록일자</th>
            <th scope="col" style="background-color: #0d6efd;color: white;">비고</th>
        </tr>
        </thead>
        <tbody>
        <%
            ArrayList<HashMap<String, String>> data = DataInput.showWifiAndBk();
            String deleteUrl = "http://localhost:8080/show-bookmark/delete.jsp?";

            for (HashMap<String, String> rowData : data) {
                String id = rowData.get("id");
                String urlId = "id=" + id;

                out.write("<tr>");
                out.write("<td>" + id + "</td>");
                out.write("<td>" + rowData.get("bName") + "</td>");
                out.write("<td>" + rowData.get("wName") + "</td>");
                out.write("<td>" + rowData.get("registerTime") + "</td>");

                out.write("<td>" + "<a href='" + deleteUrl + urlId + "' class='btn btn-danger'>삭제</a>" + "</td>");
                out.write("</tr>");
            }
        %>
        </tbody>
    </table>
</div>

</html>
