
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="DBData.DataInput" %>

<html>
<head>
    <title>와이파이 정보 구하기</title>
</head>
<body>
<%
    String bookmarkId = request.getParameter("id");

    boolean success = DataInput.deleteBookmark(bookmarkId);

    if (success) {
        out.write("<p>Success</p>");
    } else {
        out.write("<p>Fail</p>");
    }
%>
</body>

<script>
    const isSuccess = document.querySelector("p");

    if (isSuccess.textContent == "Fail") {
        alert("해당 데이터가 없습니다");
    } else if (isSuccess.textContent == "Success") {
        alert("즐겨찾기 그룹 정보를 삭제했습니다");
    } else {
        alert("다른 문제가 발생했습니다.\n관리자에게 해당 문제를 알려주세요");
    }
    location.href="http://localhost:8080/bookmark-group.jsp";
</script>
</html>
