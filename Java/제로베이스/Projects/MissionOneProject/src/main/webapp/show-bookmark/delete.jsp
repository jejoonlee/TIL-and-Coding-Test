<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="DBData.DataInput" %>

<html>
<head>
  <title>와이파이 정보 구하기</title>
</head>
<body>
<%
  request.setCharacterEncoding("UTF-8");
  String id = request.getParameter("id");

  boolean success = DataInput.deleteWifiFromBookmark(id);

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
    alert("해당 정보를 성공적으로 삭제하지 못했습니다");
  } else if (isSuccess.textContent == "Success") {
    alert("해당 정보를 성공적으로 삭제했습니다");
  } else {
    alert("다른 문제가 발생했습니다.\n관리자에게 해당 문제를 알려주세요");
  }

  location.href="http://localhost:8080/show-bookmark.jsp";
</script>
</html>

