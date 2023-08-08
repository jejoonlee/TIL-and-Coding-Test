<%@ page language="java" contentType="text/html; charset=euc_kr" pageEncoding="euc_kr" %>
<%@ page import="DBData.DataInput"%>
<%@ page import="org.json.simple.parser.ParseException" %>
<% request.setCharacterEncoding("euc_kr"); %>

<html>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">

<head>
    <title>와이파이 정보 구하기</title>
</head>
<body>
    <div style="text-align: center">
        <%
            String dataSize = String.format("%d", DataInput.dataUpdate());
            out.write("<h1 style='margin: 30px 0px'>" + dataSize + "개의 WIFI정보를 정상적으로 저장하였습니다" + "</h1>");
        %>
        <a class="btn btn-primary" href="http://localhost:8080/MissionOneProject_war_exploded/index.jsp" role="button" style="text-align:center;padding: 3px 10px;margin-right:20px">홈으로 가기</a>
    </div>
</body>
</html>
