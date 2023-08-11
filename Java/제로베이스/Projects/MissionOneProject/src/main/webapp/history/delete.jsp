<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="DBData.DataInput"%>

<html>
<head>
    <meta charset="UTF-8">
    <title>좌표 검색 기록 삭제 페이지</title>
</head>
<body>

    <% request.setCharacterEncoding("UTF-8"); %>
    <%
        String deleteId = request.getParameter("delete");
        int id = Integer.parseInt(deleteId);
        DataInput.deleteHistory(id);
    %>
</body>
<script>
    location.href="http://localhost:8080/history.jsp";
</script>
</html>
