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
    .names{
      background-color: #0d6efd;
      color: white;
      text-align: center;
      font-weight : bold;
    }
    .names, .info{
      padding: 10px 70px;
      border: solid #cecece 1px;
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

<a></a>

<form action="http://localhost:8080/bookmark-group-add/submit.jsp" method="get">
  <table style="display:flex; justify-content: center; margin:30px 0">
    <tbody>
    <tr>
      <td class="names">즐겨찾기 이름</td>
      <td class="info"><input name="bName"></td>
    </tr>
    <tr>
      <td class="names">순서</td>
      <td class="info"><input name="bOrder"></td>
    </tr>
    <tr>
      <td colspan="2" style="text-align: center; border: solid 1px #cecece"><button type="submit" class="btn btn-success" style="margin: 10px 0;">추가</button></td>
    </tr>
    </tbody>
  </table>
</form>

</body>
<script type="text/javascript" src="findLoc.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
</html>
